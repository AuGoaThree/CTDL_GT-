# VTV5011 - Quy hoach dong. Day con co tong chia het cho K
# công thức truy hồi:
# f[i][t] = min(
#     f[i-1][t],                              // không chọn a[i]
#     1 + f[i-1][(t - a[i]) mod k]            // chọn a[i]
# )

# VTV5011 - Quy hoach dong. Day con co tong chia het cho K

def solve():
    # Doc input
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Chuyen ve index 1-based
    a = [0] + a
    
    # Tinh tong tat ca
    total_sum = sum(a[1:])
    
    # Kiem tra truong hop dac biet
    if total_sum % k == 0:
        print("Day da cho thoa man yeu cau.")
        print(f"Tong ={total_sum}")
        return
    
    # Khoi tao bang DP
    INF = n + 1
    f = [[INF] * k for _ in range(n + 1)]
    f[0][0] = 0
    
    # In header
    print("n/t", end="")
    for t in range(k):
        print(f"{t:4}", end="")
    print()
    
    # In hang 0
    print(f"{0:4}", end="")
    for t in range(k):
        if f[0][t] == INF:
            print(" +00", end="")
        else:
            print(f"{f[0][t]:4}", end="")
    print()
    
    # DP
    for i in range(1, n + 1):
        for t in range(k):
            # Khong chon a[i]
            f[i][t] = f[i-1][t]
            
            # Chon a[i] (bo phan tu a[i] di)
            prev_t = (t - a[i]) % k
            if prev_t < 0:
                prev_t += k
            
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
    target = total_sum % k
    removed = f[n][target]
    
    if removed >= n:
        print("Khong co day con nao thoa man yeu cau.")
        return
    
    print(f"Chieu dai day con: {n - removed}")
    
    # Truy vet
    i = n
    t = target
    selected = []
    total_sum_selected = 0

    for i in range(n, 0, -1):
        prev_t = (t - a[i]) % k
        if prev_t < 0:
            prev_t += k
            
        # Kiem tra co chon a[i] khong
        if f[i][t] == f[i-1][t]:
              # Chon a[i] (giu lai a[i])
            selected.append((i, a[i]))
            total_sum_selected += a[i]
        else:
            t = prev_t
    # In ket qua theo thu tu giam dan
    for idx, val in selected:
        print(f"a[{idx}]={val};", end="")
    print()
    print(f"Tong ={total_sum_selected}")

if __name__ == "__main__":
    solve()

