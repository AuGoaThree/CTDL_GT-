# VTV3011 - 11. Đệ quy. Xác định giá trị phần tử của dãy 1

def X_Y(n, X_prev=1, Y_prev=0, i=0):
    """Tính giá trị X(n) và Y(n) bằng đệ quy đuôi."""
    if i == n:
        return X_prev, Y_prev
    else:
        X_curr = X_prev + Y_prev
        Y_curr = 3 * X_prev + Y_prev
        return X_Y(n, X_curr, Y_curr, i + 1)

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    Xn, Yn = X_Y(n)
    results.append((Xn, Yn))


for Xn, Yn in results:
    print(f"{Xn} {Yn}")