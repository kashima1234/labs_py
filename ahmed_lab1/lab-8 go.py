# Список
# ФИО: Гао Шан, Группа ИУ7-11Б
# Вариант №5
import time
from math import *


def menu(num):
    numbers = {
        0: "0.Выход",
        1: "1. Ввести матрицу",
        2: "2. Добавить строку",
        3: "3. Удалить строку",
        4: "4. Добавить столбец",
        5: "5. Удалить столбец",
        6: "6. Найти строку, имеющую определённое свойство по варианту",
        7: "7. Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов",
        8: "8. Найти столбец, имеющий определённое свойство по варианту",
        9: "9. Переставить местами столбцы с максимальной и минимальной суммой элементов",
        10: "10. Вывести текущую матрицу",
    }
    return numbers.get(num, None)


def result(num):
    numbers = [action_0, action_1, action_2, action_3, action_4, action_5, action_6, action_7, action_8, action_9,
               action_10]
    return numbers[num](list1)


def action_0(a):
    print('', end='')
    return a


# 1. Ввести матрицу
def action_1(a):
    m = n = -1
    list1 = []
    while m <= 0:
        m = int(input('Ввести количества строк матрицы:'))
    while n <= 0:
        n = int(input('Ввести количества стобцов матрицы:'))
    for i in range(m):
        list1.append([])
        for j in range(n):
            list1[i].append(int(input('Ввести {}-й элемент {}-й строки:'.format(i + 1, j + 1))))
    return list1


# 2. Добавить строку
def action_2(a):
    k = int(input("Номер добавленного строки(начало с 1):"))
    if k - 1 > len(a):
        print('index out of range')
    else:
        # a.append([0 for i in range(len(a[0]))])
        # for i in range(len(a) - k+1):
        #     for j in range(len(a[0])):
        #         a[len(a) - i - 1][j] = a[len(a) - i - 2][j]
        # a[k-1].clear()
        a.insert(k - 1, [])
        for j in range(len(a[0])):
            a[k - 1].append(int(input('Ввести {}-й элемент:'.format(j + 1))))
    return a


# 3. Удалить строку
def action_3(a):
    k = int(input("Номер удоленного строки(начало от 1):"))
    if k > len(a):
        print('index out of range')
    else:
        a.pop(k - 1)
    return a


# 4. Добавить столбец
def action_4(a):
    k = int(input("Номер добавленного столбеца(начало от 1):"))
    if k > len(a):
        print('index out of range')
    else:
        for i in range(len(a)):
            a[i].insert(k - 1, int(input("Ввести {}-й элемент(начало от 1):".format(i + 1))))
    return a


# 5. Удалить столбец
def action_5(a):
    k = int(input("Номер удоленного столбеца(начало от 1):"))
    if k > len(a):
        print('index out of range')
    else:
        for i in range(len(a)):
            a[i].pop(k - 1)
    return a


# 6. Найти строку, имеющую наибольшее количество повторяющихся элементов
def action_6(a):
    if len(a) == 0:
        print('Error:Матрица пуста')
    else:
        max_k = 0
        raw = -1
        for i in range(len(a)):
            for j, el in enumerate(a[i]):
                k = 0
                for p in range(len(a[i])):
                    if el == a[i][p]:
                        k += 1
                if k > max_k:
                    max_k = k
                    raw = i
        print("{}-ая строка имеет наибольшее количество повторяющихся элементов".format(raw + 1))
        input('press enter to continue')
    return a


# 7. Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов
def action_7(a):
    if len(a) == 0:
        print('Error:Матрица пуста')
    else:
        raw_1 = raw_2 = max_k = 0
        min_k = len(a[0])
        for i in range(len(a)):
            k = 0
            for j in range(len(a[i])):
                if a[i][j] < 0:
                    k += 1
            if k > max_k:
                max_k = k
                raw_1 = i
            if k < min_k:
                min_k = k
                raw_2 = i
        a[raw_1], a[raw_2] = a[raw_2], a[raw_1]
        action_10(a)
    return a


# 8. Найти столбец, имеющий наибольшее количество чисел, являющихся степенями 2
def action_8(a):
    if len(a) == 0:
        print('Error:Матрица пуста')
    else:
        raw = 0
        max_k = 0
        for i in range(len(a[0])):
            k = 0
            for j in range(len(a)):
                t = a[j][i]
                while t != 1:
                    t /= 2
                    if t == 1:
                        k += 1
                    if t % 2 != 0:
                        break
            if k > max_k:
                max_k = k
                raw = i
        print("{}-ой столбец имеет наибольшее количество чисел, являющихся степенями 2".format(raw + 1))
        input('press enter to continue')
    return a


# 9. Переставить местами столбцы с максимальной и минимальной суммой элементов
def action_9(a):
    if len(a) == 0:
        print('Error:Матрица пуста')
    else:
        raw_1 = raw_2 = s = 0
        for i in range(len(a)):
            s += a[i][0]
        max_s = min_s = s
        for i in range(len(a[0])):
            s = 0
            for j in range(len(a)):
                s += a[j][i]
            if s > max_s:
                min_s = s
                raw_1 = i
            if s < min_s:
                min_s = s
                raw_2 = i
        for i in range(len(a)):
            a[i][raw_1], a[i][raw_2] = a[i][raw_2], a[i][raw_1]
    return a


# 10. Вывести текущую матрицу


def action_10(a):
    for i in range(len(a)):
        print('[', end='')
        for j in range(len(a[i]) - 1):
            print('{:>4}'.format(a[i][j]), ',', end='')
        print('{:>4}'.format(a[i][j + 1]), ']')
    input('press enter to continue')
    return a


# inspection Exception
def input_control():
    global t
    try:
        t = int(input('Ввести число 0-10\n>>>'))
    except:
        input_control()


list1 = []

while 1:
    t = -1

    for k in range(1, 11):
        print(menu(k))
    print("0.Выход")
    while t < 0 or t > 10:
        input_control()
    print(menu(t))
    list1 = result(t)
    if t == 0:
        break
    # time.sleep(5)
