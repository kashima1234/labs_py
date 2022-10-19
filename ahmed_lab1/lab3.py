#Ахмед Кашима   ИУ7-13Б 
#Лабораторная работа №3

from math import sqrt, fabs, e                                 # Используем библиотеку math
print('Введите координаты первой вершины треугольника: ')  # Displaying the coordinates of the vertices of the triangle
x1, y1 = map(int, input().split())
print('Введите координаты второй вершины треугольника: ')
x2, y2 = map(int, input().split())
print('Введите координаты третьей вершины треугольника: ')
x3, y3 = map(int, input().split())
AB = sqrt((x2-x1)**2+(y2-y1)**2)                                         # Count the length of AB
BC= sqrt((x3-x2)**2+(y3-y2)**2)                                         # Count the length of BC
AC = sqrt((x3-x1)**2+(y3-y1)**2)                                         # Count the length of AB
if fabs(AB+BC-AC) <= 1e-8 or fabs(AB+AC-BC) <= 1e-8 or fabs(BC+AC-AB) <= 1e-8:  # 1e-8==10-8
    # AB+BC==AC or AB+AC==BC or BC + AC== AB
    print ('Это не треугольник!')
    
else:
    print('Длина стороны AB= {:.7}'.format(AB))            # print the length of the side  AB
    print('Длина стороны BC= {:.7}'.format(BC))            # print the length of the side  BC
    print('Длина стороны AC= {:.7}'.format(AC))            # print the length of the side  AC

    if AB * AB + BC * BC > AC * AC or BC * BC + AC * AC > AB * AB or AB * AB + AC * AC > BC * BC:
        print('Заданный треугольник является тупоугольнным треугольником.')
    else:
        print('Заданный треугольник не является тупоугольнным треугольником.')
    height = 0
    p = (AB + BC + AC) / 2

    if BC <= AB and BC <= AC:
        height = (2 * sqrt(p * (p - AB) * (p - BC) * (p - AC))) / BC             # Looking for the height from the smallest angele
    elif AC <= AB and AC <= BC:
        height = (2 * sqrt(p * (p - AB) * (p - BC) * (p - AC))) / AC
    elif AB <= AC and AB <= BC:
        height = (2 * sqrt(p * (p - AB) * (p - BC) * (p - AC))) / AB
    print('Высота из наименьшего угла треугольника= {:.7}'.format(height))   #Printing the height from the smallest corner of the triangle
    print('Введите координаты произвльной точки треугольника:')  # Displaying the coordinates of an arbitrary point
    x, y = map(int, input().split())
    s = 1/2*abs((x3-x1)*(y2-y1)-(y3-y1)*(x2-x1))  # Calculate the area of the  ABC
    s1 = 1/2*abs((x-x1)*(y2-y1)-(y-y1)*(x2-x1))   # Calculate the area of the ABD
    s2 = 1/2*abs((x-x3)*(y2-y3)-(y-y3)*(x2-x3))   # Calculate the area of the BCD
    s3 = 1/2*abs((x-x1)*(y3-y1)-(y-y1)*(x3-x1))   # Calculate the area of the ACD
    if fabs(s - s1 - s2 - s3) > 1e-8:                          # Looking for whether the entered arbitrary point in the triangle or not
        print('Точка S не находится внутри треугольника.')   
    else:
        print ('Точка S  находится внутри треугольника.')
        DAB = 2*s1 / AB                   # Calculate the distance from the point to the aircraft  АВ
        DBC = 2*s2 / BC                 # Calculate the distance from the point to the aircraft  ВС
        DAC = 2*s3 / AC                 # Calculate the distance from the point to the aircraft  АС#Ахмед Кашима   ИУ7-13Б 
#Лабораторная работа №3

from math import sqrt, fabs, e                                 # Используем библиотеку math
print('Введите координаты первой вершины треугольника: ')  # Displaying the coordinates of the vertices of the triangle
x1, y1 = map(int, input().split())
print('Введите координаты второй вершины треугольника: ')
x2, y2 = map(int, input().split())
print('Введите координаты третьей вершины треугольника: ')
x3, y3 = map(int, input().split())
AB = sqrt((x2-x1)**2+(y2-y1)**2)                                         # Count the length of AB
BC= sqrt((x3-x2)**2+(y3-y2)**2)                                         # Count the length of BC
AC = sqrt((x3-x1)**2+(y3-y1)**2)                                         # Count the length of AB
if fabs(AB+BC-AC) <= 1e-8 or fabs(AB+AC-BC) <= 1e-8 or fabs(BC+AC-AB) <= 1e-8:  # 1e-8==10-8
    # AB+BC==AC or AB+AC==BC or BC + AC== AB
    print ('Это не треугольник!')
    
else:
    print('Длина стороны AB= {:.7}'.format(AB))            # print the length of the side  AB
    print('Длина стороны BC= {:.7}'.format(BC))            # print the length of the side  BC
    print('Длина стороны AC= {:.7}'.format(AC))            # print the length of the side  AC

    if AB * AB + BC * BC > AC * AC or BC * BC + AC * AC > AB * AB or AB * AB + AC * AC > BC * BC:
        print('Заданный треугольник является тупоугольнным треугольником.')
    else:
        print('Заданный треугольник не является тупоугольнным треугольником.')
    height = 0
    p = (AB + BC + AC) / 2

    if BC <= AB and BC <= AC:
        height = (2 * sqrt(p * (p - AB) * (p - BC) * (p - AC))) / BC             # Looking for the height from the smallest angele
    elif AC <= AB and AC <= BC:
        height = (2 * sqrt(p * (p - AB) * (p - BC) * (p - AC))) / AC
    elif AB <= AC and AB <= BC:
        height = (2 * sqrt(p * (p - AB) * (p - BC) * (p - AC))) / AB
    print('Высота из наименьшего угла треугольника= {:.7}'.format(height))   #Printing the height from the smallest corner of the triangle
    print('Введите координаты произвльной точки треугольника:')  # Displaying the coordinates of an arbitrary point
    x, y = map(int, input().split())
    s = 1/2*abs((x3-x1)*(y2-y1)-(y3-y1)*(x2-x1))  # Calculate the area of the  ABC
    s1 = 1/2*abs((x-x1)*(y2-y1)-(y-y1)*(x2-x1))   # Calculate the area of the ABD
    s2 = 1/2*abs((x-x3)*(y2-y3)-(y-y3)*(x2-x3))   # Calculate the area of the BCD
    s3 = 1/2*abs((x-x1)*(y3-y1)-(y-y1)*(x3-x1))   # Calculate the area of the ACD
    if fabs(s - s1 - s2 - s3) > 1e-8:                          # Looking for whether the entered arbitrary point in the triangle or not
        print('Точка S не находится внутри треугольника.')   
    else:
        print ('Точка S  находится внутри треугольника.')
        DAB = 2*s1 / AB                   # Calculate the distance from the point to the aircraft  АВ
        DBC = 2*s2 / BC                 # Calculate the distance from the point to the aircraft  ВС
        DAC = 2*s3 / AC                 # Calculate the distance from the point to the aircraft  АС
        print('Расстояние от точки S до ближайшей стороны: {:g}'.format(min(min(DAB, DAC), DAB)))