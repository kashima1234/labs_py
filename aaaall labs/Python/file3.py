def the_longest_sentence(a):
    res = [sentences[0],sentences[0]]
    for j in range(1, len(sentences)):
        if len(sentences[j]) > len(res[0]):
            res[0] = sentences[j]
    d = res[0]
    return d
with open ('proba4.txt', 'r') as input_:
    with open ('resenie4.txt', 'w') as output:
        a = input_.read()
        seperators = ['.', '?', '!']
        a = list(''.join(a))
        i = 0
        sentences = ['']
        for char in a:
            sentences[i] += char
            if char in seperators:
               sentences[i] = ' '.join(sentences[i].strip().split())
               sentences.append('')
               i += 1
        sentences.remove('')
        
        result = [sentences[0],sentences[0]]
        for i in range(1, len(sentences)):
            if len(sentences[i]) < len(result[0]):
                result[0] = sentences[i]
        b = result[0]
        d = the_longest_sentence(a)
        output.write(b)
        output.write('\n')
        output.write(d)
        output.write('\n')
with open ('resenie4.txt', 'r+') as output:
    line = output.readline()
    while line:
        words = line.split()
        line = output.readline()
        len_of_words = len(words)
        for lineno,lime in enumerate(output):
            if lineno % 2 == 0:
                lime += '{'+str(len_of_words)+'}'
            print(lime)
            output.write(lime)
    
