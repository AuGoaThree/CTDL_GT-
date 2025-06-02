# VTV5008 - 8. Quay lui. Xếp quân hậu
# Đề bài: Cho một bàn cờ N x N. Hãy tìm cách đặt N quân hậu lên bàn cờ sao cho không có quân nào ăn nhau.

def UCVh(j, k):
    """Kiểm tra xem có thể đặt quân hậu tại cột j, hàng k không."""
    for i in range(1, k):
        if x[i] == j or abs(x[i] - j) == abs(i - k):
            return False
    return True

def Ghinhan():
    global dem
    dem += 1
    print(f"Solution {str(dem).rjust(max_width)}:  ", end="")
    for i in range(1, n + 1):
        print(x[i], end="  ")
    print()

def Hau(i):
    """Đệ quy quay lui để tìm cách xếp quân hậu."""
    for j in range(1, n + 1):
        if UCVh(j, i):
            x[i] = j
            if i == n:
                Ghinhan()
            else:
                Hau(i + 1)

# Main
n = int(input())
x = [0] * (n + 1)
dem = 0

# Tính độ rộng lớn nhất của số thứ tự
max_width = len(str(n * n))  # Giả sử số lượng giải pháp tối đa là n * n

Hau(1)