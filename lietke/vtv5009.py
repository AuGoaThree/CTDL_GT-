# VTV5009 - Quay lui. Xếp quân hậu 2

def UCVh(row, col, a, n):
    for i in range(1, row):
        if a[i] == col or abs(a[i] - col) == abs(i - row):
            return False
    return True

def Ghinhan(a, n):
    for i in range(1, n + 1):
        print(a[i], end=" ")
    print()

def Hau(i, a, n, y, x):
    if i == n+1:  # Đã xếp đủ 8 dòng
        Ghinhan(a, n)
        return

    if i == y:  # Nếu là dòng y, chỉ đặt ở cột x
        if UCVh(i, x, a, n):  # Kiểm tra xem x có hợp lệ không
            a[i] = x
            Hau(i + 1, a, n, y, x)
        return

    # Thử tất cả các cột cho dòng hiện tại
    for j in range(1, n + 1):
        if UCVh(i, j, a, n):
            a[i] = j
            Hau(i + 1, a, n, y, x)
            a[i] = 0  # Khôi phục trạng thái

n = 8
y, x = map(int, input().split())  
a = [0] * (n + 1)
a[y] = x  
Hau(1, a, n, y, x)