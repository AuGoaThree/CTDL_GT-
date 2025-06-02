# VTV4005 - 5. Tìm kiếm nhị phân

def mergeParts(arr, left, mid, right):
    temp = [0] * (right - left + 1)
    i = left
    j = mid + 1
    k = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp[i - left]

def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        mergeSort(arr, left, mid)  
        mergeSort(arr, mid + 1, right)  
        mergeParts(arr, left, mid, right)  

def interpolationSearch(arr, left, right, x):
    if left > right or x < arr[left] or x > arr[right]:
        return -1
    
    while left <= right and x >= arr[left] and x <= arr[right]:
        if arr[left] == arr[right]:
            if arr[left] == x:
                return left
            return -1
        
        pos = left + ((x - arr[left]) * (right - left)) // (arr[right] - arr[left])
        
        if pos < left or pos > right:
            return -1
            
        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1


n = int(input())
arr = list(map(int, input().split()))
if n > 0:
    mergeSort(arr, 0, n - 1)
k = int(input())
x = []
result = []
for i in range(k):
    x.append(int(input()))
for i in range(k):
    result.append(interpolationSearch(arr, 0, n - 1, x[i]))
print(" ".join(map(str, arr)))
print("\n".join(map(str, result)))