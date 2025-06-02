
# VTV3004 - 4. Đệ quy. Tìm ước chung lớn nhất
def GCD(a, b):
    if b == 0:
        return a
    if a%b == 0:
        return b
    return GCD(b, a%b)

t=int(input())
results = []
for _ in range(t):
    a, b = map(int, input().split())
    results.append(GCD(a, b))
for result in results:
    print(result)