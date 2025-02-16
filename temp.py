import base64

# Chuỗi cần mã hóa
my_string = "Banker and VietABank"

# Mã hóa chuỗi thành Base64
encoded_bytes = base64.b64encode(my_string.encode('utf-8'))

# Chuyển đổi từ bytes sang chuỗi (nếu cần)
encoded_string = encoded_bytes.decode('utf-8')

print(encoded_bytes)
