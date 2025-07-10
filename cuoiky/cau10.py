# VTV6001 - 1. Nhánh cận. Người du lịch 1

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
min_path = float('inf')
path = [0] * n

# Tìm cạnh nhỏ nhất trong ma trận để dùng cho cận dưới
min_edge = float('inf')
for i in range(n):
    for j in range(n):
        if i != j and a[i][j] < min_edge:
            min_edge = a[i][j]

def Try(i, curr_city, curr_len):
    global min_path
    if i == n:
        total_len = curr_len + a[curr_city][0]  # Quay về thành phố xuất phát
        if total_len < min_path:
            min_path = total_len
        return
    for next_city in range(1, n):
        if not visited[next_city]:
            temp_len = curr_len + a[curr_city][next_city]
            # Nhánh cận: nếu tổng hiện tại + cận dưới > min_path thì bỏ qua
            estimate = temp_len + (n - i) * min_edge
            if estimate >= min_path:
                continue
            visited[next_city] = True
            Try(i + 1, next_city, temp_len)
            visited[next_city] = False

visited[0] = True
Try(1, 0, 0)
print(min_path)