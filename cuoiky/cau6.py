# VTV5011 - Quy hoach dong. Day con co tong chia het cho K
# cong thuc truy hoi:
# f[i][t] = min(
#     f[i-1][t],                              // khong chon a[i]
#     1 + f[i-1][(t - a[i]) mod k]            // chon a[i]
# )

def solve():
    # Doc input
    n, k = map(int, input().split())  # n: so phan tu, k: so chia
    a = list(map(int, input().split()))  # mang dau vao
    
    # Chuyen ve index 1-based
    a = [0] + a  # them phan tu 0 vao dau
    
    # Tinh tong tat ca
    total_sum = sum(a[1:])  # tong cac phan tu tu vi tri 1 den n
    
    # Kiem tra truong hop dac biet
    if total_sum % k == 0:
        print("Day da cho thoa man yeu cau.")
        print(f"Tong ={total_sum}")
        return
    
    # Khoi tao bang DP
    INF = n + 1  # gia tri vo cuc
    f = [[INF] * k for _ in range(n + 1)]  # bang DP f[i][t]
    f[0][0] = 0  # khoi tao: khong co phan tu nao, tong = 0
    
    # In header bang DP
    print("n/t", end="")
    for t in range(k):
        print(f"{t:4}", end="")
    print()
    
    # In hang 0
    print(f"{0:4}", end="")
    for t in range(k):
        if f[0][t] == INF:
            print(" +00", end="")  # gia tri vo cuc
        else:
            print(f"{f[0][t]:4}", end="")
    print()
    
    # Thuat toan DP
    for i in range(1, n + 1):  # i: chi so phan tu dang xet
        for t in range(k):  # t: so du can dat duoc
            # Khong chon a[i] (loai bo a[i])
            f[i][t] = f[i-1][t]
            
            # Chon a[i] (giu lai a[i])
            prev_t = (t - a[i]) % k  # trang thai truoc khi them a[i]
            if prev_t < 0:
                prev_t += k  # xu ly so am
            
            if f[i-1][prev_t] < INF:
                f[i][t] = min(f[i][t], f[i-1][prev_t] + 1)
        
        # In hang i
        print(f"{i:4}", end="")
        for t in range(k):
            if f[i][t] == INF:
                print(" +00", end="")
            else:
                print(f"{f[i][t]:4}", end="")
        print()

    # Tim ket qua
    target = total_sum % k  # so du can tim
    removed = f[n][target]  # so phan tu can loai bo
    
    if removed >= n:
        print("Khong co day con nao thoa man yeu cau.")
        return
    
    print(f"Chieu dai day con: {n - removed}")
    
    # Truy vet de tim day con
    i = n
    t = target
    selected = []  # cac phan tu duoc chon
    total_sum_selected = 0  # tong cac phan tu duoc chon

    for i in range(n, 0, -1):  # duyet nguoc tu n ve 1
        prev_t = (t - a[i]) % k
        if prev_t < 0:
            prev_t += k
            
        # Kiem tra co chon a[i] khong
        if f[i][t] == f[i-1][t]:
            # Chon a[i] (giu lai a[i])
            selected.append((i, a[i]))  # them vao danh sach
            total_sum_selected += a[i]  # cong vao tong
        else:
            t = prev_t  # chuyen sang trang thai truoc
    
    # In ket qua theo thu tu giam dan
    for idx, val in selected:
        print(f"a[{idx}]={val};", end="")
    print()
    print(f"Tong ={total_sum_selected}")

if __name__ == "__main__":
    solve()