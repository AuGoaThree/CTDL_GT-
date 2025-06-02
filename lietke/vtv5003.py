# VTV5003 - 3. Quay lui. Hoán vị 1 giảm dần n..1

def backtrack(n, k, s):
    if n == k:
        print(" ".join(map(str, s)))
    else:
        for i in range(n, 0, -1):
            if i not in s[:k]:
                s[k] = i
                backtrack(n, k + 1, s)

n = int(input())
s = [0] * n
backtrack(n, 0, s)

