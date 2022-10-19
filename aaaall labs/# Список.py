# Список
# ФИО: Гао Шан, Группа ИУ7-11Б
# Вариант №5
import time
# time.sleep(5)
from math import *


def menu(num):
    numbers = {
        0: "0.Выход",
        1: "1. Проинициализировать список первыми N элементами заданного в л/р 5 ряда",
        2: "2. Очистить список и ввести его с клавиатуры",
        3: "3. Добавить элемент в произвольное место списка",
        4: "4. Удалить произвольный элемент из списка (по номеру)",
        5: "5. Очистить список",
        6: "6. Найти значение K-го экстремума в списке",
        7: "7. Найти наиболее длинную последовательность по варианту"
    }
    return numbers.get(num, None)


def result(num):
    numbers = [action_0, action_1, action_2, action_3, action_4, action_5, action_6, action_7]
    numbers[num]()


def action_0():
    print('', end='')


# 1. Проинициализировать список первыми N элементами заданного в л/р 5 ряда
def action_1():
    list1.clear()
    a = 0
    N = int(input("N="))
    while a < N:
        list1.append(round(1 / factorial(a) * (-1) ** a, 5))
        a += 1


# 2. Очистить список и ввести его с клавиатуры
def action_2():
    global list1
    list1 = list(map(int, input('Ввести элементы списки').split()))


# 3. Добавить элемент в произвольное место списка
def action_3():
    ind = int(input('Добавить элемент в месте'))
    obj = float(input('элемент='))
    list1.insert(ind - 1, obj)


# 4. Удалить произвольный элемент из списка (по номеру)
def action_4():
    list1.pop(int(input('Место удаленного элемента=')) - 1)


# 5. Очистить список
def action_5():
    list1.clear()


# 6. Найти значение K-го экстремума в списке
def action_6():
    list_1 = []
    for a in range(1, len(list1) - 1):
        if (list1[a] > list1[a + 1] and list1[a] > list1[a - 1]) or (
                list1[a] < list1[a + 1] and list1[a] < list1[a - 1]):
            list_1.append(list1[a])
    a = int(input('K='))
    try:
        print('Значение K-го экстремума в списке=', list_1[a - 1])
    except IndexError:
        print('Не так много экстремумов')
    input('press enter to continue')


# 7. Найти наиболее длинную последовательность по варианту
def action_7():

    
    max_l = 0
    a = 2
    max_li = [None]
    while a < len(list1):
        li = []
        if list1[a] == list1[a - 1] + list1[a - 2]:
            li.append(list1[a - 2])
            li.append(list1[a - 1])
            while a < len(list1) and list1[a] == list1[a - 1] + list1[a - 2]:
                li.append(list1[a])
                a += 1

        if max_l < len(li):
            max_l = len(li)
            max_li = list.copy(li)
        a += 1
    print('наиболее длинную последовательность=', max_li)
    input('press enter to continue')


# noinspection PyBroadException
def input_control():
    global t
    try:
        t = int(input('Ввести число 0-7\n>>>'))
    except:
        input_control()


list1 = []
i = 1

while 1:
    t = -1
    if i % 4 == 1:
        for k in range(1, 8):
            print(menu(k))
        print("0.Выход")
    while t < 0 or t > 7:
        input_control()
    print(menu(t))
    result(t)
    if t == 0:
        break
    print('\nlist=', list1)
    i += 1
