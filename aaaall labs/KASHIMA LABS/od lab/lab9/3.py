# Transpose a square matrix

def format_value(value):
    if type(value) == str:
        return '{:>{:}s}'.format(value, arr_print_width)
    if value is None:
        return '{:>{:}}'.format('-', arr_print_width)


arr_print_width = 12
A = []

print('Enter the values of the square matrix line by line, separated by spaces \ n '
       'Press ENTER to exit')
str_num = 1
while True:
    str_value = input(str(str_num) + '). ')
    values = str_value.split()
    if str_num > 1:
        if len(values) > len(A[0]):
            print('The entered number of elements cannot exceed the number of \
elements of the first line')
            continue
        for i in range(len(values), len(A[0])):
            values += [None]
    A += [values]
    str_num += 1
    if str_num > len(A[0]):
        break

if len(A) == 0:
    print('The matrix is empty!')
else:
    for line in A:
        arr_print_width = max(arr_print_width, max(map(len, line)))
    print('Source matrix:')
    for i in range(len(A)):
        str_value = ' '.join(map(format_value, A[i]))
        print(str_value)

    for i in range(len(A)):
        for j in range(i+1, len(A[0])):
            A[i][j], A[j][i] = A[j][i], A[i][j]

    print()
    print('The resulting matrix:')
    for i in range(len(A)):
        str_value = ' '.join(map(format_value, A[i]))
        print(str_value)
