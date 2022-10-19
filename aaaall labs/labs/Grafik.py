# y=x**6-2x**5+1.7x**4-4.7x**3-0.8x**2+4.26x-2


from math import *



a0 = float(input(' : '))
an = float(input('  '))       
c = float(input(': '))
a0 = -1
h = 0.1
an = 1
y = 0
Сумма = 0
Произведение = 1



def f(a):
    return  a ** 7 - a ** 6 + 8 * a ** 5 - 4 * a **  4 + 6 * a ** 3 + 2 * a ** 2 - 5 * a + 1


print('-' * 21 + '\n|' + 'a'.center(9) + '|' + 'y'.center(9) + '|' + '\n|' + '-' * 19 + '|')
a = a0
while a <= an:
    print('|{:^9.3f}|{:^9.3f}|'.format(a, f(a)))
    Сумма += f(a)
    Произведение *= f(a)
    a += c

else:
    print('-' * 21)
print('Сумма вычисленных значений у={:.3f}'.format(Сумма),
      '\nПроизведение вычисленных значений у={:.3f}'.format(Произведение))

notch = int(8)
ymax = f(a0)
ymin = f(a0)
a = a0

while a <= an:
    ymax = max(f(a), ymax)
    ymin = min(f(a), ymin)
    a += c
d = (ymax - ymin) / (notch - 1)
num = int(84 / notch - 1)

 
print(' ' * 6, end='')
i = 0
while i < (notch - 1):
    print(str(round(ymin + i * d, 3)).ljust(num), end='')
    i += 1
print(round(ymax, 3))
a = a0
while a <= an:
    print('{:>4.3f}'.format(a), str('*').rjust(int((f(a) - ymin) * 84 / (ymax - ymin))))
    a += c
