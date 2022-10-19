# Form matrix C by multiplying matrices A and B row by row
# of the same dimension (elements in the i-th row of matrix A are multiplied by
# corresponding elements in the i-th row of matrix B), then add all
# elements in columns of matrix C and write them to array V.
import fool_check

arr_print_width = 12
A = []
B = []
C = []

print('Enter the values of the matrix A line by line, separated by spaces \ n '
       'Press ENTER to exit')
str_num = 1
while True:
    str_value = input(str(str_num) + '). ')
    if len(str_value) == 0:
        break
    if str_num > 1 and len(str_value.split()) != len(A[0]):
        print('The number of elements in each line must be the same!')
        continue
    nums = list(map(numchecker.make_float, str_value.split()))
    if any(num is None for num in nums):
        print('Values entered must be numbers!')
        continue
    A += [nums]
    str_num += 1

print()
print('Enter the values of the matrix B of the same dimension line by line, separated by spaces')
str_num = 1
if len(A) > 0:
    while True:
        str_value = input(str(str_num) + '). ')
        if len(str_value.split()) != len(A[0]):
            if str_num > 1:
                print('The number of elements in each line must be the same!')
            else:
                print('The number of elements in a row for both matrices must \
    be the same')
            continue
        nums = list(map(numchecker.make_float, str_value.split()))
        if any(num is None for num in nums):
            print('Values entered must be numbers!')
            continue
        B += [nums]
        str_num += 1
        if str_num > len(A):
            break

V = []
if len(B) > 0:
    C = [[0 for j in range(len(A))] for i in range(len(B))]
    for i in range(len(A)):
        for j in range(len(B)):
            C[i][j] = A[i][j] * B[i][j]

    for j in range(len(C[0])):
        V.append(0)
        for i in range(len(C)):
            V[j] += C[i][j]

print()
if len(V) == 0:
    print('List V is empty')
else:
    print('{:^{:}}'.format('Final matrixC', (1 + arr_print_width) * len(A[0]) - 1))
    for line in C:
        str_value = ' '.join(map('{:12.4g}'.format, line))
        print(str_value)
    print()
    str_value = ' '.join(map(str, V))
    print('Final list V:', str_value)
