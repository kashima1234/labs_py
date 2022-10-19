#Панте Пискунов. Лабораторная работа №5
#y = ((-1)**n)*(((2*n)-1)/(factorial(2*n)))*(x**(2*n))
from math import factorial
x = float(input('Введите значение для x: '))            #,.,.,.,
eps = float(input('Введите значение для еps: '))          #Вводим значение для eps  
ite = int(input('Введите максимальное число интераций: '))#Вводим максимальное число интераций
step = int(input('Введите шаг: '))      #Вводим шаг 
summ = 1
n = 1
t = 1
iter_print = 1
r = 0
minn = 0
coeff = Pow = 0
f = 1
print('_______________________________________________________________')
print('|  N    |     t                    |     summ                 |')
print('---------------------------------------------------------------')
while n != (ite +1):
    if abs(t) < eps:
        print('the series converged in {} iteration.'.format(n-1))
        r = 1
        break
    if minn == 0:
        t = x ** Pow / factorial(coeff) * f             #Текущий элемент
        minn = 1
    elif minn ==1:
        t = -1 * x ** Pow / factorial(coeff) * f
        minn = 0
    summ += t                                       #Текущая сумма
    coeff += 2
    Pow += 2
    n += 1
    if n != 2:
        f += 2
    
    if iter_print == n-1:
        print("|{}      | {: ^18.7}       | {: ^18.7}       |".format(n-1, t ,summ))
        iter_print += step
if r == 0:
    print('the series not coverged in {} iteration.'.format(ite))
