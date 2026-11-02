# Câu hỏi thảo luận – Lab 03

## 1. Merge base là gì?

Merge base là commit tổ tiên chung gần nhất mà Git dùng làm điểm xuất phát khi thực hiện phép merge ba chiều (three-way merge) giữa hai nhánh. Git so sánh thay đổi của mỗi nhánh kể từ điểm chung đó để xác định phần nào có thể tự động kết hợp và phần nào có thể xung đột.

Trong tình huống Lab 03, hai nhánh cùng bắt đầu từ một trạng thái chung rồi sửa cùng một dòng trong `aims/cart.py`. Khi một nhánh đã được merge vào `master`, nhánh còn lại vẫn dựa trên lịch sử cũ. Khi đồng bộ, Git cần so sánh thay đổi của nhánh hiện tại với thay đổi đã có trên `master` kể từ merge base; nếu hai bên sửa cùng vùng nội dung theo cách không thể tự kết hợp, Git báo merge conflict.

## 2. Vì sao `master` và `release/*` phải dùng `revert`?

`master` và các nhánh `release/*` là những nhánh dùng chung, có thể đã được push và được người khác dựa vào. Dùng `reset` để bỏ một commit trên các nhánh này sẽ di chuyển con trỏ nhánh và có thể viết lại lịch sử đã chia sẻ, gây lệch lịch sử giữa các bản clone.

`git revert` tạo một commit mới đảo ngược thay đổi của commit cũ nhưng vẫn giữ commit cũ trong lịch sử. Vì vậy, lịch sử chung không bị viết lại và mọi người có thể truy vết được cả thay đổi ban đầu lẫn thao tác hoàn tác. `reset` phù hợp hơn với commit chưa push hoặc nhánh cá nhân/nháp; `revert` phù hợp với `master` và `release/*`.
