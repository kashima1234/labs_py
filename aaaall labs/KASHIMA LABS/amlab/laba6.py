# Уянга Амина ИУ7И-12Б
# лаб 6 вариант 25 (к п. 77 - 5)

using_list = []

while True:
    # Меню
    print("1. Проинициализировать список первыми N элементами заданного в л/р 5 ряда.")
    print("2. Очистить список и ввести его с клавиатуры.")
    print("3. Добавить элемент в произвольное место списка.")
    print("4. Удалить произвольный элемент из списка (по номеру).")
    print("5. Очистить список.")
    print("6. Найти значение K-го экстремума в списке.")
    print("7. Последовательность чисел, в которой все, начиная с 3-го, являются суммой двух предыдущих. ")
    print("8. Выйти.")

    while True:
        print("-" * 80)
        while True:
            command_str = input(" Введите номер команды: ")
            if not command_str.isdecimal():
                print("Введены неправильные данные. Попробуйте еще раз. ")

            else:
                break

        command = int(command_str)
        # проверка
        if command < 1 or command > 8:
            print("Неверный номер команды. Допустимые номера команд: 1-8.")
        else:
            break


    if command == 1:
        if using_list:
            print("Массив уже инициализирован. Очистите его.")
            enter = input("Нажмите enter чтобы продолжить. ")
        else:
            while True:
                # проверка
                N_str = input("Введите количество элементов в массиве: ")
                if not N_str.isdecimal():
                    print("Неправильный ввод. Допустимы только целые положительные числа.")
                else:
                    N = int(N_str)
                    break

            detorminate = 1   # знаменатель
            for i in range(N):
                using_list.append(1 / detorminate)
                detorminate *= i + 1

            print("Текущий массив: ", end="")
            for i in range(len(using_list)):
                print("{:.5g} ".format(using_list[i]), end="")
            print(" ")
            enter = input("Нажмите enter чтобы продолжить. ")


    elif command == 2:
        using_list.clear()
        while True:
            # Проверка корректности ввода
            N_str = input("Введите количество элементов в массиве: ")
            if not N_str.isdecimal():
                print("Введены неправильные данные. Попробуйте еще раз. ")
            else:
                N = int(N_str)
                break

        for i in range(N):
            while True:
                a = input("Введите элемент массива: ")
                a_temp = a
                if not a:
                    print("Недопустимый ввод. Допустимы только числа.")
                    continue
                if a[0] == "-":
                    a = a.replace("-", "", 1)
                elif a[0] == "+":
                    a = a.replace("+", "", 1)
                if "e" in a:
                    if a[0] == "e" or a[len(a) - 1] == "e" or not ("0" <= a[a.index("e") + 1] <= "9" \
                                or a[a.index("e") + 1] == "-" or "0" <= a[a.index("e") - 1] <= "9" ):
                        print("Недопустимый ввод. Допустимы только числа.")
                        continue
                    elif a[a.index("e") + 1] == "-":
                        a = a.replace(a[a.index("e") + 1], "", 1)
                    a = a.replace("e", "", 1)
                if "." in a:
                    a = a.replace(".", "", 1)

                # проверка
                if not a.isdecimal():
                    print("Недопустимый ввод. Допустимы только числа.")
                else:
                    using_list.append(float(a_temp))
                    break

        print("Текущий массив: ", end="")
        for i in range(len(using_list)):
            print("{:.5g} ".format(using_list[i]), end="")
        print(" ")

        enter = input("Нажмите enter чтобы продолжить.")


    elif command == 3:
        if using_list:
            while True:
                # проверка
                i_str = input("Введите индекс элемента списка : ")
                if not i_str.isdecimal():
                    print("Неправильный ввод. Допустимы только числа.")
                else:
                    i = int(i_str)
                    if i < len(using_list):
                        break
                    else:
                        print("Ошибка. ")

            while True:
                a = input("Введите элемент массива: ")
                a_temp = a
                if not a:
                    print("Недопустимый ввод. Допустимы только числа.")
                    continue
                if a[0] == "-":
                    a = a.replace("-", "", 1)
                elif a[0] == "+":
                    a = a.replace("+", "", 1)
                if "e" in a:
                    if a[0] == "e" or a[len(a) - 1] == "e" or not("0" <= a[a.index("e") + 1] <= "9" \
                            or a[a.index("e") + 1] == "-" or "0" <= a[a.index("e") - 1] <= "9"):
                        print("Недопустимый ввод. Допустимы только числа.")
                        continue
                    elif a[a.index("e") + 1] == "-":
                        a = a.replace(a[a.index("e") + 1], "", 1)
                    a = a.replace("e", "", 1)
                if "." in a:
                    a = a.replace(".", "", 1)

                # проверка
                if not a.isdecimal():
                    print("Недопустимый ввод. Допустимы только числа.")
                else:
                    using_list.insert(i, float(a_temp))
                    break

            print("Текущий массив: ", end="")
            for i in range(len(using_list)):
                print("{:.5g} ".format(using_list[i]), end="")
            print(" ")
            enter = input("Нажмите enter чтобы продлжить. ")
        else:
            print("Массив не инициализирован. Заполните его с помощью других команд.")
            enter = input("Нажмите enter чтобы продолжить. ")


    elif command == 4:
        if using_list:
            while True:
                i_str = input("Введите номер элемента, который Вы хотите удалить: ")
                if not i_str.isdecimal():
                    print("Неправильный ввод. Допустимы только целые положительные числа.")
                else:
                    i = int(i_str)
                    if i < len(using_list):
                        break
                    else:
                        print("Ошибка. Выход за пределы массива.")

            using_list.pop(i)
            print("Текущий массив: ", end="")
            for i in range(len(using_list)):
                print("{:.5g} ".format(using_list[i]), end="")
            print(" ")
            enter = input("Нажмите enter чтобы продолжить. ")
        else:
            print("Массив не инициализирован. Заполните его с помощью других команд.")
            enter = input("Нажмите enter чтобы продолжить. ")


    elif command == 5:
        if using_list:
            using_list.clear()
            print("Текущий массив: ", using_list)
            enter = input("Нажмите enter чтобы продолжить. ")
        else:
            print("Массив не инициализирован. Заполните его с помощью других команд.")
            enter = input("Нажмите enter чтобы продолжить. ")


    elif command == 6:
        if using_list:
            while True:
                k_str = input("Введите номер экстремума: ")
                if not k_str.isdecimal():
                    print("Неправильный ввод. Допустимы только целые положительные числа.")
                else:
                    k = int(k_str)
                    break

            temp_k = 0
            # экстремум
            for i in range(1, len(using_list) - 1):
                if (using_list[i - 1] < using_list[i] > using_list[i + 1]) or \
                        (using_list[i - 1] > using_list[i] < using_list[i + 1]):
                    temp_k += 1

                if temp_k == k and k != 0:
                    print("К-ый экстремум равен {}.".format(using_list[i]))
                    break

            if temp_k != k or k == 0:
                print("В массиве не существует к-го экстремума.")

            print("Текущий массив: ", end="")
            for i in range(len(using_list)):
                print("{:.5g} ".format(using_list[i]), end="")
            print(" ")
            enter = input("Нажмите enter чтобы продолжить. ")

        else:
            print("Массив не инициализирован. Заполните его с помощью других команд.")
            enter = input("Нажмите enter чтобы продолжить. ")

    elif command == 7:
        if using_list:
            # временные массивы
            additional_array_1 = []
            additional_array_2 = []

            # поиск последовательности
            for i in range(len(using_list) - 3):
                for j in range(i + 2, len(using_list)):
                    if using_list[j] == using_list[j-2] + using_list[j-1]:
                        if additional_array_2:
                            additional_array_2.append(using_list[j])
                        else:
                            additional_array_2.append(using_list[j - 2])
                            additional_array_2.append(using_list[j - 1])
                            additional_array_2.append(using_list[j])

                    else:
                        if len(additional_array_2) > len(additional_array_1) and additional_array_2:
                            additional_array_1 = additional_array_2.copy()

                        additional_array_2.clear()

                if len(additional_array_2) > len(additional_array_1):
                    additional_array_1 = additional_array_2.copy()
                additional_array_2.clear()

            if additional_array_1:
                print("Нужная последовательность: ", additional_array_1)
            else:
                print("Такой последовательности нет.")

            print("Текущий массив: ", end="")
            for i in range(len(using_list)):
                print("{:.5g} ".format(using_list[i]), end="")
            print(" ")
            enter = input("Нажмите enter чтобы продолжить. ")

        else:
            print("Массив не инициализирован. Заполните его с помощью других команд.")
            enter = input("Нажмите enter чтобы продолжить. ")


    else:
        print("Работа завершена.")
        break
