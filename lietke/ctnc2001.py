# CTNC2001 - Sinh. In dãy nhị phân 1

def binary_string_generation(n):
    """Sinh toàn bộ dãy nhị phân có n chữ số."""
    b = [0] * n  # Khởi tạo dãy nhị phân ban đầu với toàn 0
    while True:
        # In dãy hiện tại
        print(''.join(map(str, b)))
        
        # Tìm vị trí cuối cùng có giá trị 0 để chuyển thành 1
        i = n - 1
        while i >= 0 and b[i] == 1:
            b[i] = 0  # Đặt lại các bit 1 thành 0
            i -= 1
        
        # Nếu không còn vị trí nào để tăng, kết thúc
        if i < 0:
            break
        
        # Đặt bit 0 thành 1
        b[i] = 1

# Nhập số lượng chữ số nhị phân
n = int(input())
binary_string_generation(n)