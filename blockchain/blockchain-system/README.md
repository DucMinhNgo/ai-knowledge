go mod init blockchain-system

# Build block chain on go

https://www.youtube.com/watch?v=mYlHT9bB6OE&list=PLpP5MQvVi4PGmNYGEsShrlvuE2B33xV1L

> go mod init [blockchain-system]

- Smart contract: Mục đích của điều này là tạo ra các điều khoản mà không cần sự
  can thiệp của bên thứ 3. Tự động thực hiện và ghi lại các hành động pháp lý
  của các bên giúp cho việc truy dấu dễ dàng hơn bao gồm 4 yếu tố:
  - Chủ thể hợp đồng
  - Điều khoản hợp đồng
  - Chữ ký số
  - Nền tảng phân quyền Solidity, Web Assembly hay Michelson
    https://viblo.asia/p/tuong-tac-voi-smartcontract-tren-blockchain-voi-go-phan-1-1Je5EjD4KnL

- Proof of work and how to implement consensus in a golang blockchain: Là tiêu
  chí để ngăn chặn chi tiêu kép. Hầu hết các "tiền mã hóa" sử dụng như thuật
  toán đồng thuận. Được dùng để bảo mật cho sổ cái của tiền mã hóa.
  - Dữ liệu biến thiên này được đặt tên là một "nonce"
  - Kết quả là nếu muốn tạo một khối chính là đang chơi trò chơi đoán (lấy thông
    tin tất cả các giao dịch muốn thêm và một số dữ liệu quan trọng khác sau đó
    băm tất cả lại với nhau. Nhưng vị dữ liệu ko thay đổi nên bạn cần thêm 1
    phần tử thông tin biến thiên nếu khống bạn sẽ luôn thu về hash giống như ban
    đầu). Đó là còn số mà bạn sẽ thay đổi sau mỗi lần thử vì vậy bạn sẽ nhận
    được 1 hash khác nhau mỗi lần là đó gọi là đào.
  - Trong vấn đề này, Proof of Work thể hiện ưu điểm: Nó khiến cho việc gian lận
    trở nên tốn kém, nhưng lại có lợi khi hành động một cách trung thực

# Tóm lại, đào là quá trình thu thập dữ liệu blockchain và băm nó cùng với một nonce cho đến khi bạn tìm thấy một hash cụ thể. Nếu bạn tìm thấy một hash thỏa mãn các điều kiện được đặt ra bởi giao thức, bạn có quyền phát khối mới lên mạng. Tại thời điểm này, những người tham gia khác của mạng sẽ cập nhật blockchain của họ để bao gồm khối mới

    + Việc cố gắng đoán số lượng hash có thể sẽ rất tốn kém, bạn đang tiêu tốn chu trình tính toán và điện năng. Nhưng giao thức sẽ thưởng cho bạn bằng tiền mã hóa nếu bạn tìm ra một hash hợp lệ

    + Đào là tốn kém.
    + Bạn sẽ được thưởng nếu tạo ra được một khối hợp lệ.
    + Biết một đầu vào, người dùng có thể dễ dàng kiểm tra hash của mình - những người dùng không tham gia đào có thể xác minh rằng một khối là hợp lệ hay không mà không tiêu tốn nhiều sức mạnh tính toán.

- Chi tiêu kép: xảy ra khi cùng một khoản tiền nhưng được chi tiêu nhiều lần

* Ví dụ: hôm nay khi bạn trả tiền cho 1 ly ca phê (trả tiền mặt cho nhân viên
  thu ngân, người có thể khóa nó vào trong sổ cái) bạn không thể đến quán cà phê
  bên kia đường và trả tiền cho 1 ly cà phê khác với cùng hóa đơn. Vì tiền ký
  thuật số chi

- Chi tiêu 2 lần là gì: là một vấn đề có thể xảy ra trong hệ thống kỹ thuật số,
  trong đó cùng 1 tài khoản được ghi cho hai người nhận cùng lúc. Nếu không có
  bất kỳ biện pháp đối phó thích hợp nào, một giao thức không thể giải quyết đc
  vấn đề cơ bản sẽ bị hủy hoại - người dùng ko có cách nào xác minh đc số tiền
  họ nhận đc chưa đc xác minh ở nơi khác
  https://academy.binance.com/vi/articles/double-spending-explained
  - Làm thế nào để ngăn chặn tiêu chí 2 lần:
    - Cách tiếp cận tập trung: Bao gồm 1 giám sát viên kiểm soát hệ thống và
      kiểm soát việc phát hành, phân phối các đồng tiền (chữ ký mù - mật mã học
      David Chaum)
    - Cách tiếp cận phi tập trung: đảm bảo rằng các tài khoản ko thể đc chi tiêu
      2 lần trong 1 hệ sinh thái, không có người giám sát sẽ khó khăn hơn, những
      người tham gia sẽ có quyền lực ngang nhau và phải phối hợp với một bộ
      nguyên tắc giúp ngắn chặn gian lận và khuyến khích tất cả người dùng hành
      động trung thực. Blockchain thực tế là là một cơ sở dữ liệu với thuộc tính
      độc đáo. Những người tham gia vào mạng đc gọi là nút chạy phần mềm chuyên
      dụng cho phép họ đồng bộ hóa bản sao của họ với các đồng đẳng (peer). Kết
      quả toàn bộ mạng có thể kiểm tra lịch sử các giao dịch từ khối nguyên thủy
      (genesis):
      - Khi người dùng nó không đc thêm ngay vào blockchain. Trc tên nó phải
        được đưa vào các khối thông qua hoạt động khai thác. Như vậy người nhận
        chỉ nên xem giao dịch là hợp lệ sau khi khối của nó được thêm vào khối.
        Mặt khác người nhận có thể bị mất tiền vì người gửi có thể chi tiêu cùng
        một số tiền ở nơi khác.
- Có 3 phương thức phổ biến cho việc chi tiêu 2 lần:
  - Tấn công 51%: khi 1 thực thể học tổ chức kiểm soát hơn 50%. Điều này cho
    phép họ loại trừ và sửa đổi các loại giao dịch
  - Tấn công cuộc đua
  - Tấn công Finney

# https://academy.binance.com/vi/articles/what-is-public-key-cryptography

# Mã khóa công khai là gì
