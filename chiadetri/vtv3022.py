
# VTV3022 - Đệ quy. Quá trình MergeSort. Trái sang phải

def merge(arr, left, mid, right):
    print(f"Merge: {left} --> {mid} and {mid+1} --> {right}")
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]
    i = 0  
    j = 0  
    k = left  

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    
    print(' '.join(map(str, arr[left:right+1])))
    print()
    

def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        print(f"Divide: {left} --> {mid} and {mid+1} --> {right}")
        printArrayDivide(arr, left, mid, right)
        
        mergeSort(arr, left, mid)  
        mergeSort(arr, mid + 1, right)  
        merge(arr, left, mid, right)


def printArrayDivide(arr, left, mid, right):
    left_part = " ".join(map(str, arr[left:mid + 1]))
    right_part = " ".join(map(str, arr[mid + 1:right + 1]))
    print(f"{left_part} :: {right_part}")

n= int(input())
arr= list(map(int, input().split()))
print(" ".join(map(str, arr)))
mergeSort(arr, 0, n - 1)
