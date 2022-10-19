dim = int(input("Dimention: "))

def display_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            print(mat[i][j], end = " ")
        print()
mat = [[0 for i in range(dim)] for j in range(dim)]

j ,k, count = 0, 0, 0
elem = 1
flag = True
for i in range(int(dim * (dim + 1) / 2)):
    if count < dim:
        mat[j][k] = elem
        elem += 1;
        k += 1
    elif count < 2 * dim:
        k -= 1
        if flag:
            flag = False
            count += 1
            j += 1
            continue
        mat[j][k] = elem
        j += 1
        elem += 1
    """elif count < 3 * dim - 1:
        j -= 1
        mat[j][k] = elem
        elem += 1"""
    count += 1
display_mat(mat)
