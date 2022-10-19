# Дана матрица символов. Заменить в ней все гласные английские буквы на точки.
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
            list1[i].append(input('Ввести {}-й элемент {}-й строки:'.format(j + 1, i + 1)))
    return list1

def output(t):
    for i in range(len(t)):
        print('[', end='')
        for j in range(len(t[i]) - 1):
            print('{:>3}'.format(t[i][j]), ',', end='')
        print('{:>3}'.format(t[i][j + 1]), ']')
    print('')


print('Вветите матрицу:')
list1 = input_list()
# list1=[['a','w','a','d','u'],['a','e','g','o','g'],['a','g','i','5','u'],['g','e','i','o','h']]
list2 = ['a','e','i','o','u','y','A','E','I','O','U','Y']
output(list1)
for i in range( len(list1)):
    for j in range(len(list1[i])):
        if list1[i][j] in list2:
            list1[i][j]='.'
output(list1)