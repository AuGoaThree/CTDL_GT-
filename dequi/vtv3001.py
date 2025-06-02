# VTV3001 - 1. Đệ quy. Quá trình tính giai thừa
def factorial(n):
  
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    n = int(input())
    if n < 0 or n > 12:
        raise ValueError("Input must be an integer between 0 and 12.")
    for i in range(n + 1):
        print(f"{i}! = {factorial(i)}")
except ValueError as e:
    print(e)