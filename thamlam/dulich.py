import sys

def tsp_greedy(distances):
    n = len(distances)
    
    # Kiểm tra ma trận hợp lệ
    if n == 0:
        return 0, ["1"]
    
    visited = [False] * n
    visited[0] = True
    
    curr_city = 0
    total_distance = 0
    path = ["1"]

    # Lặp qua các thành phố còn lại
    for i in range(n-1):
        next_city = -1
        min_distance = float('inf')  # Thay sys.maxsize

        for j in range(n):
            # Kiểm tra thành phố chưa thăm và khoảng cách hợp lệ
            if (not visited[j] and j != curr_city and 
                distances[curr_city][j] < min_distance):
                next_city = j
                min_distance = distances[curr_city][j]

        # Kiểm tra có tìm được thành phố tiếp theo không
        if next_city == -1:
            # Không tìm được thành phố tiếp theo
            break
            
        visited[next_city] = True
        curr_city = next_city
        total_distance += min_distance
        path.append("{}({})".format(curr_city + 1, min_distance))

    # Quay về thành phố đầu tiên
    return_distance = distances[curr_city][0]
    path.append("1({})".format(return_distance))
    total_distance += return_distance

    return total_distance, path

n = int(input().strip())
if n <= 0:
    print("Tong chi phi=0")
    print("1")
    sys.exit(0)
    
distances = []
for i in range(n):
        row = list(map(int, input().strip().split()))
        if len(row) != n:
            raise ValueError("Ma trận không hợp lệ")
        distances.append(row)

    # Giải TSP bằng thuật toán tham lam
min_distance, tsp_path = tsp_greedy(distances)

    # In kết quả
print("Tong chi phi={}".format(min_distance))
print("->".join(tsp_path))
