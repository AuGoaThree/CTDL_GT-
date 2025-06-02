# VTV4016 - Tham lam. Cái túi 0-1 theo giá trị

def knapsack_greedy_by_value(weights, values, W):
    n = len(weights)
    items = [(i, weights[i], values[i]) for i in range(n)]

    items.sort(key=lambda x: x[2], reverse=True)  
    
    total_value = 0
    total_weight = 0
    selected_items = []

    for i, w, v in items:
        if total_weight + w <= W:
            total_weight += w
            total_value += v
            selected_items.append((i+1, w, v)) 
    

    # Format output
    formatted_path = [f"{i}({w},{v});" for i, w, v in selected_items]
    
    return total_weight, total_value, formatted_path

# Đọc đầu vào
n, W = map(int, input().split())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))

total_weight, total_value, greedy_path = knapsack_greedy_by_value(weights, values, W)
print(f"Tong trong luong ={total_weight}")
print(f"Tong gia tri ={total_value}")
print("".join(greedy_path))