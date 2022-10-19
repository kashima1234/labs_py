# Гао Шан ИУ7 11Б
# gaosh@student.bmstu.ru
import re


def hebing(stro):
    str1 = []
    for el in stro:
        st = ''
        for j in el:
            st += j
            st += ' '
        st = st[0:-1]
        str1.append(st)
    return str1


def result(num):
    numbers = [action_0, action_1, action_2, action_3, action_4, action_5, action_6, action_7]
    return numbers[num](str1)

# inspection Exception
def input_control():
    global t
    try:
        t = int(input('Ввести число 0-7\n>>>'))
    except:
        input_control()

dictt = {
    0: "0. Выход",
    1: "1. Выровнять текст по левому краю",
    2: "2. Выровнять текст по правому краю",
    3: "3. Выровнять текст по ширине",
    4: "4. Удаление всех вхождений заданного слова",
    5: "5. Замена одного слова другим во всём тексте",
    6: "6. Вычисление арифметических выражений внутри текста (операции умножения и деления)",
    7: "7. Отсортировать слова в лексикографическом порядке в самом длинном по количеству символов предложении"
}

def action_0(a):
    return a


# 1. Выровнять текст по левому краю
def action_1(a):
    global flago
    flago = action_1
    return a


# 2. Выровнять текст по правому краю
def action_2(a):
    max_len = len(a[0])
    for el in a:
        if len(el) > max_len:
            max_len = len(el)
    for i in range(len(a)):
        a[i] = ' ' * (max_len - len(a[i])) + a[i]
    global flago
    flago = action_2
    return a


# 3. Выровнять текст по ширине
def action_3(a):
    max_len = len(a[0])
    for el in a:
        if len(el) > max_len:
            max_len = len(el)
    a = [el.strip(' ').split(' ') for el in a]
    for i in range(len(a)):
        if len(a[i]) == 1:
            st = ''
            for j in a[i][0]:
                st += j
            a[i] = st
        else:
            leni = 0
            for el in a[i]:
                leni += len(el)
            sp = 0
            while (max_len - leni - sp) % (len(a[i]) - 1) != 0:
                sp += 1
            t = int((max_len - leni - sp) / (len(a[i]) - 1))
            st = ''
            flag = 0
            for j in range(len(a[i]) - 1):
                st += a[i][j]
                if flag < sp:
                    st += ' ' * (t + 1)
                    flag += 1
                else:
                    st += ' ' * t
            st += a[i][j + 1]
            a[i] = st
    global flago
    flago = action_3
    return a


# 4. Удаление всех вхождений заданного слова
def action_4(a):
    str0 = str(input("Вветите слово:"))
    a = [el.strip(' ').split(' ') for el in a]
    for i in range(len(a)):
        while 1:
            try:
                a[i].remove(str0)
            except ValueError:
                break
    a = hebing(a)
    if flago:
        a = flago(a)
    return a


# 5. Замена одного слова другим во всём тексте
def action_5(a):
    str0 = str(input("Вветите заменное слово:"))
    str1 = str(input("Вветите новое слово:"))
    a = [el.strip(' ').split(' ') for el in a]
    for i in range(len(a)):
        while 1:
            try:
                ind = a[i].index(str0)
                a[i].pop(ind)
                a[i].insert(ind, str1)
            except ValueError:
                break
    a = hebing(a)
    if flago:
        a = flago(a)
    return a


# 6. Вычисление арифметических выражений внутри текста (операции умножения и деления)
def action_6(a):
    a = [el.strip(' ').split(' ') for el in a]
    for i in range(len(a)):
        for j in range(len(a[i])):
            v = re.split('[*/]', a[i][j])
            try:
                for strr in v:
                    float(strr)
            except ValueError:
                continue
            fuh = re.split('[0123456789. ]+', a[i][j])
            fuh.pop(0)
            ind = 1
            for el in fuh[0:-1]:
                v.insert(ind, el)
                ind += 2
            res = float(v[0])
            ind = 1
            while ind < len(v):
                if v[ind] == '*':
                    res *= float(v[ind + 1])
                elif v[ind] == '/':
                    res /= float(v[ind + 1])
                ind += 2
            a[i][j] = str(round(res, 5))
    a = hebing(a)
    if flago:
        a = flago(a)
    return a


# 7. Отсортировать слова в лексикографическом порядке в самом длинном по количеству символов предложении.
def action_7(a):
    max_len = len(a[0])
    count = 0
    for i in range(len(a)):
        if len(a[i]) > max_len:
            max_len = len(a[i])
            count = i
    a = [el.strip(' ').split(' ') for el in a]
    a[count].sort()
    a = hebing(a)
    if flago:
        a = flago(a)
    return a



flago = False
while 1:
    filename='lab11.txt'
    t = -1
    for k in range(1,len(dictt)):
        print(dictt.get(k, None))
    print("0.Выход")
    while t < 0 or t > 7:
        input_control()
    print(dictt.get(t, None))
    if t == 0:
        break
    f = open(filename, 'r+',encoding='utf-8')
    stro = f.readlines()
    f.close()
    stro = [el.strip(' ').split() for el in stro]
    str1 = hebing(stro)
    str1 = result(t)
    with open(filename, 'w+',encoding='utf-8') as f:
        for el in str1:
            f.write(el + '\n')
    for el in str1:
        print(el)
    # time.sleep(5)
