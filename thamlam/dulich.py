import sys

def tsp_greedy(distances):
    n = len(distances)  # so thanh pho
    
    # Kiem tra ma tran hop le
    if n == 0:
        return 0, ["1"]
    
    visited = [False] * n  # danh dau thanh pho da tham
    visited[0] = True  # bat dau tu thanh pho 0
    
    curr_city = 0  # thanh pho hien tai
    total_distance = 0  # tong khoang cach di duoc
    path = ["1"]  # duong di (bat dau tu thanh pho 1)

    # Lap qua cac thanh pho con lai
    for i in range(n-1):  # i: chi so buoc lap
        next_city = -1  # thanh pho tiep theo se di
        min_distance = float('inf')  # khoang cach nho nhat tim duoc

        for j in range(n):  # j: chi so thanh pho dang xet
            # Kiem tra thanh pho chua tham va khoang cach hop le
            if (not visited[j] and j != curr_city and 
                distances[curr_city][j] < min_distance):
                next_city = j  # cap nhat thanh pho toi uu
                min_distance = distances[curr_city][j]  # cap nhat khoang cach nho nhat

        # Kiem tra co tim duoc thanh pho tiep theo khong
        if next_city == -1:
            # Khong tim duoc thanh pho tiep theo
            break
            
        visited[next_city] = True  # danh dau da tham thanh pho moi
        curr_city = next_city  # chuyen den thanh pho moi
        total_distance += min_distance  # cong them khoang cach
        path.append("{}({})".format(curr_city + 1, min_distance))  # them vao duong di

    # Quay ve thanh pho dau tien
    return_distance = distances[curr_city][0]  # khoang cach tu thanh pho cuoi ve thanh pho dau
    path.append("1({})".format(return_distance))  # them buoc cuoi vao duong di
    total_distance += return_distance  # cong them khoang cach quay ve

    return total_distance, path  # tra ve tong khoang cach va duong di

n = int(input().strip())  # so thanh pho nhap tu ban phim
if n <= 0:
    print("Tong chi phi=0")
    print("1")
    sys.exit(0)
    
distances = []  # ma tran khoang cach giua cac thanh pho
for i in range(n):  # i: chi so hang trong ma tran
    row = list(map(int, input().strip().split()))  # hang du lieu nhap vao
    if len(row) != n:
        raise ValueError("Ma tran khong hop le")
    distances.append(row)  # them hang vao ma tran

# Giai TSP bang thuat toan tham lam
min_distance, tsp_path = tsp_greedy(distances)  # min_distance: tong chi phi, tsp_path: duong di

# In ket qua
print("Tong chi phi={}".format(min_distance))
print("->".join(tsp_path))