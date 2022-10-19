from math import *


def f(x):
    a = x ** 2  # 3 * x ** 2 - 4 * x + 10
    return a


def F(x):
    a = x ** 3 / 3  # - 2 * x ** 2 + 10 * x + 100
    return a


def jif(a, b):
    return abs(F(b) - F(a))


def method_трапеций(n1, n2, a, b):
    d1 = (b - a) / n1
    d2 = (b - a) / n2
    s1 = s2 = 0
    for i in range(n1):
        s1 += d1 / 2 * (f(d1 * i) + f(d1 * i + d1))
    for j in range(n2):
        s2 += d2 / 2 * (f(d2 * j) + f(d2 * j + d2))
    return [s1, s2]


def method_тревосмых(n1, n2, a, b):
    d1 = (b - a) / n1
    d2 = (b - a) / n2
    s1 = s2 = 0
    for i in range(1,n1+1):
        s1 += d1 * (f(a + d1 * (i - 1)) + 3 * f((2 * (a + d1 * (i - 1)) + a + d1 * i) / 3) + 3 * f(
            (a + d1 * (i - 1) + (a + d1 * i) * 2) / 3) + f(a + d1 * i)) / 8
    for j in range(1,n2+1):
        s2 += d2 * (f(a + d2 * (j - 1)) + 3 * f((2 * (a + d2 * (j - 1)) + a + d2 * j) / 3) + 3 * f(
            (a + d2 * (j - 1) + (a + d2 * j) * 2) / 3) + f(a + d2 * j)) / 8
    return (s1, s2)


def wuc(itg, method):
    abs_err1, abs_err2 = abs(method[0] - itg), abs(method[1] - itg)
    rel_err1, rel_err2 = abs_err1 / itg, abs_err2 / itg
    errors1 = [abs_err1, rel_err1]
    errors2 = [abs_err2, rel_err2]
    # errors1.extend([abs_err1,rel_err1])
    # errors2.extend([abs_err2,rel_err2])
    return errors1, errors2


def input_control():
    s1 = s2 = 0
    try:
        # while s1 <= 0:
        #     s1 = float(input(f"Шаг 1  разбиения для численного интегрирования: "))
        # while s2 <= 0 or s2 == s1:
        #     s2 = float(input(f"Шаг 2  разбиения для численного интегрирования: "))
        
        start = float(input(f"Начальное значение: "))
        end = start
        while end <= start:
            end = float(input(f"Конечное значение: "))
        # n1 = int((end - start) / s1)
        # n2 = int((end - start) / s2)
        n1 = n2 = 0
        while n1 <= 0 or n2 <= 0 or n1 == n2:
            n1 = int(input('n1='))
            n2 = int(input('n2='))
    except:
        print('Error')
        return (input_control())
    return n1, n2, start, end


n1, n2, start, end = input_control()
method1 = method_трапеций(n1, n2, start, end)
method2 = method_тревосмых(n1, n2, start, end)
print('-' * 55, '\n|{:^10}|{:^20}|{:^20}|'.format('', n1, n2))
print('|{:^10}|{:^20.4f}|{:^20.4f}|'.format('Метод 1', method1[0], method1[1]))
print('|{:^10}|{:^20}|{:^20}|\n'.format('Метод 2', round(method2[0], 4) if n1 % 3 == 0 else 'не можно',
                                        round(method2[1], 4) if n2 % 3 == 0 else 'не можно'))

# абсолютную и относительную погрешности измерения

itg = jif(start, end)
print('itg=', itg)
error_method1_n1, error_method1_n2 = wuc(itg, method1)
error_method2_n1, error_method2_n2 = wuc(itg, method2)
print('-' * 84, '\n|{:^40}|{:^20}|{:^20}|'.format('', n1, n2))
print(
    '|{:^40}|{:^20.4f}|{:^20.4f}|'.format('Абсолютная погрешность Методом 1', error_method1_n1[0],
                                          error_method1_n2[0]))
print('|{:^40}|{:^20.3%}|{:^20.3%}|'.format('относительнная погрешность Методом 1', error_method1_n1[1],
                                            error_method1_n2[1]))
print(
    '|{:^40}|{:^20}|{:^20}|'.format('Абсолютная погрешность Методом 2',
                                    str(round(error_method2_n1[0], 4)) if n1 % 3 == 0 else 'не можно',
                                    str(round(error_method2_n2[0], 4)) if n2 % 3 == 0 else 'не можно'))
print('|{:^40}|{:^20}|{:^20}|'.format('относительнная погрешность Методом 2',
                                      str(round(error_method2_n1[1], 4) * 100) + '%' if n1 % 3 == 0 else 'не можно',
                                      str(round(error_method2_n2[1], 4) * 100) + '%' if n2 % 3 == 0 else 'не можно'))

if abs(error_method1_n1[0]) >= abs(error_method2_n1[0]):
    act = method_трапеций
    print('менее точный метод: метод трапеций')
else:
    act = method_тревосмых
    print('менее точный метод: метод тревосмых')
eps = 0
while eps <= 0:
    try:
        eps = float(input('\nТочность='))
    except:
        print('Error')
n = int(1)
par = 100000
Iter = 10
changed = False
res = act(1, 2, start, end)
error_low_n, error_low_N = wuc(itg, res)
if abs(error_low_n[0] - error_low_N[0]) > eps:
    flag = 1
    while par >= 1:
        while 1:
            n += par
            N = 2 * n
            res = act(n, N, start, end)
            error_low_n, error_low_N = wuc(itg, res)
            if abs(error_low_n[0] - error_low_N[0]) <= eps:
                n -= par
                par = int(par / Iter)
                if flag % 3 == 0:
                    print('working')
                flag += 1
                break
        if par < Iter and not changed:
            par = 1
            changed = True
            continue
        elif changed:
            n += 1
            break
if act == method_тревосмых:
    while n % 3 != 0:
        n += 1
print('N={}'.format(n))
