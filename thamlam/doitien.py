# Cac menh gia tien co the tra lai
money_return = [500, 100, 50, 10, 5, 1]
# Gia tri to tien khach hang dua
money = 1000
# So test case
t = int(input())

while (t):
    # Doc so tien phai tra
    pay = int(input())
    # Chi so menh gia hien tai
    mark = 0
    # Dem so to tien tra lai
    count = 0
    # So tien can tra lai
    remain = money - pay
    
    while True:
        # Neu da tra du tien
        if remain == 0:
            print(count)
            break
        
        # Neu so tien con lai nho hon menh gia hien tai
        if remain < money_return[mark]:
            # Chuyen sang menh gia nho hon
            mark += 1
        else:
            # Su dung menh gia hien tai
            remain -= money_return[mark]
            count += 1
    
    # Giam so test case
    t -= 1