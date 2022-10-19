# Determine the arithmetic mean of the positive numbers of each line
# matrixes and the number of elements less than the arithmetic mean.
# Write the results to the arrays AV and L, respectively. Print the matrix A to
# in the form of a matrix and next to the columns AV and L.

import math
import fool_check


def format_value(value):
    if type(value) == str:
        return '{:>{:}s}'.format(value, arr_print_width)
    if type(value) in [int, float]:
        return '{:>{:}.4g}'.format(value, arr_print_width)
    if value is None:
        return '{:>{:}}'.format('-', arr_print_width)


arr_print_width = 12
A = []
D = []
F = []
AV = []
L = []

str_value = input('Enter the values of array D separated by spaces: ')
for element in str_value.split():
    num = fool_check.make_float(element)
    if element is None:
        D += [element]
    else:
        D += [num]

str_value = input('Enter the values of the array F, separated by spaces: ')
for element in str_value.split():
    num = fool_check.make_float(element)
    if element is None:
        F += [element]
    else:
        F += [num]

# Define array A
for i in range(len(D)):
    A += [[]]
    for j in range(len(F)):
        element = None
        if type(D[i]) in [int, float] and type(F[j]) in [int, float]:
            element = math.sin(D[i] + F[j])
        A[i] += [element]

# Looking for arithmetic means (define an AV array)
for i in range(len(D)):
    average = None
    counter = 0
    tmp_sum = 0
    for j in range(len(F)):
        element = A[i][j]
        if type(element) in [int, float] and element > 0:
            tmp_sum += element
            counter += 1
    if counter > 0:
        average = tmp_sum/counter
    AV += [average]

# Define an array L
for i in range(len(A)):
    less_counter = None
    if AV[i] is not None:
        less_counter = 0
        for element in (A[i]):
            if type(element) in [int, float] and element < AV[i]:
                less_counter += 1
    L += [less_counter]

print()
if len(A) == 0:
    print('The matrix is empty!')
else:
    print('{:^{:}}'.format('MATRIX', (1 + arr_print_width)*len(A[0]) - 1),
          '{:>{:}}'.format('AV', arr_print_width),
          '{:>{:}}'.format('L', arr_print_width))

    for i in range(len(A)):
        str_value = ' '.join(map(format_value, A[i])) + ' ' + \
                    format_value(AV[i]) + ' ' + format_value(L[i])
        print(str_value)

    
