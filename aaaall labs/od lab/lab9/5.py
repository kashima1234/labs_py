# Подсчитать в каждой строке матрицы D количество элементов, превышающих
# суммы элементов соответствующих строк матрицы Z. Разместить эти
# количества в массиве G, умножить матрицу D на максимальный элемент
# массива G. Напечатать матрицу D до и после преобразования, а также массив
# G.

import numchecker


def format_value(value):
    if type(value) == str:
        return '{:>{:}s}'.format(value, arr_print_width)
    if type(value) in [int, float]:
        return '{:>{:}.4g}'.format(value, arr_print_width)
    if value is None:
        return '{:>{:}}'.format('-', arr_print_width)


arr_print_width = 12

D = []
Z = []
print('Построчно вводите значения матрицы D через пробелы\n'
      'Для выхода нажмите ENTER')
str_num = 1
while True:
    str_value = input(str(str_num) + '). ')
    if len(str_value) == 0:
        break
    nums = list(map(numchecker.make_float, str_value.split()))
    if str_num > 1:
        if len(nums) > len(D[0]):
            print('Вводимое количество элементов не может превышать количества \
элементов первой строки')
            continue
        for i in range(len(nums), len(D[0])):
            nums += [None]
    D += [nums]
    str_num += 1

print()
print('Построчно вводите значения матрицы Z через пробелы\n'
      'Для выхода нажмите ENTER')
str_num = 1
while True:
    str_value = input(str(str_num) + '). ')
    if len(str_value) == 0:
        break
    nums = list(map(numchecker.make_float, str_value.split()))
    if str_num > 1:
        if len(nums) > len(Z[0]):
            print('Вводимое количество элементов не может превышать количества \
элементов первой строки')
            continue
        for i in range(len(nums), len(Z[0])):
            nums += [None]
    Z += [nums]
    str_num += 1
    if str_num > len(D[0]):
        break


if len(D) == 0:
    print('Исходная матрица пуста')
else:
    for line in D:
        arr_print_width = max(arr_print_width, max(map(lambda x: len(str(x)), line)))
    print('{:^{:}}'.format('Исходная матрица D', (1 + arr_print_width) * len(D[0]) - 1))
    for line in D:
        str_value = ' '.join(map(format_value, line))
        print(str_value)

    # Суммируем строки матрицы Z в line_sums_Z
    line_sums_Z = []
    for i in range(len(Z)):
        tmp_sum = None
        for element in Z[i]:
            if type(element) in [int, float]:
                if tmp_sum is None:
                    tmp_sum = 0
                tmp_sum += element
        line_sums_Z += [tmp_sum]

    # Ищем элементы, большие сумм соответсвующих строк матрицы Z
    G = [None]*len(D)
    max_G = float('-inf')
    for i in range(min(len(D), len(line_sums_Z))):
        for j in range(len(D[0])):
            if type(D[i][j]) in [int, float] \
                    and type(line_sums_Z[i]) in [int, float]:
                if G[i] is None:
                    G[i] = 0
                if D[i][j] > line_sums_Z[i]:
                    G[i] += 1
        if type(G[i]) in [int, float] and max_G < G[i]:
            max_G = G[i]

    for i in range(len(D)):
        for j in range(len(D[i])):
            if type(D[i][j]) in [int, float] and max_G != float('-inf'):
                D[i][j] *= max_G

    print()
    print('{:^{:}}'.format('Итоговая матрица D', (1 + arr_print_width) * len(D[0]) - 1),
          '{:>{:}}'.format('G', arr_print_width))

    for i in range(len(D)):
        str_value = ' '.join(map(format_value, D[i])) + ' ' + \
                    format_value(G[i])
        print(str_value)
