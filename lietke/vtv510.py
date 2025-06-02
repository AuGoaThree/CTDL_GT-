
# VTV510 - Quay lui. Ốc sên ăn rau

n, m, y, x = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

# 4 hướng: lên, xuống, trái, phải
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def backtrack(u, v):
    visited[u][v] = True
    count = 1  # Đếm ô hiện tại

    for i in range(4):
        nu = u + dy[i]
        nv = v + dx[i]
        if 0 <= nu < n and 0 <= nv < m:
            if not visited[nu][nv] and garden[nu][nv] == 0:
                count += backtrack(nu, nv) 
    
    return count  

# Trừ 1 vì đề cho y,x theo dòng 1..n còn Python là 0-index
print(backtrack(y - 1, x - 1))
