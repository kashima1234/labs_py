# Подсчитать в каждой строке матрицы D количество элементов, превышающих
# суммы элементов соответствующих строк матрицы Z. Разместить эти
# количества в массиве G, умножить матрицу D на максимальный элемент
# массива G. Напечатать матрицу D до и после преобразования, а также массив
# G.
from numpy import random

def input_list():
    m = n = -1
    list1 = []
    while m < 2:
        m = int(input('Ввести количества строк матрицы:'))
    while n < 2:
        n = int(input('Ввести количества стобцов матрицы:'))
    for i in range(m):
        list1.append([])
        for j in range(n):
            list1[i].append(int(input('Ввести {}-й элемент {}-й строки:'.format(j + 1, i + 1))))
    return list1


def output(t):
    for i in range(len(t)):
        print('[', end='')
        for j in range(len(t[i]) - 1):
            print('{:>4}'.format(t[i][j]), ',', end='')
        print('{:>4}'.format(t[i][j + 1]), ']')

def radom_list():
    global list2
    try:
        a, b = map(int, input('Ввести количества строк и стобцов случайной матрицы:').split())
        list2 = random.randint(1, 100, size=(a, b))
    except:
        radom_list()

list2=[]
print('Вветите матрицу D:')
d = input_list()
# radom_list()
# d=list2.copy()
print('Вветите матрицу Z:')
z=[]
# z = [[9,9,20],[8,10,10],[3,5,10],[1,2,3],[10,10,20]]
# d=[[1,70,53,49,5],[20,57,87,77,45],[37,17,50,41,73],[90,24,83,5,15],[18,5,64,30,90]]

m = len(d)
n = -1
while n <= 0:
    n = int(input('Ввести количества стобцов матрицы z:'))
for i in range(m):
    z.append([])
    for j in range(n):
        z[i].append(int(input('Ввести {}-й элемент {}-й строки:'.format(j + 1, i + 1))))

g = []
for i in range(len(d)):
    k=s=0
    for j in range(len(z[i])):
        s+=z[i][j]
    for t in range(len(d[i])):
        if d[i][t]>s:
            k+=1
    g.append(k)
print('Матрица D до преобразования')
output(d)
print(f'G={g}\nНайбольший элемент Матрицы G={max(g)}')

a=max(g)
d1=d.copy()
for i in range(len(d)):
    for j in range(len(d[i])):
        d1[i][j]=d[i][j]*a
print('Матрица D после преобразования')
output(d1)