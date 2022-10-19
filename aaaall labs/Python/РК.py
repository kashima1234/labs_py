n = list(map(int,input('Введите количество строк и столбцов: ')))
a = []
for i in range(n):
    row = input('Введите вид строки:')
    a.append(row)
c = []
for i in range (0,n):
    l=[]
    for j in range(0,n):
        l.append('+')
    c.append(l)
for i in range (0,n):
    for j in range(0,len(a[i])):
        if a[i][j] =='.':
            c[i][j] == '.'
            c[-i-1][-j-1] ='.'
            c[j][i] ='.'
            c[-j-1][-i-1] ='.'




t = 1
summa = 0
iter_control = 1
print(' ------------------------------------------------------')
print('|    n      |       t              |       s           |')
while abs(t) > eps:
    for i in range(0,iterations):
        t = ((-1)**i)*(((pi/3)**(2*i+1))/(factorial(2*i+1)))
        summa += t
        if iter_control == i:
            print('|{:^16}|{:^16.3e}|{:^16.3e}|'.format(i,t,summa))
        else:
            print('|{:^16}|{:^16}|{:^16}|'.format(i, t, summa))
            iter_control += step
        if i > iterations:
            print('последовательность не сходилась за {} итерацию.'.format(N))
            break
        t = ((-1)**i)*(((pi/3)**(2*i+1))/(factorial(2*i+1)))
        summa += t
print(' -----------------------------')

