
# VTV3003 - 3. Đệ quy. Đếm số chữ số lớn nhất
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
    
def count_largest_digit(n, largest=None):
    if largest is None:
        largest = largest_digit(n)
    if n < 10:
        return 1 if n == largest else 0
    else:
        return (1 if n % 10 == largest else 0) + count_largest_digit(n // 10, largest)

    
t=int(input())
results = []
for _ in range(t):
    n = int(input())
    count_largest = count_largest_digit(n)
    results.append((n, count_largest))

max_width = max(len(str(n)) for n, _ in results)

for n, count_largest in results:
    print(f"{str(n).rjust(max_width)}: {count_largest}")