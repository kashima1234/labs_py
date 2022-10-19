M = int(input('Enter number of rows and colmns: '))
while M >= 18:
    M = int(input('Enter number of rows and colmns: '))
a = []
r = 1
for i in range(M):
    b = []
    for j in range(M):
        if j+i > M-1:  #dolna strana
            b.append(0)
        if j+i < M-1:   #gornastrana
            b.append(r)
            r += 1
        if j+i == M-1:  #diagonala
            b.append(r)
            i+=1
    a.append(b)
for i in a:
    for j in i:
        print('{:^5}'.format(j),end=' ')
    print()
