# Оюунтуяа Одбаясгалан ИУ7-13Б
# The program allows you to carry out useful work with matrices
# and display the result on the screen.
from fool_check import *


print('\nWelcome to the list editor! \ N')
# A matrix variable to be worked on.
matrix = [[1, 2, 2],
          [0, 4, 0],
          [3, 3, -5],
          [-12, 4, 0]]
# Main loop
while True:
    print('[0] Exit the program')
    print('[1] Enter matrix')
    print('[2] Add line')
    print('[3] Delete line')
    print('[4] Add Column')
    print('[5] Delete column')
    print('[6] Find the string with the largest number of consecutive identical \
elements')
    print('[7] Swap the lines with the largest and smallest \
number of negative elements')
    print('[8] Find the column with the most null elements')
    print('[9] Swap columns with maximum and minimum \
sum of elements')
    print('[10] Display the current matrix')
    command = make_integer(input('Enter the option number: '))
    if command is None:
        print('Option number value must be an integer.\n')
        continue
    if command > 10 or command < 0:
        print('Wrong option. Enter option between 0-10!\n')
        continue
    if command not in [0, 1, 2, 4] and len(matrix) == 0:
        print('Option failed: Matrix empty.\n')
        continue

    # Executing commands
    # Exit the program
    if command == 0:
        break

    # Matrix input
    if command == 1:
        # Matrix cleaning warn
        if len(matrix) > 0:
            while True:
                print('\n\tAttention! The matrix will be COMPLETELY cleared. \
Are you sure? y/n: ', end='')
                answer = input().lower()
                if answer in ['y', 'n']:
                    break
                print()
            if answer == 'n':
                continue
            matrix = []
        # Line-by-line matrix input
        counter = 0
        print('\tEnter the integer values of the matrix elements line by line \
through spaces', '\n\tTo exit press ENTER on a new line.')
        while True:
            # Handle newline input
            str_value = input('\t'+str(counter)+'). ')
            if len(str_value) == 0:
                print('\n\tMatrix updated successfully!')
                break
            row_list = str_value.split()
            if counter > 0 and len(row_list) != len(matrix[0]):
                print('\tThe number of elements of the inserted row must be \
equal to the number of elements in the first line.\n')
                continue
            if any([make_integer(element) is None for element in row_list]):
                print('\tMatrix values must be integers!\n')
                continue
            row_list = list(map(make_integer, row_list))
            matrix += [row_list]
            counter += 1

    # Insert line
    if command == 2:
        # Processing the index of the inserted row
        while True:
            index = make_integer(input('\tEnter the index of the \
strings: '))
            if index is None:
                print('\tThe index value must be an integer.\n')
            elif abs(index) > len(matrix):
                print('\tThe module index value is greater than the number of \
matrix rows.\n')
            else:
                break
        # Handle newline input
        while True:
            insert_value = input('\tEnter string values separated by spaces: ')
            row_list = insert_value.split()
            if len(row_list) != len(matrix[0]):
                print('\tThe number of elements of the inserted row must be \
equal to the number of columns.\n')
                continue
            if any([make_integer(element) is None for element in row_list]):
                print('\tMatrix values must be integers!\n')
                continue
            row_list = list(map(make_integer, row_list))
            break

        while True:
            algorithm = input('\tEnter insertion method! (A/P): ').upper()
            if algorithm in ['A', 'P']:
                break
            print()

        if algorithm == 'A':
            index = len(matrix) - abs(index) if index < 0 else index
            matrix += [[]]
            for i in range(len(matrix)-1, index, -1):
                matrix[i] = matrix[i - 1]
            matrix[index] = row_list
        if algorithm == 'P':
            matrix.insert(index, row_list)
        print('\n\tString inserted into matrix.')

    # Deleting a line
    if command == 3:
        # Handle the input of the index of the row to be deleted
        while True:
            index = make_integer(input('\tEnter the index of the \
strings: '))
            if index is None:
                print('\tThe index value must be an integer.\n')
            else:
                index = len(matrix) - abs(index) if index < 0 else index
                if index < 0 or index >= len(matrix):
                    print('\tNo row with such index exists\n')
                else:
                    break

        while True:
            algorithm = input('\tEnter removal method (A/P): ').upper()
            if algorithm in ['A', 'P']:
                break
            print()

        if algorithm == 'A':
            for i in range(index, len(matrix) - 1):
                matrix[i] = matrix[i + 1]
            matrix.pop()
        if algorithm == 'P':
            matrix = matrix[:index] + matrix[index+1:]
        print('\n\tRow removed from the matrix.')

    # Insert a column
    if command == 4:
        # Processing the index of the inserted column
        while True:
            index = make_integer(input('\tEnter the index of the \
column: '))
            if index is None:
                print('\tThe index value must be an integer.')
            elif abs(index) > len(matrix[0]):
                print('\tThe module index value is greater than the number of \
columns matrix.\n')
            else:
                break

        while True:
            insert_value = input('\tEnter column values separated by spaces: ')
            column_list = insert_value.split()
            if len(column_list) != len(matrix):
                print('\tThe cardinality of the inserted column must be \
be equal to the number of rows')
                continue
            if any([make_integer(element) is None for element in column_list]):
                print('Matrix values must be integers!')
                continue
            column_list = list(map(make_integer, column_list))
            break

        while True:
            algorithm = input('\tEnter insertion method (A/P): ').upper()
            if algorithm in ['A', 'P']:
                break
            print()

        if algorithm == 'A':
            index = len(matrix[0]) - abs(index) if index < 0 else index
            for i in range(len(matrix)):
                matrix[i] += [None]
                for j in range(len(matrix[i])-1, index, -1):
                    matrix[i][j] = matrix[i][j-1]
                matrix[i][index] = column_list[i]
        if algorithm == 'P':
            for i in range(len(matrix)):
                matrix[i].insert(index, column_list[i])
        print('\n\tColumn inserted into matrix.')

    # Deleting a column
    if command == 5:
        # Handling the input of the index of the column to be deleted
        while True:
            index = make_integer(input('\tEnter the index of the \
column: '))
            if index is None:
                print('\tThe index value must be an integer.\n')
            else:
                index = len(matrix[0]) - abs(index) if index < 0 else index
                if index < 0 or index >= len(matrix[0]):
                    print('\tThere is no column with this index\n')
                else:
                    break

        while True:
            algorithm = input('\tEnter removal method (A/P): ').upper()
            if algorithm in ['A', 'P']:
                break
            print()

        if algorithm == 'A':
            index = len(matrix[0]) - abs(index) if index < 0 else index
            for i in range(len(matrix)):
                for j in range(index, len(matrix[i])-1):
                    matrix[i][j] = matrix[i][j+1]
                matrix[i].pop()
        if algorithm == 'P':
            for i in range(len(matrix)):
                matrix[i] = matrix[i][:index] + matrix[i][index+1:]
        print('\n\tColumn removed from matrix.')

    # Search for a string with a property
    if command == 6:
        str_value = ''
        max_length = 0
        last_ch = ''
        length = 0
        for i in range(len(matrix)):
            for element in matrix[i]:
                if element == last_ch or last_ch == '':
                    length += 1
                else:
                    if max_length < length:
                        str_value = '\t[ ' + ', '.join(map('{:12.4g}'.format,
                                                           matrix[i])) + ' ]'
                        max_length = length
                    length = 1
                last_ch = element
            if max_length < length:
                str_value = '\t[ ' + ', '.join(map('{:12.4g}'.format,
                                                   matrix[i])) + ' ]'
                max_length = length
            last_ch = ''
            length = 0
        print('\n\tThe string with the most consecutive identical \
elements:')
        print(str_value)

    # Rearrange strings with properties
    if command == 7:
        min_idx = -1
        max_idx = -1
        min_counter = float('inf')
        max_counter = -min_counter
        for i in range(len(matrix)):
            counter = 0
            for element in matrix[i]:
                if element < 0:
                    counter += 1
            if counter > max_counter:
                max_idx = i
                max_counter = counter
            if counter < min_counter:
                min_idx = i
                min_counter = counter
        matrix[min_idx], matrix[max_idx] = matrix[max_idx], matrix[min_idx]
        print('\tOperation completed successfully.')

    # Search for a column with a property
    if command == 8:
        str_value = ''
        max_count = 0
        for j in range(len(matrix[0])):
            count = 0
            tmp_str = '\t[ '
            for i in range(len(matrix)):
                element = matrix[i][j]
                if element == 0:
                    count += 1
                if i > 0:
                    tmp_str += '\t  '
                tmp_str += '{:12.4g}'.format(element)
                if i < len(matrix)-1:
                    tmp_str += '\n'
            tmp_str += ' ]'
            if count > max_count:
                str_value = tmp_str
                max_count = count
        print('\n\tColumn with the most zero items:')
        print(str_value)

    # Rearrange columns with property
    if command == 9:
        min_sum = float('inf')
        max_sum = -min_sum
        max_idx = -1
        min_idx = -1
        for j in range(len(matrix[0])):
            tmp_sum = 0
            for i in range(len(matrix)):
                tmp_sum += matrix[i][j]
            if tmp_sum > max_sum:
                max_idx = j
                max_sum = tmp_sum
            if min_sum > tmp_sum:
                min_idx = j
                min_sum = tmp_sum

        for i in range(len(matrix)):
            matrix[i][min_idx], matrix[i][max_idx] = \
                matrix[i][max_idx], matrix[i][min_idx]
        print('\tOperation completed successfully.')

    if command == 10:
        print('\n\tMatrix current values:')
        matrix_str = '\t[ '
        for i in range(len(matrix)):
            if i > 0: matrix_str += '\t  '
            matrix_str += ', '.join(map('{:12.4g}'.format, matrix[i]))
            if i < len(matrix)-1: matrix_str += '\n'
        matrix_str += ' ]'
        print(matrix_str, sep='')

    print()

input('Press any key to exit.')
