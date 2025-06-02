# VTV3023 - Đệ quy. Sắp xếp nhanh (QuickSort) giảm dần

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, low, high):
    pivot = arr[high]
    left = low
    right = high - 1
    while True:
        while left <= right and arr[left] > pivot:
            left += 1
        while right >= left and arr[right] < pivot:
            right -= 1
        if left >= right:
            break
        swap(arr, left, right)
        left += 1
        right -= 1
    swap(arr, left, high)
    return left

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

n = int(input())
arr = list(map(int, input().split()))
quickSort(arr, 0, n - 1)
print(" ".join(map(str, arr)))