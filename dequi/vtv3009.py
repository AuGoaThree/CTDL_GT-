
# VTV3009 - 9. Đệ quy. Đếm số phần tử dương trong mảng
def count_positive_elements(arr, n, count=0):
    if n < 0:
        return count
    if arr[n] > 0:
        count += 1
    return count_positive_elements(arr, n - 1, count)
  
n = int(input())
arr = list(map(float, input().split()))

if len(arr) != n:
    raise ValueError("The number of elements does not match the specified size.")

positive_count = count_positive_elements(arr, n - 1)
print(positive_count)