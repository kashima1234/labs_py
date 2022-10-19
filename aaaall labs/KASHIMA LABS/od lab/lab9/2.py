# Find the maximum value above the main diagonal and the minimum value below
# side diagonal.

import fool_check

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
    A += [[]]
    for element in values:
        checked_value = fool_check.make_float(element)
        if checked_value is None:
            A[str_num - 1] += [element]
            continue
        A[str_num - 1] += [checked_value]
    str_num += 1
    if str_num > len(A[0]):
        break
print()

min_value = float('inf')
max_value = -min_value
len_A = len(A)
if len_A > 0:
    for i in range(len_A):
        for j in range(i+1, len_A):
            if type(A[i][j]) in [int, float]:
                if max_value < A[i][j]:
                    max_value = A[i][j]

    for i in range(len_A):
        for j in range(len_A-i, len_A):
            if type(A[i][j]) in [int, float]:
                if min_value > A[i][j]:
                    min_value = A[i][j]
if len_A == 0:
    print('The matrix is empty!')
else:
    if max_value != float('-inf'):
        print('Maximum value above the main diagonal:', '{:12.4g}'.format(max_value))
    else:
        print('There is no maximum value above the main diagonal')
    if min_value != float('inf'):
        print('The minimum value under the side diagonal:', '{:12.4g}'.format(min_value))
    else:
        print('There is no minimum value under the side diagonal')
