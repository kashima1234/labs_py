def main():
    fn = "matrix1.txt"
    matrix = readMatrix(fn)
    n = int(input("Enter row number: "))
    rowSum(matrix, n)

def readMatrix(fn):
    matrix = []
    with open(fn) as f: # a with block will auto close your file after the statements within it
        for line in f:
            line = line.strip() # strip off any trailing whitespace(including '\n')
            matrix.append(line.split()) 
    return matrix

def rowSum(matrix, rowNum):
    result = sum(int(i) for i in matrix[rowNum])
    print("The sum of row {} = {}".format(rowNum, result))

main()

def main():
    fn = "matrix1.txt"
    matrix = readMatrix(fn)
    n = int(input("Enter col number: "))
    colSum(matrix, n)

def readMatrix(fn):
    matrix = []
    with open(fn) as f: # a with block will auto close your file after the statements within it
        for line in f:
            line = line.strip() # strip off any trailing whitespace(including '\n')
            matrix.append(line.split()) 
    return matrix

def colSum(matrix, colNum):
    result = sum(int(row[colNum]) for row in matrix)
    print("The sum of col {} = {}".format(colNum, result))

main()



with open('matrix.txt', 'w') as testfile:
    for row in matrix:
        testfile.write(' '.join([str(a) for a in row]) + '\n')


with open(...) as infile, (...) as outfile:
    outfile.write(infile.read())

