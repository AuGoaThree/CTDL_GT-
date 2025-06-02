# VTV3020 - Đệ quy. Sắp xếp trộn (MergeSort) tăng dần

def mergeParts(arr, left, mid, right):
    # Tạo mảng tạm để lưu trữ các phần tử đã sắp xếp
    temp = [0] * (right - left + 1)
    i = left
    j = mid + 1
    k = 0

    # So sánh và sắp xếp các phần tử từ hai nửa
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    # Sao chép các phần tử còn lại từ nửa bên trái (nếu có)
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    # Sao chép các phần tử còn lại từ nửa bên phải (nếu có)
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Sao chép các phần tử đã sắp xếp về mảng gốc
    for i in range(left, right + 1):
        arr[i] = temp[i - left]

def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        mergeSort(arr, left, mid)  
        mergeSort(arr, mid + 1, right)  
        mergeParts(arr, left, mid, right)  


n= int(input())
arr= list(map(int, input().split()))
mergeSort(arr, 0, n - 1)
print(" ".join(map(str, arr)))