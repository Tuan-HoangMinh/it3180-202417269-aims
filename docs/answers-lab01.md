# Câu hỏi thảo luận – Lab 01

## 1. Vì sao dùng `git mv`?

`git mv` dùng để di chuyển hoặc đổi tên tệp, đồng thời đưa thao tác đó vào staging area. Trong Lab 01, lệnh này giúp chuyển `dvd.py` và `cart.py` vào thư mục `aims/` mà không phải tự thực hiện riêng thao tác xóa tệp cũ, thêm tệp mới và stage cả hai phía.

Git không lưu một loại đối tượng “rename” riêng trong commit; khi xem lịch sử, Git nhận diện việc đổi tên dựa trên mức độ giống nhau giữa nội dung tệp trước và sau. Tuy vậy, `git mv` vẫn tiện và giúp tránh quên stage thao tác di chuyển. Sau khi di chuyển, cần sửa các import trong `main.py` cho phù hợp với vị trí mới.

## 2. `release/lab01` có phải baseline không?

Có. `release/lab01` là baseline (mốc cấu hình) ghi nhận trạng thái dự án sau khi hoàn thành Lab 01. Nhánh được tạo từ `master` sau khi PR refactor đã merge, vì vậy tại thời điểm tạo, hai nhánh trỏ tới cùng một commit. Có thể kiểm tra bằng:

```bash
git rev-parse origin/master origin/release/lab01
```

Hai mã hash giống nhau xác nhận hai nhánh có cùng trạng thái tại thời điểm đó. Sau này `master` tiếp tục nhận thay đổi ở các Lab tiếp theo, còn `release/lab01` giữ mốc của Lab 01; do đó nhánh release giúp xác định và tái tạo chính xác trạng thái đã nộp.

## 3. Vì sao không commit thẳng vào `master` dù làm một mình?

Vì bài thực hành yêu cầu tuân thủ quy trình thay đổi có kiểm soát: tạo nhánh riêng, commit trên nhánh đó, mở Pull Request rồi mới merge vào `master`. PR tạo ra nơi ghi nhận mục đích, nội dung, cách kiểm thử và lịch sử thay đổi; đồng thời cho phép review và kiểm tra trước khi tích hợp.

Làm một mình không làm mất lợi ích của quy trình này. Theo tài liệu, có thể đặt số approval bằng `0` khi làm cá nhân, nhưng vẫn phải đi qua PR. Như vậy, `master` luôn là nhánh chính được bảo vệ và lịch sử thay đổi vẫn có thể truy vết.
