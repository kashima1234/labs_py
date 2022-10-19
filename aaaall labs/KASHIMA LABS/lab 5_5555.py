 # Кашима Aхмед, иу7и-13б
# Лабораторная работа №5
 

 
from math import factorial 
x = float(input('Введите значение для x: '))            #,.,.,.,
eps = float(input('Введите значение для еps: '))          #Вводим значение для eps  
ite = int(input('Введите максимальное число интераций: '))#Вводим максимальное число интераций
step = float(input('Введите шаг: '))      #Вводим шаг 

summ = 0
mult = t = n = 1
print('_______________________________________________________________')
print('|  N    |         t                |     summ                 |')
print('---------------------------------------------------------------')
while n != (ite +1):
    upp_t = 1 if n & 1 else -1
    dow_t = mult * pow(x, mult)
    t = upp_t / dow_t
    summ += t
    
    print("|{}      | {: ^18.7}       | {: ^18.7}       |".format(n, t ,summ))
    n += 1
    mult += 2


if n > 1:
    print("Сумма бесконечного ряда = {:.4f}, вычислена за {} итераций.".format(summ, n - 1))
else:
    print("сумма ряда больше eps")
























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
