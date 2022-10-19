#  Даны массивы D и F. Сформировать матрицу A по формуле
# количество элементов, меньших среднего арифметического.
from math import sin


def average(t):
    S = 0
    k = 0
    for i in t:
        if i > 0:
            S += i
            k += 1
    if k == 0:
        return 0
    return round(S / k, 5)


def output(t):
    for i in range(len(t)):
        for j in range(len(t[i]) - 1):
            print('{:.5f}'.format(t[i][j]), ',', end='')
        print('{:.5f}'.format(t[i][j + 1]))


d = list(map(int, input("Введите массив D").split()))
f = list(map(int, input("Введите массив F").split()))
list1 = []
for i in range(len(d)):
    list1.append([])
    for j in range(len(f)):
        list1[i].append(sin(d[i] + f[j]))
# for i in a:
#     print('{:.5f}'.format(*i))
output(list1)
aver = []
k = []
for i in range(len(list1)):
    aver.append(average(list1[i]))
    count = 0
    for j in range(len(list1[i])):
        if round(list1[i][j], 5) < aver[i]:
            count += 1
    k.append(count)
print('\nСреднее арифметическое положительных чисел каждой строки матрицы:',end='')
for i in range(len(aver)):
    if aver[i]:
        print(aver[i],',',end='')
    else:print('нет положительных чисел',end='')

print('\nКоличество элементов, меньших среднего арифметического:',end='')
for i in range(len(k)):
    if aver[i]:
        print(k[i],',',end='')
    else: print('Среднего арифметического положительных чисел НЕТ',end='')