#Панте Пискунов. Лабораторная работа №5
from math import pi, factorial
x = int(input('Введите значение для x: '))
eps = float(input('Введите значение для еps: '))       #Вводим значение для eps
while eps > 0.1:
    eps = float(input('Введите значение для еps: '))
iterations = int(input('Введите максимальное число интераций: '))  #Вводим максимальное число интераций
while iterations <= 0:
    iterations = int(input('Введите максимальное число интераций: '))    
step = int(input('Введите шаг: '))                         #Вводим шаг 
#n = 0
#t = ((-1)**n)*(((pi/3)**(2*n+1))/(factorial(2*n+1)))
t = 1
summa = 0
iter_control = 1
print(' ------------------------------------------------------')
print('|    n      |       t              |       s           |')
while abs(t) > eps:
    for i in range(0,iterations):
        if i > iterations:
            print('последовательность не сходилась за {} итерацию.'.format(N))
            break
        t = ((-1)**i)*((2*i-1)/(factorial(2*i)))*x**(2*i)
        summa += t
        if iter_control == i:
            print('|{:^11}| {:^17.3e}  |{:^20.3e}|'.format(i+1,t,summa))
            iter_control += step
        
print(' -----------------------------')

