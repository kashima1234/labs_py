# Сформировать матрицу C путём построчного перемножения матриц A и B
# одинаковой размерности (элементы в i-й строке матрицы A умножаются на
# соответствующие элементы в i-й строке матрицы B), потом сложить все
# элементы в столбцах матрицы C и записать их в массив V.
def input_list():
    m = n = -1
    list1 = []
    while m <= 0:
        m = int(input('Вветите количества строк матрицы:'))
    while n <= 0:
        n = int(input('Вветите количества стобцов матрицы:'))
    for i in range(m):
        list1.append([])
        for j in range(n):
            list1[i].append(int(input('Вветите {}-й элемент {}-й строки:'.format(j + 1, i + 1))))
    return list1


def output(t):
    for i in range(len(t)):
        print('[', end='')
        for j in range(len(t[i]) - 1):
            print('{:>3}'.format(t[i][j]), ',', end='')
        print('{:>3}'.format(t[i][j + 1]), ']')
    print('')

# a=[[1,4,1],[3,4,7],[2,1,5]]
# b=[[1,1,7],[7,4,3],[6,4,8]]
print("Вветите матрицу А:")
a = input_list()
print('\nВветите матрицу B:')
b = []
m, n = len(a), len(a[0])

for i in range(m):
    b.append([])
    for j in range(n):
        b[i].append(int(input('Вветите {}-й элемент {}-й строки:'.format(j + 1, i + 1))))


c=[]
for i in range(m):
    c.append([])
    for j in range(n):
        c[i].append(a[i][j]*b[i][j])
print('A=')
output(a)
print('B=')
output(b)
print('C=')
output(c)
v=[]
for i in range(len(c[0])):
    s=0
    for j in range(len(c)):
        s+=c[j][i]
    v.append(s)
print('Сумма все элементы в столбцах матрицы C =',v)