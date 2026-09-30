"""
IELTS Writing Agent State Schema Definition
File: docs/architecture/state_schema.py

Đặc tả IELTSWritingState sử dụng trong LangGraph Execution Pipeline.
Đảm bảo an toàn race-condition khi Fan-in kết quả từ 4 Evaluators (TA/TR, CC, LR, GRA)
và đảm bảo Rào chắn (Barrier) chỉ mở cho Verifier khi ĐỦ CẢ 4/4 Evaluators hoàn tất.
"""

from typing import List, Dict, Any, Optional, Literal, Annotated
from pydantic import BaseModel, Field, model_validator
from typing_extensions import TypedDict


# ==========================================
# 1. PYDANTIC DOMAIN SCHEMAS
# ==========================================

class ErrorSpan(BaseModel):
    """Đặc tả vị trí và loại lỗi trong bài viết."""
    start_char: int = Field(..., description="Chỉ số ký tự bắt đầu của lỗi")
    end_char: int = Field(..., description="Chỉ số ký tự kết thúc của lỗi")
    error_type: Literal[
        "GRAMMAR", "SPELLING", "WORD_CHOICE", "COLLOCATION", 
        "PUNCTUATION", "COHESION", "TASK_COVERAGE"
    ] = Field(..., description="Phân loại lỗi theo Closed Taxonomy")
    original_text: str = Field(..., description="Trích đoạn văn bản gốc bị lỗi")
    suggestion: str = Field(..., description="Gợi ý sửa đổi chuẩn xác")
    explanation: str = Field(..., description="Giải thích lý do sai bằng tiếng Việt/Anh")


class CriterionScore(BaseModel):
    """Đặc tả kết quả chấm điểm cho 1 tiêu chí Rubric (TA/TR, CC, LR, GRA)."""
    criterion: Literal["TA_TR", "CC", "LR", "GRA"] = Field(..., description="Tên tiêu chí chấm")
    band_score: float = Field(..., ge=0.0, le=9.0, description="Điểm Band từ 0.0 - 9.0 (bước nhảy 0.5)")
    sub_scores: Dict[str, float] = Field(default_factory=dict, description="Điểm thành phần chi tiết")
    verbatim_quotes: List[str] = Field(default_factory=list, description="Dẫn chứng trích đoạn nguyên văn từ bài viết")
    reasoning: str = Field(..., description="Lập luận chấm điểm chi tiết")
    identified_errors: List[ErrorSpan] = Field(default_factory=list, description="Danh sách các lỗi phát hiện")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Độ tin cậy của đánh giá")
    grounded: bool = Field(default=True, description="Cờ đánh dấu kết quả đã qua xác thực Tool/Exemplar")


class VisualFacts(BaseModel):
    """Cấu trúc dữ liệu số liệu trích xuất từ biểu đồ Task 1 Academic."""
    chart_type: str = Field(..., description="Loại biểu đồ: line, bar, pie, table, process, map")
    key_trends: List[str] = Field(default_factory=list, description="Các xu hướng chính / đặc điểm chính")
    data_points: Dict[str, Any] = Field(default_factory=dict, description="Tập dữ liệu điểm số, tỷ lệ, cực trị trích xuất")
    units: Optional[str] = Field(None, description="Đơn vị đo lường (%, USD, người...)")


class EvaluationPlan(BaseModel):
    """Kế hoạch phân bổ đánh giá từ Coordinator."""
    task_type: Literal["TASK_1_ACADEMIC", "TASK_2"] = Field(..., description="Loại đề thi")
    detected_prompt_requirements: List[str] = Field(..., description="Các yêu cầu bắt buộc của đề bài")
    requires_visual_extraction: bool = Field(default=False, description="Có cần trích xuất ảnh không")
    routing_confidence: float = Field(..., ge=0.0, le=1.0)


class VerificationReport(BaseModel):
    """
    Báo cáo kiểm định độc lập từ Verifier Node (Claude Opus 5).
    Chỉ được khởi tạo khi đã gom đủ 4/4 tiêu chí chấm điểm.
    """
    approved: bool = Field(..., description="Trạng thái duyệt kết quả chấm")
    overall_band: float = Field(..., ge=0.0, le=9.0, description="Điểm Band Overall cuối cùng đã làm tròn")
    task_band: float = Field(..., ge=0.0, le=9.0, description="Điểm Band cho Task hiện tại")
    score_caps_applied: List[str] = Field(default_factory=list, description="Danh sách các trần điểm bị áp dụng")
    fabricated_quotes_detected: List[str] = Field(default_factory=list, description="Các câu trích dẫn bịa đặt phát hiện")
    conflict_detected: bool = Field(default=False, description="Có phát hiện mâu thuẫn điểm/lập luận không")
    revision_targets: List[str] = Field(default_factory=list, description="Tiêu chí cần chấm lại nếu conflict")


class TutorFeedback(BaseModel):
    """Phản hồi định hướng sư phạm cho thí sinh."""
    band_score_summary: Dict[str, float] = Field(..., description="Tóm tắt điểm số 4 tiêu chí")
    top_strengths: List[str] = Field(..., description="Các điểm sáng nổi bật")
    top_weaknesses: List[str] = Field(..., description="Cần cải thiện chính")
    rewritten_paragraphs: List[Dict[str, str]] = Field(..., description="Các câu/đoạn viết lại đạt Band 8.0+")
    actionable_plan: List[str] = Field(..., description="Đúng 3 hành động cải thiện cụ thể")


# ==========================================
# 2. REDUCER FUNCTIONS FOR FAN-IN SAFETY & BARRIER
# ==========================================

def merge_criterion_scores(
    existing: Dict[str, CriterionScore], 
    new_scores: Dict[str, CriterionScore]
) -> Dict[str, CriterionScore]:
    """
    Custom Reducer hàm gộp dữ liệu kết quả chấm điểm từ 4 Evaluator Nodes (N3a..N3d).
    
    Đảm bảo:
    1. An toàn Race-Condition khi Fan-in: Cập nhật Dict theo Key tiêu chí thay vì ghi đè toàn bộ.
    2. Gom tích lũy điểm từng tiêu chí cho tới khi đạt đủ 4/4 tiêu chí (TA_TR, CC, LR, GRA).
    """
    updated = existing.copy() if existing else {}
    if new_scores:
        for criterion_key, score_data in new_scores.items():
            updated[criterion_key] = score_data
    return updated


def sum_completed_evaluators(existing: int, increment: int) -> int:
    """
    Custom Reducer đếm số lượng Evaluator Agent đã hoàn thành công việc.
    Dùng để theo dõi Rào chắn Fan-in (Barrier) khi đếm chạm mốc 4.
    """
    current = existing if existing is not None else 0
    return current + (increment if increment is not None else 0)


def append_audit_logs(existing: List[str], new_logs: List[str]) -> List[str]:
    """Reducer nối chuỗi Audit Log không bị ghi đè dữ liệu cũ."""
    updated = existing.copy() if existing else []
    if new_logs:
        updated.extend(new_logs)
    return updated


# ==========================================
# 3. HELPER BARRIER CHECKER
# ==========================================

def is_fan_in_ready(state: "IELTSWritingState") -> bool:
    """
    Hàm Helper kiểm tra điều kiện Rào chắn (Barrier Condition):
    Trả về True khi và chỉ khi CẢ 4 Evaluators đều đã chấm xong
    và lưu đủ 4 tiêu chí ['TA_TR', 'CC', 'LR', 'GRA'] vào State.
    """
    required_criteria = {"TA_TR", "CC", "LR", "GRA"}
    current_scores = state.get("criterion_scores", {})
    completed_count = state.get("completed_evaluators_count", 0)
    
    has_all_keys = required_criteria.issubset(set(current_scores.keys()))
    is_count_four = completed_count >= 4
    
    return has_all_keys and is_count_four


# ==========================================
# 4. LANGGRAPH AGENT STATE TYPEDDICT
# ==========================================

class IELTSWritingState(TypedDict):
    """
    Cấu trúc AgentState toàn cục chia sẻ trong LangGraph Pipeline.
    """
    # Submission Base Info
    submission_id: str
    user_id: str
    raw_essay: str
    prompt_text: str
    image_url: Optional[str]
    word_count: int
    under_length: bool
    
    # Input Guard Metrics & Flags
    injection_detected: bool
    injection_severity: Optional[str]
    pii_redacted: bool
    sanitized_essay: str
    paragraphs: List[str]
    
    # Coordinator & Visual Facts
    evaluation_plan: Optional[EvaluationPlan]
    visual_facts: Optional[VisualFacts]
    
    # Parallel Evaluator Results (Fan-in Reducer an toàn chống đè điểm)
    criterion_scores: Annotated[Dict[str, CriterionScore], merge_criterion_scores]
    
    # Barrier Tracker (Đếm số Agent đã xong, Verifier chỉ chạy khi count == 4)
    completed_evaluators_count: Annotated[int, sum_completed_evaluators]
    
    # Verification & Re-eval Loop
    verification_report: Optional[VerificationReport]
    revision_count: int
    
    # Tutor Feedback
    tutor_feedback: Optional[TutorFeedback]
    
    # System Operational Flags & Logs
    status: Literal["PROCESSING", "REJECTED", "COMPLETED", "NEEDS_HUMAN_REVIEW"]
    rejection_reason: Optional[str]
    audit_logs: Annotated[List[str], append_audit_logs]
    trace_id: str