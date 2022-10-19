def f(x):
    return x**2 
def Weddle1(f, a, b, n):  #Определяем первый интеграл по методу Уэддля
    h = (b - a) / n
    summa1 = 0
    if (n % 6) == 0:
        summa1 += ((3*h/10)*(f(a)+5*f(a)+f(a)+6*f(a)+f(a)+5*f(a)+f(a)))
    a += 6*h
    return a
a = 0
b = 3
n = 3
m = 6
eps = 0.001
weddle1 = Weddle1(f, a, b, n)   #Вычисляем первый интеграл по методу Уэддля
while abs(weddle1 - weddle1) > eps:
    weddle1 = weddle1(f, a, b, n)
weddle1_2 = Weddle1(f, a, b, m)  #Вычисляем второй интеграл по методу Уэддля
while abs(weddle1_2 -weddle1_2) > eps:
    weddle1_2 = Weddle1(f, a, b, m)
div = ' ----------------------------' * 3
print()
print(div)
print('|{:^28}|{:^28}|{:^28}|'.format('Метод',n,m))
print(div)
print('|{:^28}|{:^28.9f}|{:^28.9f}|'.format('Метод Уэддля',weddle1,weddle1_2))
