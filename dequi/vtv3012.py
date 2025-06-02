# VTV3012 - 12. Đệ quy. Kiểm tra tính chất toàn giá trị âm

def is_all_negative(arr, n):
    if n == 0:
        return True
    if arr[n - 1] >= 0:
        return False
    return is_all_negative(arr, n - 1)
 
t=int(input())
results = [] 
for _ in range(t):
    n = int(input())
    real_number = list(map(float, input().split()))
    if len(real_number) != n:
        raise ValueError("The number of elements does not match the specified size.")
    result = is_all_negative(real_number, n)
    results.append(result)


for result in results:
    print("Yes" if result else "No")