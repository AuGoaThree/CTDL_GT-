# F[i][v] = max(
#     F[i-1][v],                           // không chọn món hàng i
#     F[i-1][v - A[i-1]] + C[i-1]         // chọn món hàng i (nếu A[i-1] ≤ v)
# )
# F[i][v] = giá trị tối đa có thể đạt được khi xét i món hàng đầu tiên với sức chứa túi là v
# VTV5012 - Quy hoach dong. Cai tui

def solve():
    # Doc dau vao
    n, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # Khoi tao bang DP
    F = [[0] * (M + 1) for _ in range(n + 1)]

    # In tieu de
    print("   C   A i/v", end="")
    for v in range(M + 1):
        print(f"{v:4}", end="")
    print()

    # In hang dau tien (hang 0)
    print("           0", end="")
    for v in range(M + 1):
        print(f"{F[0][v]:4}", end="")
    print()

    # DP
    for i in range(1, n + 1):
        for v in range(M + 1):
            # Khong chon mon hang i
            F[i][v] = F[i - 1][v]
            
            # Chon mon hang i (neu co the)
            if A[i - 1] <= v and F[i][v] < F[i - 1][v - A[i - 1]] + C[i - 1]:
                F[i][v] = F[i - 1][v - A[i - 1]] + C[i - 1]

        # In hang hien tai
        print(f"{C[i - 1]:4}{A[i - 1]:4}{i:4}", end="")
        for v in range(M + 1):
            print(f"{F[i][v]:4}", end="")
        print()

    # Ket qua cuoi cung
    print(F[n][M])

    # Truy vet
    i, v = n, M
    selected = []
    
    while i > 0:
        if F[i][v] != F[i - 1][v]:
            # Chon mon hang i
            selected.append((i, A[i - 1], C[i - 1]))
            v -= A[i - 1]
        i -= 1
    
    # In ket qua truy vet theo thu tu tang dan
    selected.reverse()
    for idx, weight, value in selected:
        print(f"{idx}({weight},{value})", end=" ")
    print()

if __name__ == "__main__":
    solve()