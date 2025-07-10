# VTV13 - Quy hoach dong. Bien doi chuoi

def Min3(x, y, z):
    t = x if x < y else y
    return t if t < z else z

def solve():
    # Doc input
    n, m = map(int, input().split())
    X = input()  # Chuoi nguon
    F = input()  # Chuoi dich
    
    # Them ky tu gia de bat dau tu index 1
    X = " " + X
    F = " " + F
    
    # Khoi tao bang QHD
    # f[i][j] = so phep bien doi it nhat de dua X[1..i] thanh F[1..j]
    f = [[0] * (max(n, m) + 2) for _ in range(max(n, m) + 2)]
    
    # Truong hop co so: bien doi xau rong
    for i in range(n + 1):
        f[i][0] = i  # Can i phep xoa de bien X[1..i] thanh xau rong
    
    for j in range(m + 1):
        f[0][j] = j  # Can j phep chen de bien xau rong thanh F[1..j]
    
    # Dien bang QHD
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Neu ky tu cuoi cung giong nhau
            if X[i] == F[j]:
                f[i][j] = f[i-1][j-1]
            else:
                # Min cua 3 thao tac (xoa, chen, thay the)
                f[i][j] = 1 + Min3(f[i-1][j], f[i][j-1], f[i-1][j-1])
    
    # In bang phuong an
    print("   F", end="")
    for j in range(m + 1):
        print(f"{j:4}", end="")
    print()
    
    for i in range(n + 1):
        print(f"{i:4}", end="")
        for j in range(m + 1):
            print(f"{f[i][j]:4}", end="")
        print()
    
    # In so phep bien doi toi thieu
    print(f[n][m])
    
    # Truy vet cac phep bien doi theo thuat toan da cho trong hinh
    operations = []
    i, j = n, m
    
    while i > 0 or j > 0:
        # Trường hợp 1: X[i] == F[j]
        if i > 0 and j > 0 and X[i] == F[j]:
            i -= 1
            j -= 1

        # Trường hợp 2a: Insert
        elif j > 0 and f[i][j] == f[i][j-1] + 1:
            # Neu i = 0, nghia la chen vao dau chuoi, nen vi tri la 1
            insert_pos = i + 1 if i == 0 else i
            operations.append(f"Insert({insert_pos},{F[j]})")
            j -= 1

        # Trường hợp 2b: Replace  
        elif i > 0 and j > 0 and f[i][j] == f[i-1][j-1] + 1:
            operations.append(f"Replace({i},{F[j]})")
            i -= 1
            j -= 1

        # Trường hợp 2c: Delete
        elif i > 0 and f[i][j] == f[i-1][j] + 1:
            operations.append(f"Delete({i})")
            i -= 1
    
    # In cac phep bien doi theo dung thu tu
    for op in operations:
        print(op)

if __name__ == "__main__":
    solve()