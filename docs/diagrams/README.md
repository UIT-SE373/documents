# Sơ đồ UML

Thư mục này chứa bản vẽ UML chính thức xuất ra ảnh. Bản Mermaid nhúng trong SRS là **đặc tả nguồn** — bản vẽ ở đây phải khớp nội dung với nó.

## Cần vẽ

| Tệp | Loại sơ đồ | Nguồn nội dung trong SRS | Người phụ trách |
|-----|-----------|--------------------------|-----------------|
| `use-case-diagram.png` | UML Use Case Diagram | Mục [3.2.1](../SRS_IELTS_Agent_SE373.md#321-use-case-diagram) và bảng [3.2.2](../SRS_IELTS_Agent_SE373.md#322-use-case-specifications) | Business Analyst |
| `activity-diagram.png` | UML Activity Diagram | Mục [3.2.3](../SRS_IELTS_Agent_SE373.md#323-activity-diagram--luồng-dữ-liệu-chính) | Business Analyst |
| `architecture-diagram.png` | Component / Deployment Diagram | Mục [2.1](../SRS_IELTS_Agent_SE373.md#21-product-perspective) | AI/ML Engineer |

## Yêu cầu với Use Case Diagram

Phải thể hiện đầy đủ:

- **4 actor người**: Learner, Examiner, Administrator — và các **system actor**: LLM Provider, Vector Database, Grammar Tool.
- **14 use case** UC-01 → UC-14, đúng tên như bảng 3.2.2.
- Quan hệ `«include»`: UC-01 → UC-11, UC-01 → UC-02, UC-02 → UC-12, UC-02 → UC-14.
- Quan hệ `«extend»`: UC-13 extend UC-02 (chỉ khi Task 1 Academic có ảnh), UC-06 extend UC-04.
- Đường biên hệ thống (system boundary) bao quanh toàn bộ use case.

## Công cụ đề xuất

- **StarUML** hoặc **draw.io / diagrams.net** — xuất PNG ở độ phân giải ≥ 1600px chiều rộng.
- Giữ lại file nguồn (`.mdj`, `.drawio`) cạnh file ảnh để sửa được về sau.
