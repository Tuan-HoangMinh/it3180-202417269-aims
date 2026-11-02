# Câu hỏi thảo luận – Lab 02

## 1. Vì sao phải đồng bộ `master` trước khi tạo PR?

Trong lúc một nhánh tính năng đang được phát triển, `master` có thể đã nhận các PR khác và tiến lên trước nhánh đó. Đồng bộ nhánh tính năng với `origin/master` trước khi gửi PR giúp phát hiện sớm xung đột, kiểm tra khả năng tích hợp với mã mới nhất và chạy test trên trạng thái gần với trạng thái sẽ được merge.

Nếu không đồng bộ, xung đột hoặc lỗi tích hợp có thể chỉ xuất hiện khi PR được đưa vào `master`, khiến việc review và merge khó hơn. Trong Lab 02, Dev 2 dùng `git fetch origin`, sau đó `git merge origin/master`, chạy lại `python main.py` rồi mới push và tạo PR.

## 2. Khi nào không được rebase?

Không nên rebase một nhánh đã được chia sẻ và người khác đang dựa vào, đặc biệt là nhánh dùng chung như `master` hoặc nhánh release đã công bố. Rebase tạo lại các commit với SHA mới và viết lại lịch sử của nhánh; người cộng tác có thể bị lệch lịch sử và phải xử lý lại các commit của họ.

Rebase phù hợp hơn với nhánh cá nhân, chưa được chia sẻ hoặc chưa được người khác dựa vào. Với nhánh dùng chung, nên phối hợp theo chính sách của nhóm và ưu tiên cách tích hợp không viết lại lịch sử đã công bố.

## 3. `feature/*` khác `topic/*` ra sao?

- `feature/*` dùng cho việc phát triển một chức năng của phần mềm, ví dụ `feature/cart-print` hoặc `feature/search-by-title`.
- `topic/*` dùng cho một chủ đề/công việc hỗ trợ phát triển, thường là tài liệu hoặc cấu hình, ví dụ `topic/pr-template` và `topic/use-case-diagram`.

Nói ngắn gọn, `feature/*` tập trung vào chức năng sản phẩm; `topic/*` tập trung vào một chủ đề thay đổi cụ thể không nhất thiết là chức năng mới.
