#lab44

a = float(input('Введите начало интервала: '))
b = float(input('Введите конец интервала: '))      #Выводим начало, конец и шаг интервала
c = float(input('Введите шаг: '))
print(' -----------------------------')
print('|    x     |       f(x)       |')
ymax = a ** 7 - a ** 6 + 8 * a ** 5 - 4 * a **  4 + 6 * a ** 3 + 2 * a ** 2 - 5 * a + 1
ymin = a ** 7 - a ** 6 + 8 * a ** 5 - 4 * a **  4 + 6 * a ** 3 + 2 * a ** 2 - 5 * a + 1
i=a
while i <= b:
    y = a ** 7 - a ** 6 + 8 * a ** 5 - 4 * a **  4 + 6 * a ** 3 + 2 * a ** 2 - 5 * a + 1
    if y > ymax:
        ymax = y
    elif y < ymin:                                       #Создаем и вычисляем таблицу значения функции
        ymin = y
    print('|{: ^10.2f}|'.format(i), end='')
    if(y >= 1e4):
        print('{: ^18.4e}|'.format(y))
    else:
        print('{: ^18.4f}|'.format(y))
    i += c   
print(' -----------------------------')
y_axis = 70                                         #Выводим длину оси y
z = int(input("Введите засечек (от 4 дo 8): "))     # Выводим засечек от 4 до 8
while z < 4 or z > 8:
    z = int(input("Введите засечек (от 4 дo 8): "))
mid = (ymax-ymin)/(z-1)                         #Вычисляем среднбюю точку в графике
print(" "*8)                                    #Пробел 8
dl = int(y_axis / (z-1))                        #Вычисляем отсечки           
print(" "*8,end='')
if z < 6:
    dl -= 1
for i in range(z):
    t = ymin + i * mid                          #Выводим значения над осью OY
    if i == 0:
        print('{:.5}'.format(t),end='   ')
        if z < 6:
            print("     ",end='')
    else:
        print(('{: ^' +str(dl+1)+'.5}').format(t),end="")
print()
print(" "*9 + "|" +("-"*int(70/(z-1))+"|")*(z-1))
l = 1*(int(70/(z-1)+1)*(z-1))
i = a
polLen = ymax-ymin
while i <= b:
    print('{: ^9.3}'.format(i)+"|",end='')
    f = i ** 7 - i ** 6 + 8 * i ** 5 - 4 * i ** 4 + 6 * i ** 3 + 2 * i ** 2 - 5 * i + 1   #Выводим значения для ОХ
    pr = int(l*(f-ymin)/polLen)
    if ymin*ymax > 0:
        print(" "*pr + "*")           #print(' "pr + "')
    else:
        p0 = int(l*(0-ymin)/polLen)
        if p0 < pr:
            print(" "(p0) + "|" + " "(pr-p0-2) + "*")
        if p0 == pr:
            if f == 0:                                    #Рисуем график
                print(" "*(p0)+"+")
                print('Эту функцию сечет график в '.format(p0))
            elif f > 0:
                print(" "(p0)+"|")
            else:
                print(" " * (p0 - 1) + "*|")
        if p0 > pr:
            print(" "(pr) + "" + " "*(p0-pr-1) + "|")
    i += c