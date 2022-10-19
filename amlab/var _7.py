""" 26 вар. """ 
 
# Импортирование корня 
from math import sqrt, trunc 
 
# Пустой список для последующей обработки 
cur_list = [] 
e = 10** (-8) 
 
# Тело программы 
while True: 
    # Меню 
    print("1. Очистить список и ввести его с клавиатуры") 
    print("2. Добавить элемент в произвольное место списка") 
    print("3. Удалить произвольный элемент из списка (по номеру)") 
    print("4. Очистить список") 
    print("5. Поиск элемента наибольшей длины, не содержащего цифр") 
    print("6. Замена всех заглавных гласных английских букв на строчные" ) 
    print("0. Выйти из программы", end="\n\n") 
 
    # Выбор пользователя 
    choice = input("Выберите пункт меню: ") 
    print() 
 
    # Проверка ввода пользователя 
    if not choice.isdigit() or (int(choice) < 0 or int(choice) > 7): 
        print("Неверный ввод", end="\n\n") 
 
    # Выход из программы 
    if choice == "0": 
        break 
 
    # Пункт меню 1 
    if choice == "1":
        # Ввод списка 
        while True: 
            flag = True 
            cur_list = list(input("Введите список в одну строчку, " 
                            "разделяя элементы пробелами: ").split()) 
            print() 
            for i in range(len(cur_list)): 
                if not flag: 
                    break 
                if cur_list[i] == "." or cur_list[i] == "e" or ( 
                        cur_list[i] == "E" or cur_list[i] == "+" or 
                        cur_list[i] == "-"): 
                    print("Неверно заданы элементы списка", end="\n\n") 
                    break 
                for ch in cur_list[i]: 
                    if not ch.isdigit() and ch != "." and ch != "e" and ( 
                            ch != "E" and ch != "+" and ch != "-"): 
                        print("Неверно заданы элементы списка", end="\n\n") 
                        flag = False 
                        break 
            else: 
                for ch in cur_list[-1]: 
                    if not ch.isdigit() and ch != "." and ch != "e" and ( 
                            ch != "E" and ch != "+" and ch != "-"): 
                        break 
                else: 
                    break 
 
        # Вывод списка 
        print("Текущий список: ", end="") 
        for i in range(len(cur_list)): 
            print("{:.2e}".format(float(cur_list[i])), end="  ") 
        print(end="\n\n") 
 
 
    # Пункт меню 2 
    if choice == "2": 
         
    # Пункт меню 3 
     if choice == "3": 
        # Ввод позиции в списке 
        while True: 
            N = input("Введите позицию, куда вы хотите добавить " 
                      "произвольный элемент: ") 
            print() 
            if N == "-" or N == "+": 
                print("Неверно задана позиция", end="\n\n") 
                continue 
            for ch in N: 
                if not ch.isdigit() and ch != "-" and ch != "+": 
                    print("Неверно задана позиция", end="\n\n") 
                    break 
            else: 
                break 
 
        # Ввод значения элемента 
        while True: 
            user_elem = input("Введите значение вашего элемента: ") 
            print() 
            if user_elem == "." or user_elem == "e" or ( 
                    user_elem == "E" or user_elem == "+" or 
                    user_elem == "-" or user_elem == " "): 
                print("Неверный ввод", end="\n\n") 
            else: 
                for ch in user_elem: 
                    if not ch.isdigit() and ch != "." and ch != "e" and ( 
                            ch != "E" and ch != "+" and ch != "-" and ch!= " "): 
                        print("Неверный ввод", end="\n\n") 
                        break 
                else: 
                    break 
 
        # Вставка элемента в нужную позицию 
        cur_list.insert(int(N), float(user_elem)) # 
 
        # Вывод списка 
        print("Текущий список: ", end="") 
        for i in range(len(cur_list)): 
            print("{:.2e}".format(float(cur_list[i])), end="  ") 
        print(end="\n\n") 
 
    # Пункт меню 4 
    if choice == "4": 
        # Ввод позиции в списке 
        while True: 
            N = input("Введите позицию элемента, который вы хотитк удалить: ") 
            print() 
            if N == "-" or N == "+": 
                print("Неверно задана позиция", end="\n\n") 
                continue 
            for ch in N: 
                if not ch.isdigit() and ch != "-" and ch != "+": 
                    print("Неверно задана позиция", end="\n\n") 
                    break 
            else: 
                break 
 
        # Удаление элемента в заданной позиции 
        cur_list.pop(int(N)) 
 
        # Вывод списка 
        print("Текущий список: ", end="") 
        for i in range(len(cur_list)): 
            print("{:.2e}".format(float(cur_list[i])), end="  ") 
        print(end="\n\n") 
 
    # Пункт меню 5 
    if choice == "5": 
        cur_list = [] 
 
        # Вывод списка 
        print("Текущий список: ", end="") 
        for i in range(len(cur_list)): 
            print("{:.2e}".format(float(cur_list[i])), end="  ") 
        print(end="\n\n") 
 
    # пункт меню 6 
    if choice == "6": 
        # Задание номера нужного экстремума 
        while True: 
            N = input("Введите целое K > 0: ") 
            print() 
            if not N.isdigit() or int(N) <= 0: 
                print("Неверно задан K", end="\n\n") 
            else: 
                break 
 
        # Определение экстремума под нужным номером 
        k = 0 
        if len(cur_list) <= 2: 
            print("Нельзя определить экстремумы, т.к длина списка" 
                  " недостаточная", end="\n\n") 
        elif len(cur_list) == 3: 
            if float(cur_list[1]) < float(cur_list[0]) and \
                    float(cur_list[1]) < float(cur_list[2])\
                    or float(cur_list[1]) > float(cur_list[0])\
                    and float(cur_list[1]) > float(cur_list[2]):
                k += 1 
                ext = float(cur_list[1]) 
                if int(N) == k: 
                    print("Значение экстремума {1:.2e} под номером {0}:" 
                          " ".format(k, float(cur_list[1])), end="\n\n") 
                else: 
                    print("Указанного K-го экстремума не существует", 
                          end="\n\n") 
            else: 
                print("Указанного K-го экстремума не существует", 
                      end="\n\n") 
        else: 
            for i in range(1, len(cur_list) - 1): 
                if float(cur_list[i-1]) < float(cur_list[i]) and \
                        float(cur_list[i+1]) < float(cur_list[i]) or \
                        float(cur_list[i]) < float(cur_list[i-1]) and \
                        float(cur_list[i]) < float(cur_list[i+1]):
                    k += 1 
                    ext = cur_list[i] 
                    if int(N) == k: 
                        print("Значение экстремума")