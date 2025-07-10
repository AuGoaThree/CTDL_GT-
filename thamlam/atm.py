def solve_atm():
    W = int(input())
    c = int(input())
    
    # Kiem tra dieu kien co ban
    if W % 1000 != 0:
        return "0"
    
    menh_gia = [1000, 2000, 3000, 5000]
    count = 0  # so to tien
    ways = 1   # so cach
    money = W
    
    # Duyet tu luy thua cao nhat xuong thap nhat
    for j in range(c, -1, -1):
        used = [0, 0, 0, 0]  # danh dau menh gia nao duoc dung
        
        # Duyet tu menh gia cao nhat xuong thap nhat trong moi luy thua
        for k in range(3, -1, -1):  # 5000, 3000, 2000, 1000
            denomination = menh_gia[k] * (10 ** j)
            
            if money >= denomination:
                paper_needed = money // denomination
                count += paper_needed
                money %= denomination
                
                if paper_needed > 0:
                    used[k] = 1
        
        # Tinh so cach dua tren cac menh gia duoc su dung
        # Logic: 5000 = 2000+3000, 3000 = 1000+2000
        if used[3] == 1 and used[2] == 1 and used[0] == 1:  # dung 5000, 3000, 1000
            ways *= 3  # co 3 cach khac nhau
        elif used[3] == 1 and used[0] == 1:  # dung 5000 va 1000
            ways *= 2  # co 2 cach
        elif used[3] == 0 and used[2] == 1 and used[0] == 1:  # dung 3000 va 1000
            ways *= 2  # co 2 cach
    
    # Kiem tra xem co the doi het tien khong
    if money != 0:
        return "0"
    
    return f"{count} {ways}"

def main():
    t = int(input())
    for _ in range(t):
        result = solve_atm()
        print(result)

if __name__ == "__main__":
    main()