# Câu hỏi thảo luận – Lab 04

## 1. Vì sao `release/*` không merge vào `master`?

Trong quy trình của học phần, `master` tiếp tục phát triển và nhận tính năng mới, còn `release/*` lưu một dòng phiên bản đã phát hành để bảo trì. Sau khi tạo release branch và tag, `master` có thể đi trước release branch. Merge toàn bộ release branch ngược vào `master` không phải luồng tích hợp được bài thực hành chọn; thay vào đó, khi cần lan truyền một bản sửa giữa các dòng phiên bản, Lab 05 yêu cầu chọn đúng commit bằng `cherry-pick -x`.

Cách làm này giúp kiểm soát chính xác thay đổi nào được đưa sang từng dòng phiên bản, tránh vô tình đưa các thay đổi riêng của nhánh bảo trì vào dòng phát triển chính. Tag như `v1.0.0` đánh dấu một commit cụ thể và không di chuyển; nhánh `release/lab04` là dòng bảo trì có thể tiếp tục nhận bản sửa theo quy trình.

## 2. So sánh với GitFlow

Theo quy trình trong bài thực hành, `master` là dòng phát triển tiếp tục tiến lên, còn `release/labXX` là nhánh lưu baseline của từng bài phát hành. Khi một lỗi ảnh hưởng nhiều phiên bản, bài thực hành dùng hotfix từ nhánh release và chọn lọc commit để đưa sang các dòng khác.

Trong mô hình GitFlow phổ biến, thường có nhánh phát triển tích hợp `develop`, các nhánh `feature/*`, nhánh `release/*`, nhánh `hotfix/*` và nhánh `main`/`master` dành cho phiên bản phát hành. Một nhánh release thường được tích hợp trở lại các nhánh phát triển theo quy tắc của GitFlow. Như vậy, cả hai đều dùng nhánh riêng để quản lý tính năng và phát hành, nhưng cách tổ chức vai trò của nhánh chính và cách đồng bộ giữa release với dòng phát triển khác nhau.

*Ghi chú: PDF yêu cầu so sánh với GitFlow nhưng không trình bày chi tiết sơ đồ GitFlow; phần mô tả GitFlow ở trên là kiến thức khái quát để làm rõ phép so sánh.*

## 3. Vì sao lên `1.0.0` mà không phải `0.4.0`?

Theo tài liệu, các phiên bản `0.1.0` đến `0.3.0` đại diện cho giai đoạn đầu, chưa ổn định. Lab 04 đánh dấu baseline phát hành chính thức đầu tiên, nên chuyển sang `1.0.0` thay vì tiếp tục `0.4.0`.

Theo Semantic Versioning, `0.y.z` biểu thị giai đoạn phát triển ban đầu; `1.0.0` thể hiện mốc phát hành ổn định đầu tiên. Vì vậy, đây là thay đổi về giai đoạn phát hành, không chỉ là tăng số phiên bản MINOR.
