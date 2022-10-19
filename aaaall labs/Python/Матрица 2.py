s = 1
x,y = map(int,input('Enter number of rows and columns=').split())
matrix = []
for i in range(x):
    print('Введите элементы строки = '.format(i))
    temp_line = []
    for j in range(y):
        temp_line.append(int(input()))
    matrix.append(temp_line)
for  line in matrix:
    for elem in line:
        print('{:^5}'.format(elem),end='')
    print()
print()
for line in matrix:
    temp_sum = 0
    for elem in line:
        temp_sum += elem*elem
    s *= temp_sum
print(s)
