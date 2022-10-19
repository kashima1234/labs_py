def add_zero_to_end(col, len_max):
    if len(col) < len_max:
        number_of_zero = len_max - len(col)
        for i in range(number_of_zero):
            col.append(0)
    return col

def sort_matrix(matr):
    matr_by_col = []
    for i in range(len(matr)):
        matr_by_col.append([])
        for j in range(len(matr[i])):
            matr_by_col[i].append(matr[j][i])
    len_matr = []
    for i in range(len(matr)):
        x = 0
        for j in range(len(matr[i])):
            x += len(matr[i][j])
        len_matr.append(x)
    for i in range(len(len_matr)):
        for j in range(len(len_matr) - 1 - i):
            if len_matr[j] > len_matr[j + 1]:
                len_matr[j], len_matr[j + 1] = len_matr[j + 1], len_matr[j]
                matr[j], matr[j + 1] = matr[j + 1], matr[j]
    print(len_matr)
    return matr
        
with open('in.txt','r') as input_:
    with open('out.txt','w') as output:
        rows = 0
        mat = []
        for i in input_:
            mat.append(i.replace("\n", ""))
        
        sec_mat = []    
        for i in mat:
            sec_mat.append(i.split(" "))
        matr = []
        k = 0
        for i in sec_mat:
            matr.append([])
            for j in i:
                matr[k].append(len(j))
            k += 1
            
        len_max = len(matr[0])
        for i in range(1, len(matr)):
            if len(matr[i]) > len_max:
                len_max = len(matr[i])
        for i in range(len(matr)):
            matr[i] = add_zero_to_end(matr[i], len_max)
        for i in matr:
            for j in i:
                output.write(str(j) + " ")
            output.write("\n")
        """
        for i in mat:
            output.write(i + '\n')
    
        sec_mat = []
        for i in mat:
            sec_mat.append(i.split(" "))
        output.write("\n")
        matr = sort_matrix(sec_mat)
        for i in matr:
            for j in i:
                output.write(j + " ")
            output.write("\n")
        """
            
    
        
        
            
