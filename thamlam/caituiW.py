# VTV4017 - Tham lam. Cai tui 0-1 theo gia tri tren 1 don vi W

def knapsack_greedy_by_ratio(weights, values, W):
    n = len(weights)  # so luong do vat
   
    items = []  # danh sach cac do vat voi ty le gia tri/trong luong
    for i in range(n):  # i: chi so do vat dang xet
        if weights[i] != 0:
            ratio = values[i] / weights[i]  # ty le gia tri/trong luong
        else:
            ratio = float('inf') if values[i] > 0 else 0  # xu ly truong hop trong luong bang 0
        items.append((i, weights[i], values[i], ratio))  # them do vat vao danh sach
    
    # Sap xep theo ty le giam dan
    items.sort(key=lambda x: x[3], reverse=True)
    
    total_value = 0  # tong gia tri cua cac do vat duoc chon
    total_weight = 0  # tong trong luong cua cac do vat duoc chon
    selected_items = []  # danh sach cac do vat duoc chon

    for i, w, v, ratio in items:  # i: chi so, w: trong luong, v: gia tri, ratio: ty le
        if total_weight + w <= W:  # kiem tra co the them do vat vao tui khong
            total_weight += w  # cong them trong luong
            total_value += v  # cong them gia tri
            selected_items.append((i+1, w, v, ratio))  # them do vat vao danh sach ket qua (chi so +1)
    
    # Dinh dang chuoi ket qua
    formatted_path = []  # danh sach chuoi dinh dang
    for i, w, v, ratio in selected_items:  # duyet qua cac do vat duoc chon
        ratio_str = f"{ratio:.2f}".replace('.', ',')  # chuyen ty le thanh chuoi voi dau phay
        formatted_path.append(f"{i}({w}-{v}-{ratio_str});")  # tao chuoi dinh dang
    
    return total_weight, total_value, formatted_path  # tra ve ket qua


n, W = map(int, input().split())  # n: so do vat, W: trong luong toi da cua tui
weights = list(map(int, input().split()))  # danh sach trong luong cac do vat
values = list(map(int, input().split()))  # danh sach gia tri cac do vat

total_weight, total_value, greedy_path = knapsack_greedy_by_ratio(weights, values, W)  # giai bai toan tham lam
print(f"Tong trong luong ={total_weight}")
print(f"Tong gia tri ={total_value}")
print("".join(greedy_path))  # in duong di (cac do vat duoc chon)