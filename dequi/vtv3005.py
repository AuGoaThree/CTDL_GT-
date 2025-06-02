
# VTV3005 - 5. ĐQ. In biểu diễn nhị phân của số nguyên dương

def binary_representation(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return binary_representation(n // 2) + str(n % 2)

t=int(input())
results = []
for _ in range(t):
    n = int(input())
    results.append(binary_representation(n))
for result in results:
    print(result)