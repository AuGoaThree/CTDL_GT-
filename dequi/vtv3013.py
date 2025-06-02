# VTV3013 - 13. Đệ quy. Tính tổng của dãy 2

def S(n):
    def K(t):
        if t==n:
            return n/(n+1)
        else:
            return t/(t+1)+K(t+1)
    return K(1)
    
t=int(input())
results = []
for _ in range(t):
    n = int(input())
    results.append(S(n))
for result in results:
    print(f"{result:.10f}")