# Поворот квадратной матрицы на 90 градусов по часовой стрелке, затем на 90 градусов против часовой стрелки. Вывести промежуточную и итоговую матрицу.
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
            print('{:>3}'.format(t[i][j]), ',', end='')
        print('{:>3}'.format(t[i][j + 1]), ']')


list1 = []
input_list1()
print('Исходная матрица:')
output(list1)
list2 = []
for t in range(len(list1[0])):
    list2.append([])
for i in range(len(list2)):
    for j in range(len(list1)):
        list2[i].append(list1[len(list1)-1-j][i])

print("Промежуточная матрица:")
output(list2)
list3 = []
for t in range(len(list2[0])):
    list3.append([])
for i in range(len(list3)):
    for j in range(len(list2)):
        list3[i].append(list2[j][len(list2[i])-1-i])

print("Итоговая  матрица:")
output(list3)
