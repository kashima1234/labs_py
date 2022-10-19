a = float(input('Введите начало интервала: '))
b = float(input('Введите конец интервала: '))
c = float(input('Введите шаг: '))
print('-------------------------------')
print('|    x  |     y1  |      y2')
def frange(x, y, jump):
    while x < y:
        yield x
        x += jump 
for x in frange(a, b+c, c):
    y1 = x
    y2 = x*x
    print('|{:5.3g}  |  {:5.3g}  |  {:5.3g}'.format(x, y1, y2))
p = 512*x**10-1280*x**8-1120*x**6-400*x**4-5*x**2-1
print('Сумма вычисленых значении функции p = {:.4f}'. format(p))
Y = []
z = int(input('Введите количество засечек j (от 4 до 8): '))
