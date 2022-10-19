# Транспонирование квадратной матрицы.

def input_list1():
    global list1
    m = -1
    list1 = []
    while m < 1:
        m = int(input('Ввести количества строк матрицы:'))
    for i in range(m):
        list1.append([])
        for j in range(m):
            list1[i].append(int(input('Ввести {}-й элемент {}-й строки:'.format(j + 1, i + 1))))


def output(t):
    for i in range(len(t)):
        print('[', end='')
        for j in range(len(t[i]) - 1):
            print('{:>4}'.format(t[i][j]), ',', end='')
        print('{:>4}'.format(t[i][j + 1]), ']')


list1 = []
input_list1()
print('Исходная матрица:')
output(list1)
list2 = []
for i in range(len(list1[0])):
    list2.append([])
    for j in range(len(list1)):
        list2[i].append(list1[j][i])
print("Транспонирование матрицы:")
output(list2)
