# VTV7004 - 4. Tham lam. Trồng cây

n=int(input())
trees = list(map(int, input().split()))
trees.sort(reverse=True)

party_day = 0
for i in range(n):
    day_to_grow = trees[i]
    party_day = max(party_day, day_to_grow + i+1)
party_day += 1 
print(party_day)