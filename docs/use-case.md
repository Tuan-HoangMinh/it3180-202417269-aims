\# AIMS-mini – Use Case Diagram



\## 1. Actors



\- \*\*Customer:\*\* Người sử dụng hệ thống để xem và lựa chọn DVD.

\- \*\*Store System:\*\* Hệ thống quản lý các thao tác với DVD và giỏ hàng.



\## 2. Main Use Cases



\- Add DVD to Cart: Thêm DVD vào giỏ hàng.

\- Remove DVD from Cart: Xóa DVD khỏi giỏ hàng.

\- View Cart: Hiển thị nội dung giỏ hàng.

\- Calculate Total Cost: Tính tổng chi phí giỏ hàng.

\- Search DVD by Title: Tìm kiếm DVD theo tên.



\## 3. Use Case Relationships



\- Customer có thể thêm DVD vào giỏ hàng.

\- Customer có thể xóa DVD khỏi giỏ hàng.

\- Customer có thể xem nội dung giỏ hàng.

\- Khi xem giỏ hàng, hệ thống hiển thị danh sách DVD và tổng chi phí.

\- Customer có thể tìm kiếm DVD theo tên.



\## 4. Use Case Diagram



```mermaid

flowchart LR

&#x20;   Customer\[Customer]

&#x20;   System((AIMS-mini System))



&#x20;   Customer --> Add\[Add DVD to Cart]

&#x20;   Customer --> Remove\[Remove DVD from Cart]

&#x20;   Customer --> View\[View Cart]

&#x20;   Customer --> Search\[Search DVD by Title]



&#x20;   Add --- System

&#x20;   Remove --- System

&#x20;   View --- System

&#x20;   Search --- System

&#x20;   View --> Total\[Calculate Total Cost]

```

