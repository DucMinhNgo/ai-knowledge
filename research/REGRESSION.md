Regression:
# Linear Regression (Hồi quy tuyến tính):
1. Giới thiệu
  (x1, x2, x3) được thống kê từ dữ liệu của 1000 căn nhà) vector hàng chửa thông tin - input.
  y = f(x) (scalar) - output
  - Phân tích bài toán:
  x1, x2: diện tích căn nhà lớn, số phòng ngủ càng nhiều thì giá tiền càng cao.
  x3: càng xa thành phố thì giá tiền càng giảm.
  với hàm 3 chiều thì
  f(x) = x1.w1 + x2.w2 + x3.w3 + w0 (bias: dự kiến) tìm các con số w0, w1, w2, w3 nên bài toán được gọi là linear regression.
  y: giá trị thực của (outcome)
  y^: giá trị của mô hình dự đoán được.
  1. y và y^ khác nhau do có sai số mô hình (mục đích mong muốn cho sai số xảy ra là nhỏ nhất).
  2. linear hiểu theo 1 cách đơn giản là làm thẳng, làm phẳng dữ liệu
  Trong không gian nhiều chiều thì khái niệm mặt phẳng không còn phù hợp nữa (hyperplane). Các hàm số tuyến tính là các hàm đơn giản vị chúng thuận lợi cho việc hình dung thuật toán.
  (x bar).
  note: Bình phương có đạo hàm tại mọi nơi trong khi trị tuyệt đối thì không.
  Trị tuyệt đối không có giá trị tại 0.
  Nếu ma trận vuống và khả nghịch  (non-singular hay invertible)
2. Phân tích toán học
  2.1. dạng của linear regression:
  2.2. Sai số dự đoán
  2.3. Hàm mất mát (loss function): tìm giá trị hàm w sao cho giá trị của loss function càng nhỏ.
  giá trị của w làm cho hàm mất mát đạt giá trị nhỏ nhất được gọi là điểm tối ưu (optimal point).
  2.4. Nghiệm của bà toán linear regression
3. Một số ví dụ trên python:
  3.1. Dự đoán cân nặng từ chiều cao
  Từ hình ta thấy dữ liệu sẵp xếp gần như 1 đường thẳng nên có khả năng cho ra được kết quả tốt.
   (cân nặng) = w_1*(chiều cao) + w_0
Hồi quy tuyến tính bậc 2
- Hạn chế: Hồi quy tuyến tính rất nh`ạy cảm với nhiễu
- Khi làm việc với hồi quy tuyến tính các outlier cần được loại bỏ. Bước này gọi là tiền xử lý pre-processing.
- Không biểu diễn được các mô hình phức tạp. Phương pháp này có thể s dụng với mối quan hệ outcome, input không nhất thiết là tuyến tính.
4. Các phương pháp tối ưu:
- Là mô hình đơn giản, là lời giải cho phương trình đạo hàm = 0, trong hầu hết các trường hợp chúng ta không thể giải được cá phương trình có đạo hàm bành 0.
- Còn tính được hàm là còn hy vọng.
# Deep:
- Linear Regression
- Gradient Decent (tìm giá trị nhỏ nhất của hàm số f(x) dựa trên đạo hàm):
đạo hàm: đạo là con đường, hàm là số, đạo hàm hiển thị sự biến đổi của hàm số hay còn có các gọi thân thương hơn là độ dóc của đồ thị.
Step 1: khỏi tạo giá trị x = x0 tùy ý.
Step 2: x = x - learning_rate*f(x)' (learning_rate là hằng số không âm ví dự 0.001).
Step 3: Tính là f(x) nếu f(x) đủ nhở thì dừng lại, ngược lại tiếp tực bước 2.
  + Training: tìm đường thảng model gần các điểm trên nhất (máy cần dùng thuật toán gradient decent để tìm model)
  + Nhận xét: 
    Thuật toán hoạt động rất tốt trong trường hợp không thể tìm được giá trị nhỏ nhất bằng đại số tuyến tính.
    Việc quan trọng nhất của thuật toán là tìm đạo hàm của hàm số theo từng biến sau đó lặp lai bước 2.
- Loss Function (J): Làm được sử dụng để đánh giá xem giá trị kết quả có đúng hay không.
  + J càng nhỏ thì đường thẳng càng gần các điểm dữ liệu, J = 0 dường thẳng đi qua tất các các điểm dữ liệu.




# Logistic Regression:
# Stepwise Regression: