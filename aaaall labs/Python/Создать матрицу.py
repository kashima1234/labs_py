a = []
n,m =map(int,input('Введите количество строк и столбов:').split())
for i in range (n):
    b = []
    for j in range (m):
        b.append(int(input()))
    a.append(b)
for i in range (n):
    for j in range (m):
        print('{:^5}'.format(a[i][j]),end='')
    print()
for i in range (n):
    mn = 0
    for j in range (m):
        if a[i][j] < a[i][mn] and i != j:
            mn = j
    a[i][i], a[i][mn] = a[i][mn], a[i][i]
for i in range (n):
    for j in range (m):
        print('{:^5}'.format(a[i][j]),end='')
    print()
        
