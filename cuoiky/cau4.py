# VTV5010 - Quy hoach dong. Day con don dieu tang dai nhat

def longest_increasing_subsequence():
    # Doc so luong phan tu
    n = int(input())
    
    # Doc day so goc
    original_a = list(map(int, input().split()))
    
    # Them phan tu -vo cuc va +vo cuc vao dau va cuoi day
    # Vi tri 0: -vo cuc, vi tri 1..n: day goc, vi tri n+1: +vo cuc
    a = [-float('inf')] + original_a + [float('inf')]
    
    # L[i] = do dai day con tang dai nhat bat dau tu vi tri i
    L = [0] * (n + 2)
    
    # T[i] = vi tri phan tu tiep theo trong day con tang dai nhat tu vi tri i
    T = [0] * (n + 2)
    
    # Khoi tao: tu vi tri n+1 (+vo cuc) co day con dai nhat la 1
    L[n + 1] = 1  
    print(f"L[{n+1}]={L[n + 1]}")

    # Duyet nguoc tu vi tri n ve 0
    for i in range(n, -1, -1):
        # Khoi tao jmax la vi tri cuoi cung (n+1)
        jmax = n + 1
        print(f"jmax=n+1={n}+1={n+1}")
        
        # Tim vi tri j > i sao cho a[j] > a[i] va L[j] lon nhat
        for j in range(i + 1, n + 2):
            condition1 = a[j] > a[i]  # Dieu kien tang dan
            condition2 = L[j] > L[jmax]  # Tim day con dai hon
            
            # Neu ca 2 dieu kien deu thoa man
            if condition1 and condition2:
                print(f"i={i},j={j},jmax={jmax},a[{j}]>a[{i}] &&L[{j}]>L[{jmax}]:")
                jmax = j  # Cap nhat vi tri toi uu
                print(f"jmax=j={jmax}")
        
        # Do dai day con tang dai nhat tu vi tri i
        L[i] = L[jmax] + 1  
        print(f"L[{i}]=L[{jmax}]+1={L[i]}")
        
        # Luu vi tri phan tu tiep theo trong day con
        T[i] = jmax  
        print(f"T[{i}]=jmax={jmax}")
    
    # In do dai day con tang dai nhat (tru di 2 vi co them 2 phan tu gia)
    print(L[0] - 2)
    
    # Truy vet de in day con
    i = T[0]  # Bat dau tu phan tu dau tien trong day con
    result = []
    
    # Duyet theo chuoi lien ket T cho den khi gap phan tu cuoi (+vo cuc)
    while i != n + 1:
        result.append(f"a[{i}]={a[i]}")  # Them phan tu vao ket qua
        i = T[i]  # Chuyen den phan tu tiep theo
    
    # In ket qua neu co
    if result:
        print(";".join(result) + ";")

if __name__ == "__main__":
    longest_increasing_subsequence()