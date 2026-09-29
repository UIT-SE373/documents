# UIT-SE373 · Documents

Kho tài liệu của đồ án môn **SE373 — AI Agentic**, Trường Đại học Công nghệ Thông tin (UIT).

**Đề tài:** IELTS Writing Agent — hệ thống Multi-Agent chuyên biệt cho kỹ năng viết (Writing skill only), chấm và phản hồi bài viết IELTS Writing Task 1 & Task 2, xây dựng trên LangGraph.

## Cấu trúc

```
documents/
├── SRS/
│   ├── SRS_IELTS_Writing_Agent_SE373_v2.md  # Software Requirements Specification v2.1 (bản chính)
│   └── SRS_IELTS_Writing_Agent_SE373_v1.md  # Bản v1 lưu trữ
├── diagrams/                                 # Sơ đồ UML xuất ra ảnh
└── adr/                                      # Architecture Decision Records
```

## Tài liệu hiện có

| Tài liệu | Phiên bản | Trạng thái | Mô tả |
|----------|-----------|------------|-------|
| [SRS_IELTS_Writing_Agent_SE373_v2.md](SRS/SRS_IELTS_Writing_Agent_SE373_v2.md) | 2.0 | Đã hoàn thiện | Đặc tả yêu cầu phần mềm đầy đủ theo template [jam01/SRS-Template](https://github.com/jam01/SRS-Template) (ISO/IEC/IEEE 29148), chuyên biệt kỹ năng viết Task 1 & Task 2 |

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
