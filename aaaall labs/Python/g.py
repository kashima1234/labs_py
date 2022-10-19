import re
def remove(A):

    pattern = '[0123456789.-]'

    A = [re.sub(pattern, '', i) for i in A]

    return A
A = ['-1.0', '-4.5', 'abd', 'bd', 'ddd', 'wwwww','10.125', '-5.0625', '1.1390625']
empty = []
for string in remove(A):
    if string != '':
        empty.append(string)
print(empty) 
index = 1
output = [empty[0]]
while index < len(empty):
    word = empty[index]
    prevWord = empty[index - 1]
    isMadeFromPrev = True
    for char in word:
        if not char in prevWord:
            isMadeFromPrev = False
            break
    if isMadeFromPrev:
        output.append(word)
    index += 1
#finalList = list(dict.fromkeys(output))
print('Последовательность,включающую в себя наибольшее количество элементов-строк: ',output)
