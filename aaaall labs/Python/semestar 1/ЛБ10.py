#Пискунов Панте. Лабораторная работа №10
import re
print()
print()
def menu():         #Создаем меню
    print ('\t1. Выравнивание текста по ширине.')
    print ('\t2. Выравнивание текста по левому краю.')
    print ('\t3. Выравнивание текста по правому краю.')
    print ('\t4. Замена одного слова другим во всем тексте.')
    print ('\t5. Удалить указанное слово из текста.')
    print ('\t6. Вычисление арифметического выражения.')
    print ('\t7. Удалить самое длиное слово в самом коротком по числу слов предложении.')

def select():    #Создаем шаг для выбра
    try:
        s = int(input('Выбор: '))
    except ValueError:
        print('Неправильное значение,попробуйте еще раз!')
        return select()
    if s < 0 or s > 7:
        print('Выбрать в интервале [1,7]!')
        return select()
    return s

def main(text, s):
    if s == 1 or s <=3:
        for i in range(len(text)):
            line = text[i]
            text[i] = ' '.join([x.strip() for x in line.split()])
        lenghtestLine = 0
        for line in  text:
                if len(line) > lenghtestLine:
                    lenghtestLine = len(line)

        if s == 1:     #Выравниваем текст по ширине
            text = centerAlign(text, lenghtestLine)
            print()

        elif s == 2:    #Выравниваем текст по левому краю
            for i in range(len(text)):
                text[i] = text[i].lstrip()
            
        if s == 3:  #Выравнивание текста по правому краю
            for i in range(len(text)):
                if text[i] != '':
                    text[i] = ' ' * (lenghtestLine - len(text[i])) + text[i]
        
        return text

    elif s == 4:        #Заменяем одного слова другим во всем тексте
        word = input('Введите слово, которым хотите его заменить: ')
        toword = input('Замена слова: ')
        return myReplace(text,word, toword)

    elif s == 5:    #Удаляем указанное слово из текста
        word = input('Введите слово, которое хотите удалить из текста: ')
        return myRemove(text,word)

    elif s == 6:  #Вычисляем арифметику
        return sixth_punct(text)

    elif s == 7: #Ищем длину слова и предложения
        return findLengSent(text)

def safe_number(num):
    try:
        if '.' in num or 'e' in num:
            return float(num)
        else:
            return int(num)
    except:
        return None
  
def brk(listed):
    seperator = [' ', ',', '.', '"', "'", ';', ':', '[', ']', '{', '}', '=', '+', '-', '_', ')', '(', '1', '!', '/', '\\', '?', '>', '<']
    breakedLines = []
    i = -1
    for line in listed:             
        breakedLines.append([''])
        i += 1
        j = 0
        for char in line:
            if char in seperator:
                breakedLines[i].append(char)
                breakedLines[i].append("")
                j += 2
            else:
                breakedLines[i][j] += char

    return breakedLines


def myReplace(listed, word, toWord):     #Определяем какое слово хотим поменять               
    breakedLines = brk(listed)
    for i in range(len(breakedLines)):
        for j, wrd in enumerate(breakedLines[i]):
            if wrd == word:
                breakedLines[i][j] = toWord

        breakedLines[i] = ''.join(breakedLines[i])  
    return breakedLines
                
def myRemove(listed, word):             #Определяем какое слово хотим удалить                    
    breakedLines = brk(listed)
    for i in range(len(breakedLines)):
        for j, wrd in enumerate(breakedLines[i]):
            if wrd == word:
                breakedLines[i][j] = ''

        breakedLines[i] = ''.join(breakedLines[i])
    return breakedLines

def centerAlign(listed, scrWidth):  #Выравниваем текст по ширине          
    breakedLines = []
    i = -1
    for line in listed:         # срезаем строку
        breakedLines.append([''])
        i += 1
        j = 0
        for char in line:       
            if char == ' ':     #split
                breakedLines[i].append(char)
                breakedLines[i].append('')
                j += 2
            else:
                breakedLines[i][j] += char  
        if '' in breakedLines[i]:
            breakedLines[i].remove('')  #если существует пустая строка,тогда удаляем ее

    for i in range(len(breakedLines)):  # выравниваем строку 
        spaces = breakedLines[i].count(' ')
        if spaces != 0:
            lenLn = 0
            for j in range(len(breakedLines[i])):
                lenLn += len(breakedLines[i][j])

            differ = scrWidth - lenLn
            toAdd = differ % spaces
            for j in range(len(breakedLines[i])):
                if breakedLines[i][j] == ' ':
                    breakedLines[i][j] += ' ' * (differ//spaces + (1 if toAdd > 0 else 0))
                    toAdd -= 1
        breakedLines[i] = ''.join(breakedLines[i])
    
    return breakedLines

def find_longest_word(word_list):       #Определяем наидлинее слово
    seperator = [',','.',';','!','?',' ']
    word_list = word_list.replace(',', ' ').replace(', ', ' ').replace( '?', ' ').replace('.', ' ').split()
    longest_word =  max(word_list, key=len)
    return longest_word
    
def findLengSent(text):     #Определяем самое короткое предложение
    fr = text.copy()
    sep = ['?', '.', '!']
    text = list(''.join(text))
    sentences = ['']
    i = 0
    for char in text:
        sentences[i] += char
        if char in sep:
            sentences[i] = ' '.join(sentences[i].strip().split())
            sentences.append('')
            i += 1

    sentences.remove('')
    result = [sentences[0], sentences[0]]
    for i in range(1, len(sentences)):
        if len(sentences[i]) < len(result[0]):
            result[0] = sentences[i]
    
    a = result[0]
    print('Самое короткое предложение: ', a)
    b = find_longest_word(a)
    print('Найдлинее слово: ', b)
    return myRemove(fr, b)

def find_inner_exp(exp):
    if not('(' in exp or ')' in exp):
        return exp

    final_exp = exp
    while '(' in final_exp or ')' in final_exp:
        open_index = final_exp.index('(')
        index = open_index + 1
        openings = 1

        while index < len(final_exp):
            char = final_exp[index]
            if char in '(':
                openings += 1
            if char in ')':
                openings -= 1
                if openings == 0:
                    inner_exp = final_exp[open_index + 1: index]
                    result = str(eval_exp(inner_exp))
                    final_exp = final_exp[:open_index] + result + final_exp[index + 1:]
                    break
            index += 1

    final_exp = final_exp.replace('+-', '-')
    final_exp = final_exp.replace('-+', '-')
    final_exp = final_exp.replace('++', '+')
    final_exp = final_exp.replace('--', '-')
    return final_exp


def eval_exp(raw):

    raw = raw.replace(' ', '')
    exp = find_inner_exp(raw)
    num = safe_number(exp)

    if type(num) in [int, float]:
        return num

    if '-' in exp:
        left, right = exp.split('-')
        if len(left) and left[-1].isnumeric():
            return eval_exp(left) - eval_exp(right)
    if '+' in exp:
        left, right = exp.split('+')
        if (left[-1].isnumeric()):
            return eval_exp(left) + eval_exp(right)
    if '/' in exp:
        left, right = exp.split('/')
        return eval_exp(left) / eval_exp(right)
    if '**' in exp:
        left, right = exp.split('**')
        return eval_exp(left) ** eval_exp(right)
    if '*' in exp:
        left, right = exp.split('*')
        return eval_exp(left) * eval_exp(right)


def eval_exps(line):
    exps = get_exps(line)
    new_line = line
    for exp in exps:
        result = str(eval_exp(exp))
        if result != None:
            new_line = new_line.replace(exp, result + ' ')
    return new_line


def get_exps(line):
    exps = ['']
    for char in line:
        if char.isdigit() or char in '+-/*%()':
            exps[-1] += char
        elif char == ' ' and exps[-1] != '':
            exps[-1] += char
        else:
            if exps[-1] != '':
                exps.append('')

    return list(filter(lambda e: e != ' ' and e != '', exps))

def sixth_punct(text):
    for i, line in enumerate(text):
        text[i] = eval_exps(line)
    return text
f = open('text.txt', 'r')

textList = f.read().split('\n')
printtext = textList
f.close()
while True:
    menu()
    select1 = select()
    textList = main(textList,select1)
    if select1 == 0:
        break
    if select1 < 7:
        print('\n'.join(textList))
