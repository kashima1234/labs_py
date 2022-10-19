# Count in each row of matrix D the number of elements exceeding
# sums of elements of the corresponding rows of matrix Z. Place these
# quantities in array G, multiply matrix D by the maximum element
# of array G. Print matrix D before and after transformation, as well as array
# G.

import fool_check


def format_value(value):
    if type(value) in [int, float]:
        return '{:>{:}.4g}'.format(value, arr_print_width)
    if value is None:
        return '{:>{:}}'.format('-', arr_print_width)


arr_print_width = 12

D = []
Z = []

print('Enter the values of the matrix D line by line, separated by spaces \ n '
       'Press ENTER on a new line to exit')
str_num = 1
while True:
    str_value = input(str(str_num) + '). ')
    if len(str_value) == 0:
        break
    nums = list(map(fool_check.make_float, str_value.split()))
    if str_num > 1 and len(nums) != len(D[0]):
        print('The number of elements in each line must be the same')
        continue
    if any(num is None for num in nums):
        print('Input items must be numbers')
        continue
    D += [nums]
    str_num += 1

print()
print('Enter the values of the Z matrix line by line, separated by spaces \ n '
       'Press ENTER on a new line to exit')
str_num = 1
while True:
    str_value = input(str(str_num) + '). ')
    if len(str_value) == 0:
        break
    nums = list(map(fool_check.make_float, str_value.split()))
    if str_num > 1 and len(nums) != len(Z[0]):
        print('The number of elements in each line must be the same')
        continue
    if any(num is None for num in nums):
        print('Input elements must be numbers')
        continue
    Z += [nums]
    str_num += 1

if len(D) == 0 or len(Z) == 0:
    print('One or more of the original matrices are empty')
else:
    print('{:^{:}}'.format('Source matrix D', (1 + arr_print_width) * len(D[0]) - 1))
    for line in D:
        str_value = ' '.join(map(format_value, line))
        print(str_value)

    # Sum the rows of matrix Z in line_sums_Z
    line_sums_Z = list(map(sum, Z))

    # Elements that are larger than the sums of the corresponding rows of the matrix Z
    G = [0]*len(D)
    max_G = float('-inf')
    for i in range(min(len(D), len(Z))):
        for j in range(len(D[0])):
            if D[i][j] > line_sums_Z[i]:
                G[i] += 1
        if max_G < G[i]:
            max_G = G[i]

    for i in range(len(D)):
        for j in range(len(D[i])):
            D[i][j] *= max_G

    print()
    print('{:^{:}}'.format('Final matrix D', (1 + arr_print_width) * len(D[0]) - 1),
          '{:>{:}}'.format('G', arr_print_width))

    for i in range(len(D)):
        str_value = ' '.join(map(format_value, D[i])) + ' ' + \
                    format_value(G[i])
        print(str_value)
