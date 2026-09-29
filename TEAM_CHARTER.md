# TEAM CHARTER — IELTS LEARNING AGENT PROJECT
**Automated Assessment and Feedback System for IELTS Writing**  
*Course SE373 — AI Agentic | University of Information Technology (UIT - VNU-HCM) | Team Charter*

---

## 1. Purpose & Outcomes (Mục đích & Kết quả đầu ra)

* **Our Purpose:** Build an automated assessment and coaching platform that helps IELTS test-takers practice and improve their Writing skills (Task 1 & Task 2). The system provides fast, objective scoring and personalized, actionable feedback aligned with official Cambridge Band Descriptors (*tiêu chí chấm thi chuẩn*).
* **Target Users:** IELTS learners, writing instructors, and test evaluators.
* **Key Measurable Outcomes:**
  * **Deliverable:** A responsive web application delivering comprehensive 4-criteria feedback (Task Achievement/Response, Coherence & Cohesion, Lexical Resource, Grammatical Range & Accuracy) in under 30 seconds.
  * **Evaluation Quality:** High scoring consistency matching human examiners (Mean Absolute Error $\le 0.5$ band) with transparent, citation-backed feedback (*phản hồi có dẫn chứng cụ thể*).
  * **Academic Goal:** on-time delivery with high mark assessment.

---

## 2. Values & Behaviors (Giá trị cốt lõi & Quy tắc hành vi)

### Encouraged Behaviors (Khuyến khích)
* **Ownership & Accountability (*Tinh thần trách nhiệm & Chủ quyền công việc*):** Take full end-to-end ownership of assigned agent nodes, schemas, or UI modules. If encountering technical roadblocks or prompt regressions, flag a **blocker** (*vấn đề gây nghẽn tiến độ*) immediately in team channels instead of waiting for meetings.
* **Proactive Transparency (*Minh bạch chủ động*):** Push small, frequent commits using Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`); document architectural decisions and trade-offs in ADRs (Architecture Decision Records); keep task boards up to date daily.
* **Token & Cost Prudence (*Ý thức kiểm soát chi phí token*):** Run local mocks or lightweight models (e.g., Claude Haiku) during local debugging; enforce strict recursion limits (*giới hạn đệ quy*) and checkpointer safety in LangGraph to prevent infinite LLM calling loops and runaway API bills.
* **Constructive Critique (*Góp ý mang tính xây dựng*):** Challenge prompts, code, and test cases objectively, never attacking the person. When pointing out flaws, always propose a concrete, workable alternative.
* **Empathy & Mutual Support (*Thấu hiểu & Hỗ trợ đồng đội*):** Step up to help teammates when workloads peak, model outputs hallucinate unexpectedly, or cross-functional integration issues occur.

### Unacceptable Behaviors (Không chấp nhận)
* **Ghosting (*Mất tích không báo trước*):** Disappearing, going silent on chat, or missing milestone deadlines without at least 24 hours prior notice.
* **Direct Commits to Main (*Commit trực tiếp vào nhánh chính*):** Merging code without an approved Pull Request (PR) and passing automated linting and verification tests.
* **Unbounded API Spends (*Tiêu xài API không kiểm soát*):** Triggering unmonitored batch LLM evaluation runs on expensive models without dry-runs, caching, or rate limits.
* **Passive Withholding (*Thụ động che giấu vấn đề*):** Concealing prompt degradations, failing gold set benchmarks, or schedule delays until sprint demo or submission deadlines.
* **Finger-Pointing (*Đổ lỗi cá nhân*):** Blaming individuals during failures or model evaluation drops instead of conducting blameless post-mortems and refining validation guardrails.

---

## 3. Roles & Decision Rights (Vai trò & Quyền quyết định)

### Team Roles & Responsibilities (5-Member Team)
| Role | Primary Responsibilities |
| :--- | :--- |
| **Team Leader / Product Owner (PO)** | Project backlog and milestone roadmap; course lecturer liaison (*đầu mối liên lạc giảng viên*); task allocation and sprint tracking; scope enforcement; final sign-off on breaking changes and acceptance criteria. |
| **AI / ML & Multi-Agent Architect** | LangGraph graph topology (Coordinator, Evaluator fan-out, Verifier, Tutor Agent); `AgentState` schema design; prompt engineering and structured Pydantic outputs; LLM provider integration and fallback strategies. |
| **Knowledge & Evaluation Engineer (RAG / Data)** | Grounding pipeline: Academic Word List (AWL) lookup tool, Vector DB / RAG setup with Band 8.0+ essays, Cambridge Band Descriptors index; grammar checking tool integration; golden dataset curation and benchmark harness (MAE tracking). |
| **Backend & DevOps Engineer** | FastAPI web services; Server-Sent Events (SSE) streaming; PostgreSQL database and LangGraph checkpointer persistence; Docker Compose orchestration; rate limiting and token consumption monitoring; CI/CD pipeline automation. |
| **Frontend & QA Engineer** | Responsive web user interface (essay submission, real-time SSE progress indicators, character-indexed error highlighting, 4-criteria radar charts, Band 8.0+ rewrites); end-to-end integration testing; test case validation against user personas. |

### Decision Rights Matrix
* **Autonomous (*Quyền tự chủ*):** Each member has full autonomy over internal implementation details within their domain (e.g., AI/ML on prompt phrasing and system prompts, Backend on ORM queries and connection pools, Frontend on UI component styling, Data Engineer on vector indexing parameters).

---

## 4. Communication Protocols (Quy chuẩn giao tiếp)

| Purpose | Primary Channel | Rule / Expected Response Time |
| :--- | :--- | :--- |
| **Quick Chat & Daily Sync** | Zalo | Respond within 3–4 business hours. Use role tags (e.g., `@backend`, `@ai-engineer`) for urgent questions. |
| **Urgent & Blocker Alerts** | Direct Phone Call / Urgent Ping | Immediate response required (< 1 hour) for critical build breaks, runaway LLM API spending, or urgent submission deadlines. |
| **Task & Sprint Tracking** | GitHub Projects (Kanban) | Every work item must have a ticket. Card states: `Backlog` ➔ `Ready` ➔ `In Progress` ➔ `In Review` ➔ `Done`. Update cards before each sync. |
| **Code Review & Issue Tracking** | GitHub PRs & GitHub Issues | Minimum 1 approving peer review required before merging. Breaking changes require full team consensus. No self-merging. Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/). |
| **Official Documentation** | `/documents` repository | Single source of truth (*nguồn thông tin chuẩn duy nhất*) for SRS, Architecture Decision Records (ADRs), Team Charter, and UML diagrams. |

---

## 5. Work Cadence & Rhythm (Nhịp độ làm việc)

```
[Sunday 20:00] ──────────► [Fri 20:50] ──────────► [Saturday 22:00]
Sprint Planning           Async Standup           Sprint retrospective       
& Backlog Allocation      (Chat Channel)                       
```

---

## 6. Conflict Resolution (Quy trình xử lý xung đột)

We resolve technical and procedural disagreements through a structured, 4-step escalation hierarchy:

```
[Level 1: Direct 1-on-1 Dialogue] 
       │ (Unresolved within 24h)
       ▼
[Level 2: Team Debate with Objective Weighted Matrix] 
       │ (Deadlock / Split vote)
       ▼
[Level 3: Team Leader Tie-Breaker Decision] 
       │ (Irreconcilable crisis / Course risk)
       ▼
[Level 4: Course Lecturer & Mentor Consultation]
```

---

## 7. Learning & Continuous Improvement (Học hỏi & Cải tiến liên tục)

* **Blameless Post-Mortems (*Phân tích nguyên nhân không quy trách nhiệm cá nhân*):**
  * When an evaluation regression occurs (e.g., MAE drops, token consumption spikes, or an agent enters an infinite loop), hold a 15-minute root cause analysis.
  * Focus strictly on *how our guardrails, schemas, or tests missed the issue*, never on *who wrote the prompt or code*.
* **Actionable Retrospective Commitments (*Cam kết cải tiến sau mỗi chu kỳ*):**
  * Limit retrospective improvements to **maximum 2 actionable commitments** per sprint (e.g., "Add automated Pydantic schema validation to PR checks" or "Implement local mock LLM provider for unit tests").
  * Review progress on previous action items at the start of every sprint planning meeting.


