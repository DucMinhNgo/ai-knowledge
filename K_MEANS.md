Trong thuật toán K-means chúng ta không biết nhãn của dữ liệu, mục đích là để phân cụm (cluster).
- Dữ liêu trong cùng 1 cụm có tính chất giống nhau
- Một cty muốn tạo ra những chính sách ưu đãi cho mỗi khách hàng khác nhau dựa trên sự tương tác giữa mỗi khác hàng với cty đó.
- đường phân ranh giữa các điểm là các đường trung trực.
- Trong không gian hai chiều gọi là lãnh hải, trong không gian 3 chiều gọi là lãnh không. Trong không gian đa chiều ta gọi là siêu đa diện (hyperpolygon)

- Mục đích của bài toán:
  + Từ dữ liệu đầu vào và số lượng nhóm chúng ta muốn tìm. Chỉ ra center của nhóm là phân các điểm dữ liệu vào nhóm tương ứng. Giả sử thêm rằng mồi điểm dữ liệu chỉ thuộc đúng 1 nhóm
 - Luật:
  + Số vô hướng được biểu diễn bằng các chứ cái không in đậm, có thể viết hoa
  + Các vector được biểu diễn bằng các chứ in đậm.
  + Ma Trận được biểu diễn bằng chữ in đậm viết hoa.

- Hàm mất mát và bài toán tối ưu:
min: là giá trị nhỏ nhất của hàm số => arg min là giá trị làm cho hàm số nhở nhất.
(Trong mọi bài toán ta thường quan tâm đến min hơn là min)
- Điểm cực đại cực tiểu chưa chắc đã làm cho hàm số mang giá trị nhỏ nhất.

Trước mắt chúng ta lấy mẫu phân phối có kì vọng là center của cluster đó là ma trận hiệp phương sai (convarian matrix) là ma trận đơn.
- K-means: lưu ý tính công thức của các điểm trong không gian (Euclid).
- K-means: Phân hoạch theo tâm A, B cho trước hoặc tự chọn điểm để phân hoạch. Thường thì ta sẽ chọn điểm đầu và điểm cuối để phân hoạch.
A (1, 1)
B (2, 1)
C (4, 3)
D (5, 4)
Phân hoạch những đối tượng thành 2 nhóm.
Chọn 2 tâm (1, 1), (5, 4)
Tính khoảng các giữa các điểm cho tới tâm.