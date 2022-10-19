 # Кашима Aхмед, иу7и-13б
# Лабораторная работа №5
 
#y = (-1)**n1 / (2 * n + 1) ** 2*n + 1 

 
from math import factorial
x = float(input('Введите значение для x: '))            #,.,.,.,
eps = float(input('Введите значение для еps: '))          #Вводим значение для eps  
ite = int(input('Введите максимальное число интераций: '))#Вводим максимальное число интераций
step = int(input('Введите шаг: '))      #Вводим шаг 
summ = 1
n = 1
t = 2
iter_print = 1
r = 0
minn = 0
coeff = Pow = 0
f = 1
print('_______________________________________________________________')
print('|  N    |         t                |     summ                 |')
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





































#while True:
 #   t = ((-1)**n)*(((2*n)-1)/(factorial(2*n)))*(x**(2*n))    #Текущий элемент
  #  summa += t                                               #Текущая сумма

   # if iter_control == n:
    #    if abs(t) > 1e+4:
     #       print("|{:^16}|{:^16.3e}|{:^16.3e}|".format(n + 1  , t, summa))
      #  else:
       #     print("|{:^16}|{:^16.3e}|{:^16}|".format(n + 1  , t, summa))
        #iter_control += step
   # n += 1
    #if n > iterations:
     #   print(div)
      #  print('Последовательность не сходилась за {} итерацию.'.format(iterations))
       # break
