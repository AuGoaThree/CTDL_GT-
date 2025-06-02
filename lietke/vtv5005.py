
# VTV5005 - 5. Quay lui. Chỉnh hợp
# chỉnh hợp
def backtrack(n, k, i, s, used):
    if i == k:
        print(" ".join(map(str, s)))
    else:
        for j in range(1, n + 1):
            if not used[j]:
                s[i] = j
                used[j] = True
                backtrack(n, k, i + 1, s, used)
                used[j] = False

n, k = map(int, input().split())
s = [0] * k
used = [False] * (n + 1)
backtrack(n, k, 0, s, used)
