from math import sqrt,cos
N = int(input('Введите количество треугольников: '))
T = int(input('Введите значение для параметра T: '))
s = 0
for x in range(1,N+1):
    print()
    print(x,'-ый треугольник:')
    a = float(input('Введите длину стороны a: '))
    while a < 0:
        a = float(input('Введите длину стороны a: '))
    b = float(input('Введите длину стороны b: '))
    while b < 0 :
        b = float(input('Введите длину стороны b: '))
    beta = float(input('Введите угол треугольника: '))
    c = sqrt(a**2 + b**2 - 2 * a * b * cos(beta))
    if a < T:
        ma = sqrt(2 * b * b + 2 * c * c - a * a) / 2
        print('Медиана стороны а = ',round(ma,2))
    else:
        ma = 0
    if b < T:
        mb = sqrt(2 * a * a + 2 * c * c - b * b) / 2
        print('Медиана стороны b = ',round(mb,2))
    else:
        mb = 0
    if c < T:
        mc = sqrt(2 * a * a + 2 * b * b - c * c) / 2
        print('Медиана стороны c = ',round(mc,2))
    else:
        mc = 0
    s = ma + mc + mb
    print('Сумма медианы всех треугольников = ',round(s,2))
