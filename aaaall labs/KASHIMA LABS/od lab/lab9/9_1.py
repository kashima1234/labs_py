# Enter a three-dimensional array (array of matrices of size X * Y * Z), output the i-th
# slice at the second index.

import numchecker


def update_arr_print_width(line):
    global arr_print_width
    for element in line:
        if type(element) == str:
            arr_print_width = max(arr_print_width, len(element))


def format_value(value):
    if type(value) == str:
        return '{:>{:}s}'.format(value, arr_print_width)
    if type(value) in [int, float]:
        return '{:>{:}.4g}'.format(value, arr_print_width)
    if value is None:
        return '{:>{:}}'.format('-', arr_print_width)


arr_print_width = 12
A = []

print('Third array input')
print('To exit press ENTER on the first line of the new matrix')
slice_idx = 0
while True:
    print()
    print('Input ', slice_idx + 1, 'layer', sep='')
    print('Line by line enter matrix values separated by spaces')
    str_idx = 0
    while True:
        str_value = input(str(str_idx + 1) + '). ')
        if (str_idx == 0 or slice_idx == 0) and len(str_value) == 0:
            break
        if (str_idx > 0 or slice_idx > 0) and len(str_value.split()) != len(A[0][0]):
            print('The number of elements in the row of each of the matrices must be the same')
            continue
        if str_idx == 0:
            A += [[]]
        A[slice_idx] += [str_value.split()]
        str_idx += 1
        if slice_idx > 0 and str_idx == len(A[0]):
            break
    if str_idx == 0 and len(str_value) == 0 or slice_idx == 0 and len(A) == 0:
        break
    slice_idx += 1

if len(A) > 0:
    while True:
        str_value = input('Enter the index of the slice: ')
        line_slice_idx = numchecker.make_integer(str_value)
        if line_slice_idx is None:
            print('The entered value must be an integer!!')
        elif line_slice_idx >= len(A):
            print('The index entered exceeds the index of the last slice')
        else:
            break

print()
if len(A) == 0:
    print('The array is empty')
else:
    for line in A:
        update_arr_print_width(line)

    print(line_slice_idx + 1, 'th slice at the second index:', sep='')
    for i in range(len(A)):
        str_value = ' '.join(map(format_value, A[i][line_slice_idx]))
        print(str_value)
    print()
