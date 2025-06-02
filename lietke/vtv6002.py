
# VTV6002 - 2. Nhánh cận. Người du lịch 2

def Try(i, curr_city, curr_len, curr_path, start_city):
    global min_path, best_paths
    if i == n:
        total_len = curr_len + a[curr_city][start_city]  # Quay ve diem xuat phat
        if total_len < min_path:
            min_path = total_len
            best_paths = [curr_path[:]]  # Luu lo trinh moi
        elif total_len == min_path:
            best_paths.append(curr_path[:])  # Them lo trinh co cung chi phi
        return
    
    # Nhanh can
    estimate = curr_len + (n - i) * min_edge
    if estimate >= min_path:
        return
    
    for next_city in range(n):
        if not visited[next_city]:
            visited[next_city] = True
            curr_path[i] = next_city
            Try(i + 1, next_city, curr_len + a[curr_city][next_city], curr_path, start_city)
            visited[next_city] = False

# Doc input
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# Tim canh nho nhat cho can duoi
min_edge = float('inf')
for i in range(n):
    for j in range(n):
        if i != j and a[i][j] < min_edge:
            min_edge = a[i][j]

# Khoi tao bien
min_path = float('inf')
best_paths = []  # Luu tat ca lo trinh toi uu

# Thu bat dau tu moi thanh pho
for start_city in range(n):
    visited = [False] * n
    path = [0] * n
    visited[start_city] = True
    path[0] = start_city
    Try(1, start_city, 0, path, start_city)

# In ket qua
print(f"Min total distance = {min_path}")
for i, p in enumerate(best_paths, 1):
    print(f"Solution  {i}:    {'   '.join(map(str, p))}")