# Кашима Aхмед, иу7и-13б 
# Лабораторная работа № 5 

# Сумма бесконечного ряда
 
# y = 1/x - 1/ 3 * x **3 + 1 /  5 * x ** 5 + ... + (-1)**n1 / (2 * n + 1) ** 2*n + 1 + ...




k = float(input("Точность ="))
list1 = int(input("Шаг печати ="))
x0 = int(input('Количестве итераций ='))
s = 0
i = 1
n = 'беcконечное значение'
def f(x):
    return  1/x - 1/ 3 * x **3 + 1 / 5 * x ** 5 + ... + (-1)** n*1 / (2 * n + 1) ** 29 * n + 1 + ...

            # 31b its for -- betw.. number and t,s,. # 5its for distance betw letererrers           # make table                                                              
print('-' * 31, '\n|{:^5}|{:^11}|{:^11}|'.format('№', 't', 's'), '\n|' + '-' * 29 + '|')
while 1:
    j = 1
    for q in range(1, i):
        j *= q
    t = 1 / j
    if t >= k:
        s += t
        if i <= x0 and (i - 1) % list1 == 0:
            print('|{:^5}|{:^11.4f}|{:^11.4f}|'.format(i, t, s))
        i += 1
    else:
        break

print('-' * 31)
print('Сумма бесконечного ряда={:.7g}, вычислена за {:} итераций'.format(s, i - 1))
