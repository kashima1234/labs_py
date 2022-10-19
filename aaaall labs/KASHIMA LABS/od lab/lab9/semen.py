
razm = list(map(int, input('enter the dimensions of the array in the format XxYxZ: ').split('x')))
print(razm)
A = [[[0]*razm[0]]*razm[1]]*razm[2]
print(A)
for k in range(razm[2]):
    for i in range(razm[0]):
        for j in range(razm[1]):
            A[k][i][j] = float(input('Meaning: '))
print(A[0])
print(A[1])
sums_Z = []
for j in range(razm[1]):
    tmp_sum = 0
    for i in range(razm[0]):
        tmp_sum += sum(A[i][j])
        sums_Z.append((tmp_sum, (i, j)))

print(sums_Z)
sums_Z = sorted(sums_Z, key=lambda x: x[0])
print(sums_Z)




