# Сумма бесконечного ряда
# y = x - x ** 2 / 2 + x ** 3 / 3 + ... + (-1) ** n-1 * x ** n / n + ...




k = float(input("Точность ="))
list1 = int(input("Шаг печати ="))
x0 = int(input('Количестве итераций ='))
s = 0
i = 1
n = 'безконечное значение'
def f(x):
    return  
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
print('Сумма бесконечного ряда={:.7f}, вычислена за {:} итераций'.format(s, i - 1))
