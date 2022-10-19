# Ввести трёхмерный массив (массив матриц размера X*Y*Z), вывести из него i-й срез по второму индексу.
# list1 = [[[20, 1, 5, 2, 4], [7, 8, 9, 6, 3], [1, 5, 4, 2, 5], [8, 9, 6, 3, 1]], [[4, 5, 2, 7, 5], [6, 9, 8, 5, 2], [1, 4, 5, 2, 3], [6, 9, 8, 5, 4]], [[2, 1, 5, 3, 6], [9, 8, 4, 2, 5], [1, 25, 2, 5, 3], [58, 54, 2, 4, 8]]]
x = y = z = -1
list1=[]
print("Вветите трёхмерный массив с размерой X*Y*Z(X,Y,Z>=2):")
while x <= 1:
    x = int(input('X='))
while y <= 1:
    y = int(input('Y='))
while z <= 1:
    z = int(input('Z='))
for i in range(z):
    list1.append([])
    for j in range(y):
        list1[i].append([])
        for k in range(x):
            list1[i][j].append(int(input('Ввести {}-й элемент {}-й строки {}-ого стобца:'.format(k + 1, j + 1, i + 1))))
t = -1
while 0 > t or t> len(list1):
    t = int(input('Введите номер среза I(0<I<={}):'.format(len(list1))))
for i in range(len(list1)):
    print(list1[i][t-1])
print(list1)