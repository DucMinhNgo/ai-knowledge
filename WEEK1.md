- Supervisor
- Unsupervisor
  + Thông qua vòng lập để bổ sung.
- Active learning:
  + Phương pháp học chủ động.
  - Một số tiêu chí:
  + Chọn mẫu ít chắc chắn nhất.
  + giảm thiểu tối đa số dự đoán sai.
  + giảm không gian.
- Online learning: cập nhật bộ dữ liệu khi training mô hình.
  + Stochastic gradient descent (SGD): cập nhât ngữ cảnh mới.
- Offline (Batch) learning: thường sử dụng trong mô hình.
- Transfer learning (Các task thường được tiến hành 1 cách tuần tự):
  + Học từ 1 bài toán giải quyết 1 bài toán khác. Trích xuất ra tri thức từ những tác vụ nguồn để giải quyết các tác vụ khác.
  + Sử dụng mô hình kết quả của model khác (tăng tốc độ)
  - Classification:
  - Feature extractor:
  - Weight intialization:
- Yolo AI:
- Object dectection:
- Image style transfer
- Mobile net
- Inception V3

- Reinforcement learning (RL) - Học tăng cường
  + Thử và sai (chọn ra solution tốt nhất), Ví dụ em bé tập đi xe đạp.
  + concept vâcbulary in RL
  + Hành động là tập hợp các thao tác mà agent được phép thực hiện, hành động dẫn đến sự thay đổi của môi trường.
  + observation: 1 phần của trạng thái: chơi cờ (toàn bộ trạng thái), mê cung (1 phần của trạng thái).
  + Reward (điểm thưởng): 
  + AlphaGo to AlphaZero: tích lữ tri thức của con người mà ko cần diễn tả. Học từ ảnh chụp và nước cờ.
    + 2 giai đoạn: supervisor learning:
    + RL: tự chơi với chính mình để học:

- Monte carlo tree search (MCTS):
  + Không đi đến tận cùng: giả lập nước đi.
- A taxonomy of RL algorithms:
- RL toolkits: OpenAL Gym, Open GL:
- RL platforms: Cloud AutoML Vision.
- Muilti-Agent: Hide and Seek.
- Open AI.

- Test ứng dụng (training các test):
  + Xây dự hệ thống chơi tự động.

- Semi-supervisor learning: Có dữ liệu ít, ít mẫu được gắn nhãn và nhiều mẫu không được gán nhãn, tận dụng ưu điểm của cả hai.
  + Xây dựng 1 bộ phân lớp ban đầu, gán nhãn cho những dữ liệu còn lại, kém theo độ đo.
  + Chọn những dữ liệu tin cậy nhất để đưa vầ vập dữ liệu ban đầu. Sau mỗi bước sẽ mở rộng mô hình học. Tận dụng tiệt để dữ liệu gán nhãn. Trong th khó để thu thập dữ liệu.
  + Cần chuyên gia phân biệt các hình ảnh khối u hoặc các tế bào bình thường.
  + Thường được sử dụng trong các bài toán về y tế.
  + Tìm ẩn nguy cơ trong bước chọn mẫu (đưa dữ liệu gán nhãn sai trong mô hình).

- Xây dụng 2 hoặc 3 training: thường không nhiều hơn.
- Self-Supervisor:
  + Dữ liệu tấm ảnh, encode, decode: kì vọng input và output gần giống nhau.
  - Image colorization: tô màu cho anh xám. Không thể đánh giá.
  - Image dencising:

  - generator, discriminator: Tạo ảnh giả và phân biệt ảnh giả và thật.
  - Image inpainting using GAN.
  - 8 đến 16 teslaai chip để traing.
  - Image synthesis using GAN - Tạo ảnh nhân tạo từ ảnh ban đầu - Tạo ảnh anime từ anh chụp.

- Multi-instance learning:
  + Không gán nhãn từng cá nhân mà gán nhãn một nhóm các mẫu. Xét điểm ảnh bt hay bất thường.
  Xét nhóm các điểm ảnh.


=> statistical inference (suy luận thống kê):
  + Induction
  + deduction
  + trainsduction

=> Xây dụng cây quyết định.
=> K-nearest neighbors.

- Multi-tasks learning:
  + Sematic decoder (ngữ nghĩa):
  + Instance decoder:
  + Depth Decoder:

- oracle (human, người gán nhãn) Khó lấy được gán nhãn chính xác đặc biệt là dữ liệu sinh học.
- Image style transfer:
  + Train tiếp từ kết quả train trước đó.
  + Theo phong các hội họa từ những nhà họa sĩ nổi tiếng.
  + Quyết định ảnh kết quả giữ lại bao nhiêu phần trăm nộ dung

- Ensemble learning: Học hết hợp.
  + Kết hợp nhiều mô hình đơn giản nhưng yếu hơn.
  + Kết hợp lời dự đoán cuối cùng.
  + 3 tyles:
    > Bagging: giải thuật trên các tập con khác nhau (theo xác suất).
    > Boosting: 1 tập base learner tuần tự (KNN, decision tree, ).
    > Stracking:

- Một số 
  - Random forest:
    + tạo ra một số bộ phân lớp cơ sở.
    + Chọn ngẫu nhiên 1 thuộc tính.
    + Chọn thuốc tính 1 cách ngẫu nhiên.
    + Tính trung bình trên các kết quả nhận được.
  - Adaboost:
    + Bố trí các bộ phân lớp yếu.
    + có một số mẫu bị dự đoán sai.
  - deepfake detection:
    + Với 1 dữ liệu đầu vào thì sẽ có các bộ phân lớp.
    + Lấy trung bình hoặc lấy đa số chưa chắc là tốt.
  - Anomaly detection video: Xem góc chiếu sáng đúng hay không.
  - Federated learning: (FL)
    + Thể hiện khả năng tìm kiếm:
    - Combine modal is distributed:
      + Train theo từng thiết bị cá nhân, mô hình hông nặng nề.
    - Đạt được mô hình thông minh hơn, tốc độ cao hơn => nhở hơn, gọn gàng hơn so với dữ liệu gốc.
    - Mỗi thiết bị performance khác nhau.

  - TensorFlow

- PySyft
- PyGrid
- Explainable AI (XAI):
  - Giải thích model. Tăng cường tin tưởng của người dùng với sự quyết định.
  - 90% người dùng bị bệnh ung thư => suy ra lời giải thích.
  - Quyết định trong th xe tự vận hành.
  + White box
  + Black box


+ https://phamdinhkhanh.github.io/2020/09/19/MobileNet.html

# ==========================
Phân loại một số phương pháp học:
- Supervised learning:
  + Classification:
  + Regression
- Unsupervised:
  + Clustering (Phân nhóm)
  + Association (Sự kết hợp)
- Semi-Supervised learning
- Reinforcement learning:
