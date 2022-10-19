#Панте Пискунов. Лабораторная работа №5
#y = ((-1)**n)*(((2*n)-1)/(factorial(2*n)))*(x**(2*n))


from math import factorial
x = int(input('Введите значение для x: '))
eps = float(input('Введите значение для еps: '))       #Вводим значение для eps
while eps > 0.1:
    eps = float(input('Введите значение для еps: '))
iterations = int(input('Введите максимальное число интераций: '))  #Вводим максимальное число интераций
while iterations <= 0:
    iterations = int(input('Введите максимальное число интераций: '))    
step = int(input('Введите шаг: '))                         #Вводим шаг 
div = " ----------------" * 3
print(div)
print("|{:^16}|{:^16}|{:^16}|".format("N", "t", "s"))      
print(div)
summa = 0
n = 1
t = 1
iter_control = 1
flag = 0
N = 0
while N != iterations:
    t =  (-1)**n * 1 / ((2 * n + 1 ) * x **  (2 * n + 1))    #Текущий элемент
    if abs(t) < eps:
        print('Последовательность сходилась {} итерации.'.format(N))
        flag = 1
        break
    summa += t                                                  #Текущая сумма1
    n += step
    N += 1
    if iter_control == (n - step):
        print("|{:^16} | {:^16} | {: ^16} |".format(N-1, t, summa))
        iter_control += step
    else:
        print('Неправильный вывод!')
        break
if flag == 0:
    print()
    print('Последовательность не сходилась через {} итерации.'.format(iterations))











































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
