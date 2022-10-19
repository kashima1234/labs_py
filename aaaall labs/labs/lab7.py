# Список(2)
 # lab 7
import time
from math import *


def menu(num):
    numbers = {
        0: "0.Выход",
        1: "1. Очистить список и ввести его с клавиатуры",
        2: "2. Добавить элемент в произвольное место списка",
        3: "3. Удалить произвольный элемент из списка (по номеру),",
        4: "4. Очистить список",
        5: "5. Поиск элемента наибольшей длины, не содержащего английских гласных",
        6: "6. Замена всех заглавных согласных англиских букв на строчные",
    }
    return numbers.get(num, None)


def result(num, a):
    numbers = [action_0, action_1, action_2, action_3, action_4, action_5, action_6, ]
    a = numbers[num](a)
    return a


def action_0():
   print('', end='')


# 1. Очистить список и ввести его с клавиатуры
def action_1(a):
    list1 = list(map(str, input('Ввести элементы списки').split()))
    return list1


# 2. Добавить элемент в произвольное место списка
def action_2(a):
    ind = int(input('Добавить элемент в месте:'))
    if ind - 1 > len(a) or ind <= 0:
        print('index out of range')
    else:
        obj = input('элемент=')
        a.append(obj)
        for i in range(1, len(a) - ind + 1):
            a[-i], a[-i - 1] = a[-i - 1], a[-i]
    return a


# 3. Удалить произвольный элемент из списка (по номеру)
def action_3(a):
    if len(a):
        ind = int(input('Ударить элемент в месте:'))
        if ind > len(a) or ind <= 0:
            print('index out of range')
        else:
            for i in range(ind - 1, len(a) - 1):
                a[i], a[i + 1] = a[i + 1], a[i]
            a.pop()
    else:print('ERROR:Список пустой')
    return a


# 4. Очистить список
def action_4(a):
    a.clear()
    return a


# 5.Поиск элемента наибольшей длины, не содержащего английских гласных
def action_5(a):
    arr = ''
    list1 = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    for el in a:
        t = 1
        for i in list1:
            if i in el:
                t = 0
                break
        if t and len(arr) == 0:
            arr = el
        elif t and len(el) > len(arr):
            arr = el
    if len(arr):
        print(arr)
    else:
        print('Нет элемента, не содержащего английских гласных.')
    return a


# 6. Замена всех заглавных согласных англиских букв на строчные
def action_6(a):

    list1 = []
    list2 = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    if len(a):
        for el in a:
            for i in el:
                if i in list2:
                    list1.append(el.lower())        # this is mean you add last word to list./
    else:
        print('ERROR:Список пустой')
    return list1


def input_control():
    global t
    try:
        t = int(input('Ввести число 0-6\n>>>'))
    except:
        input_control()


# a = ['1sdfwwWwysd', '2aaAaaa', '3asdfg3', '4dsqweSr', '5sdzZxac', '6DdFFFZ', '7aa', '8ASDFF']
# print(a)
i = 1
a=[]

while 1:
    t = -1
    if i % 3 == 1:
        for k in range(1, 6):
            print(menu(k))
        print("0.Выход")
    while t < 0 or t > 6:
        input_control()
    print(menu(t))
    if t == 0:
        break
    a = result(t, a)
    print('\nlist=', a)
    i += 1
