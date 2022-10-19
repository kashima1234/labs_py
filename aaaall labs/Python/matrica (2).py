n = int(input('Enter number of rows:'))
s = [list(map(int,input().split()))for i in range(n)]
print()
for i in s:
    for j in i:
        print(j,end='  ')
    print()
print()
rows = len(s)
columns = len(s[0])
for i in range(0 , rows):
    sum_columns = 0
    for j in range(0,columns):
        if s[i][j] > 0:
            sum_columns += s[j][i]
            average = sum_columns / columns
    print('Aritmetic of ' + min(str(i+1))+' column '+(str(average)))
print()

