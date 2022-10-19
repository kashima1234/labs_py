from math import sqrt
print('Введите координаты первой вершины:')
x1, y1 = map(int,input().split())
print('Введите координаты второй вершины:')
x2, y2 = map(int,input().split())
print('Введите координаты третъей вершины:')
x3, y3 = map(int,input().split())
AB = sqrt((x2-x1)**2+(y2-y1)**2)
BC = sqrt((x3-x2)**2+(y3-y2)**2)
AC = sqrt((x3-x1)**2+(y3-y1)**2)
p = (AB+BC+AC)/2
S = sqrt(p*(p-BC)*(p-AC)*(p-AB))
if AB+BC-AC <= 1e-8 or AB+AC-BC <= 1e-8 or BC+AC-AB <= 1e-8:
    print ('Это не треугольник!')
else:
    print('Длина стороны АB= {:.7}'.format(AB))
    print('Длина стороны BC= {:.7}'.format(BC))
    print('Длина стороны AC= {:.7}'.format(AC))
    if BC < AC and BC < AB:
        ha = (2*S)/BC
        print ('Длина высоты из наименьшего угла= {:.7}'.format(ha))
    elif AC < BC and AC < AB:
        hb = (2*S)/AC
        print ('Длина высоты из наименьшего угла= {:.7}'.format(hb))
    else:
        hc = (2*S)/AB
        print('Длина высоты из наименьшего угла = {:.7}'.format(hc))
        
