# VTV5002 - 2. Quay lui. In dãy nhị phân 2  giảm dần

def backtrack(n, k, s):
    if n == k:
        print("".join(map(str, s)))
    else:
        for i in range(1, -1, -1):
            s[k] = i
            backtrack(n, k + 1, s)

n = int(input())
s = [0] * n
backtrack(n, 0, s)

