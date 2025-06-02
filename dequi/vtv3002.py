
# VTV3002 - 2. Đệ quy. Xác định chữ số lớn nhất
def maximum(a, b):
    if a > b:
        return a
    else:
        return b    
    
def largest_digit(n):
    if n < 10:
        return n
    else:
        return maximum(n % 10, largest_digit(n // 10))

t=int(input())
results = []
for _ in range(t):
    n = int(input())
    largest_digit_num = largest_digit(n)
    results.append((n, largest_digit_num))

max_width = max(len(str(n)) for n, _ in results)

for n, largest_digit_num in results:
    print(f"{str(n).rjust(max_width)}: {largest_digit_num}")