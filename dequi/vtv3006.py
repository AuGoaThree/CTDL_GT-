# VTV3006 - 6. Đệ quy. Tính giá trị của hàm 1

from math import sqrt


def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return sqrt(n+f(n-1))

t=int(input())
results = []
for _ in range(t):
    n = int(input())
    results.append(f(n))
for result in results:
    print(f"{result:.10f}")