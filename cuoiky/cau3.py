# VTV3022 - De quy. Qua trinh MergeSort. Phai sang trai

def merge(arr, left, mid, right):
    print(f"Merge: {left} --> {mid} and {mid+1} --> {right}")
    left_arr = arr[left:mid+1]  # mang con trai
    right_arr = arr[mid+1:right+1]  # mang con phai
    i = 0  # chi so cho mang con trai
    j = 0  # chi so cho mang con phai
    k = left  # chi so cho mang ket qua

    # Tron hai mang con
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # Sao chep cac phan tu con lai cua mang trai
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    # Sao chep cac phan tu con lai cua mang phai
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    
    # In ket qua sau khi tron
    print(' '.join(map(str, arr[left:right+1])))
    print()
    

def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2  # tinh diem giua
        print(f"Divide: {left} --> {mid} and {mid+1} --> {right}")
        printArrayDivide(arr, left, mid, right)
        
        # THAY DOI: Goi de quy ben PHAI truoc, roi den ben TRAI
        mergeSort(arr, mid + 1, right)  # xu ly nua phai truoc
        mergeSort(arr, left, mid)       # roi xu ly nua trai
        merge(arr, left, mid, right)    # cuoi cung tron lai


def printArrayDivide(arr, left, mid, right):
    left_part = " ".join(map(str, arr[left:mid + 1]))  # phan trai
    right_part = " ".join(map(str, arr[mid + 1:right + 1]))  # phan phai
    print(f"{left_part} :: {right_part}")

n = int(input())  # so phan tu
arr = list(map(int, input().split()))  # mang dau vao
print(" ".join(map(str, arr)))  # in mang ban dau
mergeSort(arr, 0, n - 1)  # bat dau sap xep