
# CTNC2002 - Sinh. Hoán vị 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr


def permutation_generation(n):
    # các hoán vị sắp xếp giảm dần
    a= [i for i in range(n, 0, -1)] 
    while True:
        # In hoán vị hiện tại
        print(' '.join(map(str, a)))

        # Tìm vị trí cuối cùng có giá trị nhỏ hơn phần tử tiếp theo để hoán đổi
        i = n - 2
        while i >= 0 and a[i] < a[i + 1]:
            i -= 1

        # Nếu không còn vị trí nào để hoán đổi, kết thúc
        if i < 0:
            break

        # Tìm vị trí lớn nhất từ bên phải để hoán đổi với a[i]
        j = n - 1
        while a[i] < a[j]:
            j -= 1
        # Hoán đổi a[i] và a[j]
        a = swap(a, i, j)
        # Đảo ngược phần còn lại của dãy từ i+1 đến n-1
        a = a[:i + 1] + a[i + 1:][::-1]

n= int(input())
permutation_generation(n)