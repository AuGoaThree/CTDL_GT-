

# VTV5006 - 6. Quay lui. Tổ hợp 1

def backtrack(n, k, i, s):
    if i == k:
        print(" ".join(map(str, s)))
    else:
        for j in range(s[i - 1] + 1, n + 1):
            s[i] = j
            backtrack(n, k, i + 1, s)
n, k = map(int, input().split())
s = [0] * k
backtrack(n, k, 0, s)
