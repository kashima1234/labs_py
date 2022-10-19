n = int(input())
a = []
for i in range (n):
    a.append([])
    for j in range(n):
        a[i].append(j)
for  i in a:
    for j in i:
        print('{:^5}'.format(j),end='')
    print()
print()
s = 0
for i in range(n):
    for j in range(n):
        if (i >= j and i + j <= n - 1) or (i <= j and i+j >= n - 1):
            s += a[i][j]
print(s)
