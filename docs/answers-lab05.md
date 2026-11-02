# Câu hỏi thảo luận – Lab 05

## 1. Ưu, nhược điểm của upstream first so với release first?

**Upstream first** là sửa lỗi trước trên dòng phát triển chính (ví dụ `master`), sau đó cherry-pick bản sửa sang các nhánh release bị ảnh hưởng.

Ưu điểm:
- Dòng phát triển chính nhận bản sửa trước, giảm nguy cơ lỗi đã được xử lý ở release nhưng vẫn tồn tại trong mã nguồn phát triển.
- Bản sửa được xem như thay đổi gốc ở upstream; các release nhận lại thay đổi có chọn lọc bằng cherry-pick.
- Phù hợp khi sản phẩm có dòng phát triển chính tiến liên tục và các nhánh release là những dòng cần bảo trì riêng.

Nhược điểm:
- Bản sửa có thể khó cherry-pick vào release cũ nếu mã nguồn đã khác nhiều.
- Nếu bản sửa cần phát hành khẩn cấp cho phiên bản đang chạy, phải chờ xử lý ở upstream rồi mới lan truyền, trừ khi quy trình có cách rút ngắn bước này.

**Release first** là sửa lỗi trước trên nhánh release đang bị ảnh hưởng, sau đó lan truyền bản sửa sang các dòng khác. Đây là luồng của bài thực hành: hotfix bắt đầu từ `release/lab04`, rồi dùng `cherry-pick -x` đưa commit sửa lỗi sang `master` và `release/lab05`.

Ưu điểm của release first là sửa trực tiếp trên baseline đang bị lỗi và có thể phát hành bản vá cho phiên bản đó sớm. Nhược điểm là phải kiểm toán việc lan truyền sang mọi dòng phiên bản khác; nếu quên một nhánh, lỗi vẫn còn ở nhánh đó.

## 2. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?

Lệnh trong Phần F dùng để kiểm tra hai lần cherry-pick là:

```bash
git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"
```

Theo luồng đúng, kết quả cần có hai commit cherry-pick: một trên `master` và một trên `release/lab05`. Nếu chỉ có một commit mang dòng `cherry picked from commit <FIX_SHA>`, cần kiểm tra nhánh còn thiếu.

Có thể kiểm tra bổ sung trực tiếp bằng cách chạy vòng lặp kiểm tra hành vi trên `v1.0.1`, `v1.1.0` và `master` như hướng dẫn của Lab 05. Cả ba phải tìm được `The Lion King` khi từ khóa là `lion`. Nếu `release/lab05` chưa nhận bản sửa, kiểm tra trên `v1.1.0` sẽ không cho kết quả mong đợi.

Lệnh `git cherry -v` trong tài liệu minh họa việc so sánh thay đổi tương đương giữa `master` và `release/lab04`; khi kiểm tra một cặp nhánh khác, cần thay ref cho đúng cặp cần kiểm toán. Không nên chỉ dựa vào `git tag --contains <FIX_SHA>`, vì lệnh đó xác nhận tag chứa commit gốc, không tự chứng minh rằng cả hai bản cherry-pick đã có mặt.
