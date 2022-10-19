from sys import stdin, stdout

with stdin as in_file, stdout as out_file: 
# with open('in3.txt', 'r') as in_file, open('out3.txt', 'w') as out_file:

    sharps_indexes = [] # indexes of #-filled columns
    pals_count = [] # index = line; value = palindome count

    line1 = in_file.readline()

    # collecting indexes of all #s in 1st line 
    for i in range(len(line1)):
        if line1[i] == '#':
            sharps_indexes.append(i)

    # if there is no # in potential #-filled column, it is not #-filled column then
    for line in in_file:
        for i in range(len(line)):
            if line[i] != '#' and i in sharps_indexes:
                sharps_indexes.remove(i)
    
    in_file.seek(0)
    for line in in_file:
        
        # removing #-filled column from line for further palindrome-check
        chars = list(line)
        for sharp in sharps_indexes:
            chars[sharp] = ''
        line = ''.join(chars)
        
        # counting palindromes
        count = 0        
        words = line.split()
        for word in words:
            if len(word) > 1 and word == word[::-1]:
                count += 1
        
        pals_count.append(count)
    
    # writing out_file by char
    in_file.seek(0)
    line_index = 0
    for line in in_file:
        for i in range(len(line)-1):
            if i not in sharps_indexes:
                out_file.write(line[i])
        out_file.write(' '+str(pals_count[line_index])+'\n')
        line_index += 1