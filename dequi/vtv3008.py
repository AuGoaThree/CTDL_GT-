# VTV3008 - 8. Đệ quy. Tính tổng các phần tử chẵn của mảng (chia để trị)

def even_sum_divide_and_conquer(arr, left, right):
    """Tính tổng các phần tử chẵn trong mảng bằng đệ quy chia để trị."""
    if left > right:
        return 0
    if left == right:
        return arr[left] if arr[left] % 2 == 0 else 0
    mid = (left + right) // 2
    left_sum = even_sum_divide_and_conquer(arr, left, mid)
    right_sum = even_sum_divide_and_conquer(arr, mid + 1, right)
    return left_sum + right_sum

# Nhập dữ liệu
n = int(input())
arr = list(map(int, input().split()))

# Kiểm tra kích thước mảng
if len(arr) != n:
    raise ValueError("The number of elements does not match the specified size.")

# In kết quả
print(even_sum_divide_and_conquer(arr, 0, n - 1))