# Saving packages
>>
pip freeze > requirements.txt
pip install -r requirements.txt
>>

# Miniconda:
Anaconda: Sử dụng anaconda để hỗ trợ cài đặt các thư viện cần thiết (đơn giản hóa việc tạo môi trường)
Miniconda: Phiên bản không bao gồm packages.
note: run on (bash).
Anaconda cung cấp đầy đủ thử viện khi cài đặt.
Việc thừa thãi dung lượng sẽ gây ra tình trạng chiếm bộ nhớ
>>
conda -V
conda create -n pydustin
conda activate pydustin
conda deactivate
để Jupyter Notebook truy cập vào môi trường chạy lệnh sau khi đã active môi trường
conda install -c conda-forge nb_conda
>>
- numpy: conda install numpy
- matplotlib: conda install matplotlib
- conda install scikit-learn, pandas, seaborn, pyvi

# Jupyter NoteBook
https://200lab.io/blog/jupyter-notebook-la-gi/
Ju/pyt/er
Julia, Python, R
Là một nền tảng tính toán khoa học mã nguồn mở có thể dùng để chia sẻ các tài liệu có chứa code trực tiếp, phương trình, trực quan hóa dữ liệu và văn bản tường thuật.
- Là một trường điện toán ngôn ngữ hỗ trợ hơn 40 ngôn ngữ lập trình.
- Có thể đưa dữ liệu, hình ảnh, code video trong dùng1 file, giúp cho việc trình bày trở nên dễ dàng Bạn có thể vừa trình chiếu, vừa chạy code trên đó. Cốt lõi của việc này là Markdown
- Một số lợi ích mà juputer mang lại:
  + Phân tích khám phá dữ liệu (Exploratory data analysis):
  Xem kết quả code inline mà không cần phụ thuốc vào các phần khác của code.
  + Mọi ô của code có thể được kiểm tra bất cứ lúc nào.

- Trực quan hóa dữ liệu (Data visualization)
- Tương tác trực tiếp với code (ipywidgets).
- Ngoài ra nó còn cho phép người dùng kiểm soát nguồn dữ liệu đầu vào và phản hồi lại trực tiếp trên trình duyệt.

conda install jupyter
jupyter notebook

# google colab
https://users.soict.hust.edu.vn/khoattq/ml-dm-course/131404-IT3190/H%C6%B0%E1%BB%9Bng%20d%E1%BA%ABn%20c%C3%A0i%20%C4%91%E1%BA%B7t%20m%C3%B4i%20tr%C6%B0%E1%BB%9Dng.pdf

Colaboratory hay còn gọi là google colab: cho phép thực thi python trên nền tảng đám mây
Không yêu cầu cài đặt máy, mọi thứ có thể chạy trên trình duyệt: (CPU, GPU, TPU đều được cung cấp).
Tính năng tương tự như jupyter notebook:
Không cần bận tâm về các cài đặt môi trường hay các gói thư viện mà có thể import trực tiếp để sử dụng chúng
