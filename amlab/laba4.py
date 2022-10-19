 
 # corect lab 4 
 # kashima ahmed 
import math

z_first = float(input('Введите начало интервала : '))
z_last = float(input('Введите конец интервала : '))
z_step = float(input('Введите шаг  : '))
f1_min = float('inf')
f1_max = float('-inf')
z_amount = abs(math.floor((z_last - z_first)/z_step))+1

# табличка
print(36*'-')
print('|     z    ' + '|    f1    |' + '     f2     |')
print(36*'-')
function_exists = False
for i in range(z_amount):
    z = z_first + z_step*i
    if z > 0:
        f1 = z*math.log(z) + 0.125
        f1_min = min(f1,f1_min)
        point_exists = True
    else:
        f1 = '-'
        point_exists = False
    if point_exists:
        function_exists = True
        if f1 > f1_max:
            f1_max = max(f1,f1_max)
            z_max = z
    if z < 1e2:
        f2 = 3*z - math.exp(z)
        f2_inf = False
    else:
        f2_inf = True
    if point_exists and f2_inf:
        print('| {:< 8.4}'.format(z),
              '| {:< 8.2g}'.format(f1),
              '| {:^11}|'.format('inf'))
    elif point_exists:
        print('| {:< 8.4}'.format(z),
              '| {:< 8.4g}'.format(f1),
              '| {:< 11.4g}|'.format(f2))
    elif f2_inf:
        print('| {:< 8.4}'.format(z),
              '| {:^8}'.format(f1),
              '| {:^9}|'.format('inf'))
    else:
        print('| {:< 8.4}'.format(z),
              '| {:^8}'.format(f1),
              '| {:< 11.4g}|'.format(f2))
print(36*'-')

if function_exists:
    print('\nМаксимальное значение f1 равно {:.4f}'.format(f1_max))
    print('Достигается при z равном {:.4f}\n'.format(z_max))

# построение графика функции f1 = z*ln(z) + 0.125
if function_exists:
    y_marks = int(input('Введите количество засечек на оси y (от 4 до 8): '))
    if y_marks > 8 or y_marks < 4:
        print('Необходимо количество засечек от 4 до 8')
    else:
        # разница между значениями y на засечках:
        y_mark_step = (f1_max - f1_min)/(y_marks-1)

        # шаг y за один символ строки
        y_step = (f1_max - f1_min)/80

        # значение отсечки для построения оси y
        scale_value = f1_min

        # кол-во символов между отсечками
        scale_step = math.ceil(79/(y_marks-1))

        # ось y
        y_axis = 8*' ' + '{:<8.3g}'.format(scale_value)

        # построение на оси y
        for j in range(y_marks-2):
            scale_value += y_mark_step
            y_axis += ' '*(scale_step-8)
            y_axis += '{:<8.3g}'.format(scale_value)
        scale_value += y_mark_step
        y_axis += ' ' * (87 - len(y_axis))
        y_axis += '{:<8.3g}'.format(scale_value)
        print(y_axis)
        
        # построение графика
        for k in range(int(z_first*1e7), int(z_last*1e7)+1, int(z_step*1e7)):
            z = k/1e7
            if z > 0:
                f1 = z*math.log(z) + 0.125
                point_exists = True
            else:
                f1 = False
                point_exists = False
            graph_line = '{:< 7.4} |'.format(z)
            y_symbol = f1_min
            for m in range(81):
                y_symbol_next = y_symbol + y_step
                if f1 >= y_symbol and f1 < y_symbol_next and point_exists:
                    graph_line += '*'
                elif y_symbol < 0 and y_symbol_next > 0:
                    graph_line += '|'
                else:
                        graph_line += (' ')
                y_symbol += y_step
            print(graph_line)
else:
    print('График функции не лежит на данном отрезке')
