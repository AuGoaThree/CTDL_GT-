# VTV3026 - Đệ quy. Quá trình QuickSort. Pivot=Right

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def printPartition(arr, left, right):
    print()
    print(f"Partitioning: left={left}, right={right}")
    print(" ".join(map(str, arr[left:right + 1])))

def partition(arr, low, high):
    printPartition(arr, low, high)
    pivot = arr[high]
    left = low
    right = high - 1
    while True:
        while left <= right and arr[left] > pivot:
            left += 1
        while right >= left and arr[right] <= pivot:
            right -= 1
        if left >= right:
            break
        swap(arr, left, right)
        print(" ".join(map(str, arr[low:high + 1])))
        left += 1
        right -= 1
    swap(arr, left, high)
    print(" ".join(map(str, arr[low:high + 1])))
    return left

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

n = int(input())
arr = list(map(int, input().split()))
print(" ".join(map(str, arr)))
quickSort(arr, 0, n - 1)
print(" ".join(map(str, arr)))