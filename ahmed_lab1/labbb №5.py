#Панте Пискунов. Лабораторная работа №5
#y = ((-1)**n)*(((2*n)-1)/(factorial(2*n)))*(x**(2*n))


from math import factorial
x = int(input('Введите значение для x: '))
#while x > 1 or x < 1 :
    #x = int(input('Введите значение для x: '))

eps = float(input('Введите значение для еps: '))       #Вводим значение для eps
#while eps > 0.1:
   # eps = float(input('Введите значение для еps: '))

ite = int(input('Введите максимальное число интераций: '))  #Вводим максимальное число интераций
#while iterations < 10 or iterations > 10 :
#    iterations = int(input('Введите максимальное число интераций: ')) 

step = int(input('Введите шаг: '))  
#while step > 2 or step < 2 :   
    # step = int(input('Введите шаг: '))   # Вводим шаг 
                                                 
div = " ----------------" * 3
print(div)
print("|{:^16}|{:^16}|{:^16}|".format("N", "t", "s"))      
print(div)

summ = 0
mult = t = n = 1
summa = 0
n = 1
t = 1
iter_control = 1
flag = 0
N = 0
while n != (ite +1):
    upp_t = 1 if n & 1 else -1
    dow_t = mult * pow(x, mult)
    t = upp_t / dow_t
    summ += t
    
#N != iterations:
   # t =  (-1)**n * 1 / ((2 * n + 1 ) * x **  (2 * n + 1))    #Текущий элемент
    if abs(t) < eps:
        print('Последовательность сходилась {} итерации.'.format(N))
        flag = 1
        break
    summa += t                                                  #Текущая сумма
    n += step
    N += 1
    if iter_control == (n - step):
        #print("|{:^16} | {:^16} | {: ^16} |".format(N-1, t, summa))
        print("|{}      | {: ^18.7}       | {: ^18.7}       |".format(n, t ,summ))
    n += 1
    mult += 2
    iter_control += step
else:
    print('Неправильный вывод!')
    break
if flag == 0:
      print()
    print('Последовательность не сходилась через {} итерации.'.format(iter))











































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


 