
# VTV5001 - 1. Quay lui. In dãy nhị phân 1

def backtrack(n, k, s):
    if n == k:
        print("".join(map(str, s)))
    else:
        for i in range(2):
            s[k] = i
            backtrack(n, k + 1, s)
n = int(input())
s = [0] * n
backtrack(n, 0, s)
