
# VTV3010 - 10. Đệ quy. Tính tổng của dãy 1

def factorial(n):
  
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def S(x,n):
    def K(t):
        if t>n:
            return 0
        else:
            return pow(x,t)/factorial(t)+K(t+1)
    return K(1)

t=int(input())
results = []
for _ in range(t):
    # x là số double
    # n là số nguyên dương
    x, n = (input().split())
    x = float(x)
    n = int(n) 
    results.append(S(x,n))
for result in results:
    print(f"{result:.8f}")