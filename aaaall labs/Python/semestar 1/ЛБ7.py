#Пискунов Панте. Лабораторная работа №7
print()
print('Mатрица A')
print()
n = int(input('Введите количество строк матрицы: '))
while n <= 0 or n > 5:
    n = int(input('Введите количество строк матрицы: '))
print()
print()
a = []
r = 2
for i in range (n):
    b = []
    for j in range (n):
        if i == j:
            b.append(0)     #Создаем диагональ матрицы из 0
        elif j < i:
            b.append(1)     #Создаем нижный треугольник матрицы из 1
        else:
            b.append(r)
            r += 1          #Создаем верхный треугольник матрици
    a.append(b)
print(a)
for i in range (n):
    for j in range (n):
        print('{:^5}'.format(a[i][j]),end=' ')   #Печатаем нашу матрицу
    print()
print()
rows = len(a)
columns = len(a[0])
empty = []
for i in range (0,rows):
    sumRow = 0
    for j in range (0,columns):
        sumRow += a[i][j]
        average = sumRow/n      #Ишем среднее арифметическое значение каждой строки
        empty.append(average)   #Ишем максимальный элемент матрицы
    print('Среднее арифметическое значение ' + str(i+1) +' строки: ' + str(average))
print()
print('Наибольшее арифметическое значение = ',max(empty))
print()
print()
print('Maтрица V')
print()
n = int(input('Введите количество строк  матрицы: '))
while n <= 0 or n > 17:
    n = int(input('Введите количество строк матрицы: '))
m = int(input('Введите количество столбцов матрицы: '))
while m <= 0 or m > 7:
    m = int(input('Введите количество столбцов матрицы: '))      #Количество столбцов
matrix = []   #Пустой список
for i in range(n):
    print('Введите элементы строки: '.format(i))
    tempLine = []
    for j in range(m):
        tempLine.append(int(input()))     #Выбираем элементы по случайномѕ выбору
    matrix.append(tempLine)
for line in matrix:
    for elem in line:
        print('{:^5}'.format(elem),end='')      #Печатаем матрицу V
    print()
print()
z = [(sum(j for j in i if j > 0), sum(1 for j in i if j > 0)) for i in matrix]  #Ишем среднее арифметическое значение матрицы
z = [round(i[0]/i[1], 3) if i[1] else int('0') for i in z]    #Если все елементы в строке отрицательные,то их превращаем в 0
z = [i for i in z if i != 0]                                #Удаляем все нули
print()
print('Z = ',z)
z[z.index(max(z))],z[0] = z[0],z[z.index(max(z))]   #Меняем местами максимального элемента с первым 
print('Обновленый список = ',z)
print()
print()
print('Матрица Z')
print()
N = int(input('Введите количество строк матрицы: '))
M = int(input('Введите количество столбцов матрицы: '))
print()
Matrix = []
for i in range(N):
    for j in range(M):
        Matrix.append(z)
for i in range(N):
    for j in range(M):
        print(Matrix[i][j],end='  ')
    print()
print()
print()
print('Матрица V')
print()
for line in matrix:
    for elem in line:
        print('{:^5}'.format(elem),end='') #Печатаем матрицу V
    print()
print()
    
#Matrix = []
#while z != []:
 #   Matrix.append(z[:3])
  #  z = z[3:]
#for i in Matrix:
 #   for j in i:
  #      print('{:^8}'.format(j),end=' ')   #Печатаем массив Z в виде матрицы
   # print()
#print()
