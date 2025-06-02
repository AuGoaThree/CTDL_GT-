# CTNC2003 - Sinh. Tổ hợp 1 

def combination_generation(n, k):
    c = list(range(1, k + 1))
    result = []
    while True:
        result.append(' '.join(map(str, c)))
        i = k - 1
        while i >= 0 and c[i] == n - (k - 1 - i):
            i -= 1
        if i < 0:
            break
        c[i] += 1
        for j in range(i + 1, k):
             # vị trí nhỏ nhất có thể
            c[j] = c[j - 1] + 1 
           
    print('\n'.join(result))


n, k = map(int, input().split())
combination_generation(n, k)

