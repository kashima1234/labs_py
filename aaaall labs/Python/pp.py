import math
 
def F(x):
    return (x-3)**2
 
a = float(input('Введите нижний предел интегрирования: '))
while a < 0:
   a = float(input('Введите нижний предел интегрирования: '))
b = float(input('Введите верхний предел интегрирования: '))
while b < 0:
    b = float(input('Введите верхний предел интегрирования: '))
n = int(input('Введите количество интервалов-разбиений для подсчета интеграла (В первый раз): '))
m = int(input('Введите количество интервалов-разбиений для подсчета интеграла (В второй раз): '))
eps = float(input('Введите значение для eps: '))
while eps >0.1:
    eps = float(input('Введите значение для eps: '))
#Метод правых прямоугольников
dx=(b-a)/n
prev=0.0
for i in range(1,n+1):
    prev+=F(a+i*dx)
prev*=dx
while(True):
    n*=2
    dx=(b-a)/n
    curr=0.0
    for i in range(1,n+1):
        curr+=F(a+i*dx)
    curr*=dx
    if math.fabs(curr-prev)<=eps:
        print("integral="+str(curr))
        break
    prev=curr
print(prev)
