 
#Lab08
# Variant 21

def menu(): 
    print('[1] Ввести матрицу')
    print('[2] Добавить строку ')
    print('[3] Удалить строкуw ')
    print('[4] Добавить столбецn ')
    print('[5] Удалить столбец')
    print('[6] Наиболее повторяющиеся элементы ')
    print('[7] Переставить местами строки с наибольшим и наименьшим количество мотрицательных элементов')
    print('[8] Разница между модулями суммы отрицательных и положительных элементов минимальн ')
    print('[9] Переставить местами столбцы с максимальной и минимальной суммой элементов ')
    print('[10] Вывести текущую матрицу ')



def fool_float_num(num):     # check for floating point number
    e = num.find("e")
    if num[0] == '-':
        num = num[1:]
    if e == -1:
        return False
    if e == len(num) - 1 or num.count('e') > 1:
        return False
    chto = num[0:e]
    order = num[e + 1]
    if chto != "" and order != "":
        if chto.isdecimal() and order.isdecimal():
            return True
        else:
            return False
    else:
        return False
        
def check_dig(num):     # number check
    if num[0] == '-':
        num = num[1:]
    if num.isdecimal():
        return True
    else:
        return False

def prime_num(num):     # check for a prime number
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
            

k = 0 
matrix = []


while True:

    flag = 0 
    
    if k == 0: 
        print(menu())
        k = 3
    k -= 1

    for i in range(len(matrix)):
        if matrix[i] != []:
            flag = 1
            break

    if flag == 0: 
        matrix.clear()

    while True: 
        cmd = input('Enter the command number: ')
        if cmd != "" and (cmd.isdecimal() or fool_float_num(cmd)):
            cmd = int(float(cmd))
            if cmd > 10 or cmd < 0:
                print('The entered menu item does not exist. try again. ')
            else:
                break
        else:
            print('Data entered incorrectly. try again. ')

    if cmd == 0: 
        print('The program has ended.')
        break
    
    if cmd == 1: 

        matrix.clear()
        while True: 
            line = input('Enter the number of matrix rows: ') 
            if line != "" and (line.isdecimal() or fool_float_num(line)) and float(line) > 0:
                line = int(float(line))
                break
            else:
                print('The number of matrix rows must be a number.')
                
        while True: 
            column = input('Enter the number of matrix columns: ')
            if column != "" and (column.isdecimal() or fool_float_num(column)) and float(column) > 0:
                column = int(float(column))
                break
            else:
                print('The number of matrix columns must be a number.')
                
        
        for i in range(line):
            matrix.append([])
            for j in range(column):
                while True:
                    elm = input('Enter the {}th element of the {}th line: '.format(j + 1, i + 1))
                    if elm != "" and (check_dig(elm) or fool_float_num(elm)):
                        elm = int(float(elm))
                        break
                    else:
                        print('Matrix element must be a number.')
                matrix[i].append(elm)
        
    if cmd  == 2: 

        while True: 
            id = input('Enter matrix row index: ')
            if id != "" and (id.isdecimal() or fool_float_num(id)):
                id = int(float(id))
                if id < 0 or id > len(matrix):
                    print('Row index outside matrix.')
                else:
                    break
            else:
                print('Data entered incorrectly. try again. ')
        
        if matrix == []:
            print('The matrix is empty.')
            while True:
                
                column = input('Enter the number of matrix columns: ')
                if column != "" and (column.isdecimal() or fool_float_num(column)) and float(column) > 0:
                    column = int(float(column))
                    break
                else:
                    print('The number of matrix columns must be a number.')
        else:
            column = len(matrix[0])
        add_line = []
        for i in range(column):
            while True:
                
                elm = input('Enter the {}th element of the string: '.format(i + 1))
                if elm != "" and (check_dig(elm) or fool_float_num(elm)):
                    elm = int(float(elm))
                    add_line.append(elm)
                    break
                else:
                    print('Element value must be an integer.')


        matrix.insert(id, add_line)
            
        print('Row added to matrix.')
            
    if cmd  == 3: 
        if matrix == []:
            print('The matrix is empty.')
        else:
            while True:
                
                id = input('Enter matrix row index: ')
                if id != "" and (id.isdecimal() or fool_float_num(id)):
                    id = int(float(id))
                    if id < 0 or id >= len(matrix) :
                        print('Specified row index does not exist.')
                    else:
                        break
                else:
                    print('Row index must be a number.')
                        
            matrix.pop(id)
                
            print('Row removed.')
                
    if cmd  == 4: 
        if matrix == []:
            print('The matrix is empty.')
            len_matrix = 0
            while True:
                
                line = input('Enter the number of matrix rows: ')
                if line != "" and (line.isdecimal() or fool_float_num(line)) and float(line) > 0:
                    line = int(float(line))
                    for i in range(line):
                        matrix.append([])
                    break
                else:
                    print('Number of matrix rows must be a positive integer.')
        else:
            len_matrix = len(matrix)

            
        while True:
            
            id = input('Enter matrix column index: ')
            if id != "" and (id.isdecimal() or fool_float_num(id)):
                id = int(float(id))
                if id < 0 or id > len_matrix:
                    print('Column index outside matrix.')
                else:
                    break
            else:
                print('Data entered incorrectly. try again. ')

        for i in range(len(matrix)):
            while True:
                
                elm = input('Enter the {}th element of the column: '.format(i + 1))
                if elm != "" and (check_dig(elm) or fool_float_num(elm)):
                    elm = int(float(elm))
                    break
                else:
                    print('Element value must be an integer.')
                    
            for j in range(len(matrix[i]) + 1):
                    if id == j:
                        matrix[i].insert(j, elm)

        print('Column added to matrix.')
            
    if cmd  == 5: 
        if matrix == []:
            print('The matrix is empty.')
        else:
            len_matrix = len(matrix[0])

            while True:
                
                id = input('Enter matrix column index: ')
                if id != "" and (id.isdecimal() or fool_float_num(id)):
                    id = int(float(id))
                    if id < 0 or id >= len_matrix:
                        print('Column index outside matrix.')
                    else:
                        break
                else:
                    print('Data entered incorrectly. try again. ')
               
            for i in range(len(matrix)):
                    matrix[i].pop(id)
                
            print('Column removed.')
            
            
    if cmd  == 6: 
        if matrix == []:
            print('The matrix is empty.')
        else:
            max_count = 0 
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    count = matrix[i].count(matrix[i][j]) 
                    if count > max_count:
                        max_count = count
                        id = i
            print('Row index: {}. Line: {}'.format(id, matrix[id]))
                        
    if cmd  == 7: 
        if matrix == []: 
            print('The matrix is empty.')
        elif len(matrix[0]) == 1: 
            print('The matrix contains one column.')
        else:
            add_list = [0] * len(matrix) 
            for i in range(0, len(matrix)):
                count = 0
                for j in range(len(matrix[i])):
                    if matrix[i][j] < 0:
                        add_list[i] += 1 
            max_list = max(add_list)
            min_list = max_list
            for g in range(len(add_list)):
                if add_list[g] != 0 and add_list[g] < min_list:
                    min_list = add_list[g]
            if max_list != 0 and min_list != 0:
                min_id = add_list.index(min_list)
                max_id = add_list.index(max_list)
                if min_id != max_id:
                    matrix[max_id], matrix[min_id] = matrix[min_id], matrix[max_id]
                    print('Rows with the most and least negative elements are swapped.')
                else:
                    print('Rows matching condition not found.')
            else:
                print('Rows matching the condition were not found.')
            
              
    if cmd  == 8:
        if matrix == []: 
            print('The matrix is empty.')
        else:
            add_list = [0] * len(matrix[0])
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if prime_num(matrix[i][j]) and matrix[i][j] > 1:
                        add_list[j] += 1
            max_count = 0
            for g in range(len(add_list)):
                if add_list[g] > max_count:
                    max_count = max(add_list[g], max_count)
                    id = g
            if max_count == 0:
                print('Column matching condition not found.')
            else:
                print('Column Index: {}.'.format(id))
                print('Column:')
                for h in range(len(matrix)):
                    print(matrix[h][id])
                    
    if cmd  == 9: 
        if matrix == []: 
            print('The matrix is empty.')
        elif len(matrix[0]) == 1: 
            print('The matrix contains one column.')
        else:
            add_list = [0] * len(matrix[0]) 
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    add_list[j] += matrix[i][j]
            min_id = add_list.index(min(add_list))
            max_id = add_list.index(max(add_list))
            if min_id == max_id:
                print('Columns matching condition not found.')
            else:
                print('The columns with the largest and smallest sums are swapped.')
                for i in range(len(matrix)):
                    matrix[i][max_id], matrix[i][min_id] = matrix[i][min_id], matrix[i][max_id]
       
                
    if cmd  == 10: 
        if matrix == []:
            print('The matrix is empty.')
        else: 
            print('Matrix:')
            for j in range(len(matrix)):
                for i in range(len(matrix[j])):
                    print('{:5}'.format(matrix[j][i]), end = ' ')
                print()
