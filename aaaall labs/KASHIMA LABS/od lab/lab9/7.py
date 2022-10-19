# Given a matrix of symbols. Replace all English vowels in it with
# points.
def update_arr_print_width(line):
    global arr_print_width
    for element in line:
        if type(element) == str:
            arr_print_width = max(arr_print_width, len(element))


def format_value(value):
    if type(value) == str:
        return '{:>{:}s}'.format(value, arr_print_width)
    if value is None:
        return '{:>{:}}'.format('-', arr_print_width)


arr_print_width = 12
A = []
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

print('Enter the values of the matrix A line by line, separated by spaces \ n '
       'Press ENTER to exit')
str_num = 1
while True:
    str_value = input(str(str_num) + '). ')
    if len(str_value) == 0:
        break
    values = []
    for i in range(len(str_value) // 2):
        ch = str_value[i * 2]
        values.append(ch)

    if str_num > 1:
        if len(values) > len(A[0]):
            print('The entered number of elements cannot exceed the number of \
elements of the first line')
            continue
        for i in range(len(values), len(A[0])):
            values += [None]
    if any(value is not None and len(value) != 1 for value in values):
        print('Input values must be characters!')
        continue
    A += [values]
    str_num += 1

for i in range(len(A)):
    for j in range(len(A[0])):
        element = A[i][j]
        new_element = element
        if element is None:
            new_element = '-'
        elif element in vowels:
            new_element = '.'
        A[i][j] = new_element

if len(A) == 0:
    print('The original matrix is empty!')
else:
    for line in A:
        arr_print_width = max(arr_print_width, max(map(len, line)))
    print()
    print('{:^{:}}'.format('Final matrix A', (1 + arr_print_width) * len(A[0]) - 1))
    for line in A:
        str_value = ' '.join(map(format_value, line))
        print(str_value)
