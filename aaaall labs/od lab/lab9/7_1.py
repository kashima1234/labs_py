# Given a matrix of symbols. Replace all English vowels in it with
# points.

def format_value(value):
    if type(value) == str:
        return '{:>{:}s}'.format(value, arr_print_width)
    if value is None:
        return '{:>{:}}'.format('-', arr_print_width)


arr_print_width = 12
A = []
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
# 1). line1 ahsdfashdflkjhas 0
# 2). - None
# 3). Sooooob jo1u ''
print('Enter the values of the matrix A line by line, separated by spaces '
       'Press ENTER to exit')
str_num = 1
while True:
    str_value = input(str(str_num) + '). ')
    if len(str_value) == 0:
        break
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

for i in range(len(A)):
    for j in range(len(A[i])):
        element = A[i][j]
        new_element = ''
        if element is None:
            new_element = '-'
        else:
            for char in element:
                if char in vowels:
                    new_element += '.'
                    continue
                new_element += char
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
