# UIT-SE373 · Documents

Kho tài liệu của đồ án môn **SE373 — AI Agentic**, Trường Đại học Công nghệ Thông tin (UIT).

**Đề tài:** IELTS Learning Agent — hệ thống Multi-Agent chấm và phản hồi bài viết IELTS Writing Task 1 & Task 2, xây dựng trên LangGraph.

## Cấu trúc

```
docs/
├── SRS_IELTS_Agent_SE373.md     # Software Requirements Specification (bản chính)
├── diagrams/                     # Sơ đồ UML xuất ra ảnh
│   ├── use-case-diagram.png
│   └── activity-diagram.png
└── adr/                          # Architecture Decision Records
```

## Tài liệu hiện có

| Tài liệu | Phiên bản | Trạng thái | Mô tả |
|----------|-----------|------------|-------|
| [SRS_IELTS_Agent_SE373.md](docs/SRS_IELTS_Agent_SE373.md) | 1.0 | Chờ review | Đặc tả yêu cầu phần mềm đầy đủ theo template [jam01/SRS-Template](https://github.com/jam01/SRS-Template) (ISO/IEC/IEEE 29148) |

## Quy ước

- Tài liệu viết bằng **Markdown**, thân bài tiếng Việt, heading và thuật ngữ kỹ thuật tiếng Anh.
- Sơ đồ nhúng trực tiếp bằng **Mermaid** để GitHub render được; bản UML chính thức xuất ảnh vào `docs/diagrams/`.
- Mọi thay đổi yêu cầu đi qua Pull Request, theo quy trình ở mục **3.5.10 Change Management** của SRS.
- Commit theo [Conventional Commits](https://www.conventionalcommits.org/): `docs:`, `feat:`, `fix:`, `chore:`.

## Quy trình review

1. Tạo branch `docs/<mô-tả-ngắn>`.
2. Mở Pull Request vào `main`, gán reviewer theo bảng phân công ở đầu SRS.
3. Cần tối thiểu **1 approval** để merge; riêng thay đổi mức *Breaking* cần cả 5 thành viên duyệt.
4. Checklist review của nhóm nằm ở **Appendix G** trong SRS.
