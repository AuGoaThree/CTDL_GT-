
# VTV5004 - 4. Quay lui. Hoán vị 2

def backtrack(arr, k, s):
    arr.sort()
    if len(arr) == k:
        print(" ".join(map(str, s)))
    else:
        for i in range(len(arr)):
            if arr[i] not in s[:k]:
                s[k] = arr[i]
                backtrack(arr, k + 1, s)


n= int(input())
s= []
s= list(map(int, input().split()))
if len(s) != n:
    raise ValueError("n phần tử.")
backtrack(s, 0, [0] * n)

   
