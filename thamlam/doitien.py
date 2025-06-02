money_return = [500,100,50,10,5,1]
money = 1000
t = int(input())

while (t):
    pay = int(input())
    mark = 0
    count = 0
    remain = money - pay
    while True:
        if remain == 0:
            print(count)
            break
        
        if remain < money_return[mark]:
            mark += 1
        else:
            remain -= money_return[mark]
            count += 1
    t -= 1