# Гао Шан ИУ7 11Б
# gaosh@student.bmstu.ru
import re


# def result(num):
#     numbers = [action_0, action_1, action_2, action_3, action_4, action_5, action_6, action_7]
#     return numbers[num](str1)

# inspection Exception
def input_control():
    global cmd
    max_cmd = 7
    cmd = -1
    try:
        while cmd < 0 or cmd > max_cmd:
            cmd = int(input('Ввести число 0-7\n>>>'))
    except:
        input_control()


menu = {
    0: "0. Выход",
    1: "1. Выбрать файл для работы",
    2: "2. Инициализировать базу данных",
    3: "3. Вывести содержимое базы данных",
    4: "4. Добавить запись в базу данных",
    5: "5. Поиск по одному полю",
    6: "6. Поиск по двум полям",
}


def action_0(a, b):
    return a


def action_1(a, b):
    global filename
    while True:
        filename = input('Выбрайте файл для работы')
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                print('Файл успешно выбран')
                break
        except:
            print("Не удалось открыть файл")
            continue


def action_2(a, b):
    global dict, head
    if filename:
        dict = {}
        with open(filename, 'r+', encoding='utf-8') as f:
            head = f.readline().strip().split(',')
            for line in f:
                line = line.strip().split(',')
                dict[line[0]] = line
        print('База данных успешно инициализирована')
    else:
        print('Файл ещё не выбран')


def action_3(dict, head):
    if filename:
        for el in head[:-1]:
            print('{:<10}'.format(el)+',',end='')
        print(head[-1])
        for i, j in dict.items():
            for el in j[:-1]:
                print('{:<12}'.format(el)+',',end='')
            print(j[-1])
    else:
        print('Файл ещё не выбран')
    
    return 1


def action_4(dict, head):
    return 1


def action_5(dict, head):
    return 1


def action_6(dict, head):
    return 1


dict = {}
# filename = False
filename = 'lab12.txt'
head = []
# for i, j in dict.items():
#     print(i, j)
# print(head)

while 1:
    for k in range(1, len(menu)):
        print(menu.get(k, None))
    print("0.Выход")
    input_control()
    print(menu.get(cmd, None))
    if cmd == 0:
        break
    act = 'action_' + str(cmd)
    locals()[act](dict, head)
    # time.sleep(5)
