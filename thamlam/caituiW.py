# VTV4017 - Tham lam. Cái túi 0-1 theo giá trị trên 1 đơn vị W

def knapsack_greedy_by_ratio(weights, values, W):
    n = len(weights)
   
    items = []
    for i in range(n):
        if weights[i] != 0:
            ratio = values[i] / weights[i]
        else:
            ratio = float('inf') if values[i] > 0 else 0
        items.append((i, weights[i], values[i], ratio))
    
    # Sắp xếp theo tỷ lệ giảm dần
    items.sort(key=lambda x: x[3], reverse=True)
    
    total_value = 0
    total_weight = 0
    selected_items = []

    for i, w, v, ratio in items:
        if total_weight + w <= W:
            total_weight += w
            total_value += v
            selected_items.append((i+1, w, v, ratio))
    
   
    formatted_path = []
    for i, w, v, ratio in selected_items:
        ratio_str = f"{ratio:.2f}".replace('.', ',')  
        formatted_path.append(f"{i}({w}-{v}-{ratio_str});")
    
    return total_weight, total_value, formatted_path


n, W = map(int, input().split())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))

total_weight, total_value, greedy_path = knapsack_greedy_by_ratio(weights, values, W)
print(f"Tong trong luong ={total_weight}")
print(f"Tong gia tri ={total_value}")
print("".join(greedy_path))