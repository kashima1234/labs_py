#Панте Пискунов. Лабораторная работа №4
x = float(input('Введите координаты точки по x: ')) # Выводим координаты по абсцисe
y = float(input('Введите координаты точки по y: ')) #Выводим координаты по ординатe
flag = False                                        #Создаем переменую
if -9 <= x <= -1:
    if y >= (-1/8)*(x+9)**2+8 and y <= 7*(x+8)**2+1:                           #Создаем условия, при которых наша программа будет работать     
        flag = True
if -8 <= x <= -2:
    if (y >= (1/49)*(x+1)**2 and y <= (-1/8)*(x+9)**2+8) or (y >= 1/3*(x+5)**2-7 and y <= (-4/49)*(x+1)**2):
        flag = True
if -2 <= x <= 2:
    if y == 1.5*x+2 or y == -1.5*x+2:
        flag = True
if -2 <= x <= -1:
    if (y >= 1/49*(x+1)**2 and y <= (-1/8)*(x+9)**2+8) or (y >= -2*(x+1)**2-2 and y <= -4/49*(x+1)**2):
        flag = True
if -1 <= x <= 1:
    if y >= 4*x**2+2 or y == -4*x**2+2:
        flag = True
if  1 <= x <= 2:
    if (y >= 1/49*(x-1)**2 and y <= (-1/8)*(x-9)**2+8) or (y >= -2*(x-1)**2-2 and y <= -4/49*(x-1)**2):
        flag = True
if 2 <= x <= 8:
    if (y >= (1/49)*(x-1)**2 and y <= (-1/8)*(x+9)**2+8) or (y >= 1/3*(x-5)**2-7 and y <= (-4/49)*(x-1)**2):
        flag = True
if flag:                                      
    print('Точка принадлежит графику!')
else:
    print('Точка не принадлежит графику!')
                            
