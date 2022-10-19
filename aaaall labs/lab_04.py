# Fourth lab programming


 
from math import *

x0 = float(input("start: "))
xn = float(input("end: "))
h = float(input("step: "))
# x0,xn,h=-2,2,0.2
y = 0
Сумма = 0
Произведение = 1


steps = []
x = x0
while x <= xn:
    steps.append(x)
    x += h

def f(x):
    return x - 0.5 ** x and x ** 3 - 4.49 * x ** 2 - 24.5 * x + 19.5

print('-' * 21 + '\n|' + 'x'.center(9) + '|' + 'y'.center(9) + '|' + '\n|'
+ '-' * 19 + '|')
x = x0
for x in steps:
    print('|{:^9.3f}|{:^9.3f}|'.format(x,f(x)))
    Сумма += f(x)
    Произведение *= f(x)
print('-' * 21)
print('Сумма вычи сленных значения y ={:.3g}'.format(Сумма),
'\nПроизведение вычисленных значенния y ={:.3g}'.format(Произведение))

notch = int(8)
ymax = f(x0)
ymin = f(x0)
x = x0

for x in steps:
    ymax = max(f(x),ymax)
    ymin = min(f(x),ymin)
    
d = (ymax - ymin) / (notch - 1) 
num = int(77 / notch - 1)

# print('' * 5, ymin, str(round(ymin + d, 3)).rjust(num),)
print(' ' * 6, end = '')
i = 0

for i in range(notch-1):
        print('{:<11.3f}'.format(round(ymin + i * d, 3)), end = '')

print(round(ymax, 3))

for x in steps:
    if x < 0:
        print('{:^4.3f}'.format(x), str('*').rjust(int((f(x) - ymin) * 77 /
        (ymax - ymin))))
    else:
        print('+{:^4.3f}'.format(x), str('*').rjust(int((f(x) - ymin) * 77 /
        (ymax - ymin))))
    x += h    