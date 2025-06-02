def solve_atm():
    W = int(input())
    c = int(input())
    
    # Kiểm tra điều kiện cơ bản
    if W % 1000 != 0:
        return "0"
    
    menh_gia = [1000, 2000, 3000, 5000]
    count = 0  # số tờ tiền
    ways = 1   # số cách
    money = W
    
    # Duyệt từ lũy thừa cao nhất xuống thấp nhất
    for j in range(c, -1, -1):
        used = [0, 0, 0, 0]  # đánh dấu mệnh giá nào được dùng
        
        # Duyệt từ mệnh giá cao nhất xuống thấp nhất trong mỗi lũy thừa
        for k in range(3, -1, -1):  # 5000, 3000, 2000, 1000
            denomination = menh_gia[k] * (10 ** j)
            
            if money >= denomination:
                paper_needed = money // denomination
                count += paper_needed
                money %= denomination
                
                if paper_needed > 0:
                    used[k] = 1
        
        # Tính số cách dựa trên các mệnh giá được sử dụng
        # Logic: 5000 = 2000+3000, 3000 = 1000+2000
        if used[3] == 1 and used[2] == 1 and used[0] == 1:  # dùng 5000, 3000, 1000
            ways *= 3  # có 3 cách khác nhau
        elif used[3] == 1 and used[0] == 1:  # dùng 5000 và 1000
            ways *= 2  # có 2 cách
        elif used[3] == 0 and used[2] == 1 and used[0] == 1:  # dùng 3000 và 1000
            ways *= 2  # có 2 cách
    
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