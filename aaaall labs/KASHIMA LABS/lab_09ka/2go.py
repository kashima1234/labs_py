# Найти максимальное значение над главной диагональю и минимальное - под побочной диагональю.
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
output(list1)
n=len(list1)
max_el=list1[0][1]
for i in range(n):
    for j in range(i+1,n):
        if list1[i][j]>max_el:
            max_el=list1[i][j]
min_el=list1[-1][1]
for i in range(n):
    for j in range(n-i,n):
        if min_el>list1[i][j]:
            min_el=list1[i][j]
print('Максимальное значение над главной диагональю:',max_el)
print("Минимальное значение под побочной диагональю:",min_el)


