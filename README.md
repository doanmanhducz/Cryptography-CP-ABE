# Cryptography-CP-ABE
## Giới thiệu: ENCRYPTION, ACCESS CONTROL AND QUERY ON CLOUD DATABASE IN REAL ESTATE TRANSACTIONS 

### Ngữ cảnh vấn đề : 
* Các công ty bất động sản cần lưu trữ và quản lý tài liệu liên quan đến giao dịch, hợp đồng và hồ sơ pháp lý.
* Dữ liệu được lưu trữ trên Cloud và cần đảm bảo bảo mật khi truy cập từ nhiều bên (nhân viên công ty, ngân hàng, cơ quan hành chính công, v.v.).
* Vấn đề đặt ra là làm sao kiểm soát quyền truy cập để chỉ những người có thẩm quyền mới có thể đọc hoặc sửa dữ liệu.

![Image](https://github.com/user-attachments/assets/919df18e-8efe-49fe-ba64-7516fce4c978)

### Các bên liên quan và mối đe dọa
* Data Owners: Người sở hữu và quản lý dữ liệu.
* Data Users: Những người được cấp quyền truy cập vào dữ liệu (nhân viên, ngân hàng, cơ quan hành chính công).
* Cloud Storage: Nơi lưu trữ dữ liệu nhưng chỉ đóng vai trò trung gian, không được phép đọc nội dung.
* Mối đe dọa:
  - Bên thứ ba bán tín nhiệm (semi-trusted): Cloud có thể truy cập dữ liệu.
  - Kẻ giả mạo: Giả danh người có quyền để truy cập dữ liệu trái phép.

 ![Image](https://github.com/user-attachments/assets/c3c3d8f8-2ee5-411d-98a2-db105c5deccd)

 ### Giải pháp bảo mật
* Xác thực & cấp quyền (Authentication & Authorization): Đảm bảo chỉ người có quyền mới truy cập được hệ thống.
* Bảo mật dữ liệu (Confidentiality):
  * Mã hóa đối xứng AES: Đảm bảo dữ liệu trên Cloud không bị đọc bởi bên thứ ba.
  * Mã hóa CP-ABE (Ciphertext Policy Attribute-Based Encryption): Chỉ những người có thuộc tính phù hợp mới có thể giải mã dữ liệu.
  * Trao đổi khóa Diffie-Hellman: Tạo khóa bí mật động để bảo vệ thông tin truy vấn và dữ liệu.
 
![Image](https://github.com/user-attachments/assets/91724e99-09f0-45e6-936a-92083907d854)
![Image](https://github.com/user-attachments/assets/7da71bfa-1712-490c-81ba-15241bdffdc4)

### Triển khai và đánh giá
* Hệ thống được thử nghiệm trên môi trường Linux với các node giả lập (server ngân hàng, người dùng có quyền khác nhau).
* Các bước thử nghiệm gồm: tạo khóa, mã hóa dữ liệu, lưu trữ lên Cloud, kiểm soát truy vấn, giải mã dựa trên chính sách.
* Hệ thống hoạt động hiệu quả trong kiểm soát truy cập, nhưng chưa có xác thực từ phía server để đảm bảo người dùng không truy cập nhầm máy chủ.
