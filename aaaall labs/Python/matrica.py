n = int(input('Введите количество строк  матрицы: '))
m = int(input('Введите количество столбцов матрицы: '))
matrix = []
for i in range(n):
    print('Введите элементы строки: '.format(i))
    tempLine = []
    for j in range(m):
        tempLine.append(int(input()))
    matrix.append(tempLine)
for line in matrix:
    for elem in line:
        print('{:^5}'.format(elem),end='')      
    print()
print()
rows = len(matrix)
colums = len(matrix[0])
for i in range(rows):
    summ = 1
    for j in range(colums):
        summ *= matrix[j][i]
    print('Произведение ' + str(i+1) +' столбца = ' + str(summ))      

