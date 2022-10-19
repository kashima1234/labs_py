# Задана матрица D и массив I, содержащий номера строк, для которых
# необходимо определить максимальный элемент. Значения максимальных
# элементов запомнить в массиве R. Определить среднее арифметическое
# вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
# среднее арифметическое значение.
def input_list():
    m = n = -1
    list1 = []
    while m <= 0:
        m = int(input('Ввести количества строк матрицы:'))
    while n <= 0:
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
            print('{:>3}'.format(t[i][j]), ',', end='')
        print('{:>3}'.format(t[i][j + 1]), ']')

# d = [[54, 97, 76, 85, 83, 32, 80, 65], [74, 9, 1, 43, 42, 44, 77, 93], [18, 47, 9, 51, 9, 23, 75, 50],
#      [1, 26, 83, 50, 44, 7, 72, 75], [1, 12, 91, 86, 6, 53, 99, 59], [15, 39, 67, 78, 32, 96, 35, 88],
#      [95, 40, 36, 35, 66, 73, 83, 86], [61, 10, 45, 59, 23, 51, 39, 92]]
print("Вветите матрица D:")
d = input_list()

l = set()
i = 1
while i != 0:
    i = int(input(
        'Вветите номер строки(от 1), для которой необходимо определить максимальный элемент,заканчиваться на 0\n'))
    if i > 0:
        l.add(i)
    else:
        continue
r = []
for i in l:
    if i <= len(d):
        r.append(max(d[i - 1]))
s = 0
for i in r:
    s += i
print('d=')
output(d)
print('L=',l,'\nR=',r)
print('среднее арифметическое вычисленных максимальных значений=', round(s / len(r), 4))