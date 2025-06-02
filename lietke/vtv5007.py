

# VTV5007 - 7. Quay lui. Tổ hợp 2 Giảm dần mỗi phần tử giảm dần

def backtrack(pos, start):
    if pos == k:
        print(' '.join(map(str, comb)))
        return
    for i in range(start, 0, -1):
        comb[pos] = i
        backtrack(pos + 1, i - 1)

n, k = map(int, input().split())
comb = [0] * k

backtrack(0, n)
