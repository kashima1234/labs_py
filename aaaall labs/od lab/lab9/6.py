# A matrix D and an array I are given, containing the numbers of the rows for which
# you need to define the maximum element. Maximum values
# of elements to remember in the array R. Determine the arithmetic mean
# calculated maximum values. Print matrix D, arrays I and R,
# arithmetic mean.

import fool_check


def update_arr_print_width(line):
    global arr_print_width
    for element in line:
        if type(element) == str:
            arr_print_width = max(arr_print_width, len(element))


def get_max(arr):
    max_num = None
    for element in arr:
        tmp_num = numchecker.make_integer(element)
        if tmp_num is not None:
            if max_num is None:
                max_num = tmp_num
            if max_num < tmp_num:
                max_num = tmp_num
    return max_num


def format_value(value):
    if type(value) == str:
        return '{:>{:}s}'.format(value, arr_print_width)
    if type(value) in [int, float]:
        return '{:>{:}.4g}'.format(value, arr_print_width)
    if value is None:
        return '{:>{:}}'.format('-', arr_print_width)


arr_print_width = 12


def program_six():
    global arr_print_width
    D = []
    I = []
    print('Enter the values of the matrix D line by line, separated by spaces \ n '
           'Press ENTER on a new line to exit')
    str_num = 1
    while True:
        str_value = input(str(str_num) + '). ')
        if len(str_value) == 0:
            break
        values = str_value.split()
        if str_num > 1:
            if len(values) > len(D[0]):
                print('The entered number of elements cannot exceed the number of \
elements of the first line')
                continue
            for i in range(len(values), len(D[0])):
                values += [None]
        D += [values]
        str_num += 1

    if len(D) == 0:
        print('Matrix D is empty!')
        return

    while True:
        str_value = input('Enter the line indices on a single line, separated by spaces: ')
        if len(str_value) == 0 or len(str_value.split()) == 0:
            print('Empty string entered!')
            continue
        nums = list(map(numchecker.make_integer, str_value.split()))
        if any(num is None for num in nums):
            print('Values entered must be integers!')
            continue
        if any(num >= len(D) or num < 0 for num in nums):
            print('The lines with the entered indices must exist!')
            continue
        I = nums
        break

    R = []
    cnt = 0
    tmp_sum = 0
    for i in range(len(I)):
        R += [get_max(D[I[i]])]
        if R[i] is not None:
            tmp_sum += R[i]
            cnt += 1
    average = tmp_sum / cnt

    for line in D:
        update_arr_print_width(line)

    print()
    print('{:^{:}}'.format('Matrix D', (1 + arr_print_width) * len(D[0]) - 1),
          '{:>{:}}'.format('R', arr_print_width),
          '{:>{:}}'.format('I', arr_print_width))
    for i in range(max(len(D), len(I))):
        values = [['']*len(D[0]), '', '']
        for j, matrix in enumerate([D, R, I]):
            if i < len(matrix):
                values[j] = matrix[i]
        str_value = ' '.join(map(format_value, values[0])) + ' ' + \
                    format_value(values[1]) + ' ' + format_value(values[2])
        print(str_value)
    print('The arithmetic mean of the calculated maximum values:', average)


if __name__ == '__main__':
    program_six()
