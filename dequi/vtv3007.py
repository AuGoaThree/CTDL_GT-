# VTV3007 - 7. Đệ quy. Tính giá trị của hàm 2

from math import sqrt


def S(n):
    def K(t):
        if t==n:
            return sqrt(n)
        else:
            return sqrt(t+K(t+1))
    return K(1)
    
t=int(input())
results = []
for _ in range(t):
    n = int(input())
    results.append(S(n))
for result in results:
    print(f"{result:.10f}")