 
# лаба 7 - вариант 2 - к п. 5, 6 - 1 и 2

def menu(): #меню
    print()
    print("1. Очистить список и ввести его с клавиатуры")
    print("2. Добавить элемент в произвольное место списка")
    print("3. Удалить произвольный элемент списка (по номеру)")
    print("4. Очистить список")
    print("5. Поиск элемента с наибольшим числом английских гласных букв")
    print("6. Замена всех гласных английских букв на заглавные")


def fool_num(x):  # защита от дурака
    while 1:
        t = input()
        if x == 0:  # проверка на дробные числа
            if not t.replace('.', '1').replace('-', '1').isdigit():
                print("Введены неправильные данныею Попробуйте еще раз. ")
            else:
                if float(t) % 1 < 1e-6:  # проверка на целые числа
                    return int(t)
                else:
                    return float(t)
        if x == 1:  # проверка на целые числа
            if not t.replace('-', '1').isdigit():
                print("Введены неправильные данныею Попробуйте еще раз. ")
            else:
                return int(t)
        if x == 2:  # проверка на натуральные числа
            if not t.isdigit():
                print("Введены неправильные данныею Попробуйте еще раз. ")
            else:
                return int(t)


def one():
    print("Введите размер массива: ", end='')
    n = fool_num(2)
    b = [''] * n
    for i in range(n):
        b[i] = str(input(f"Введите {i + 1} элемент массива: "))
    return b


def two(b: list):
    if len(b) == 0:
        print("Массив пуст")
    print("Введите номер элемента, в который хотите добавить элемент: ", end='')
    n = fool_num(2)
    if n > len(b):
        print("Элемента с таким индексом нет в массиве")
        return b
    b.append(0)
    for i in range(len(b) - 1, n, -1):  # сдвиг массива
        b[i] = b[i - 1]
    b[n] = str(input("Введите значение элемента: "))
    return b


def three(b: list):
    if len(b) == 0:
        print("Массив пуст")
    print("Введите номер элемента, который хотите удалить: ", end='')
    n = fool_num(2)
    if n > len(b):
        print("Элемента с таким индексом нет в массиве")
        return b
    for i in range(n, len(b) - 1):  # сдвиг массива
        b[i] = b[i + 1]
    return b[:len(b) - 1]  # возврат массива без ненужных элементов


def five(b: list):
    if len(b) == 0:
        print("Массив пуст")
        return b
    m = 0  # максимум
    mi = -1  # индекс макс. элемента
    vowel = ['A', 'E', 'I', 'O', 'U', 'Y']  # гласные
    for i in range(len(b)):
        c = 0
        for j in vowel:
            c += b[i].count(j) + b[i].count(j.lower())  # суммирование заглавных и строчных гласных
        if c > m:  # нахождение максимального элемента
            m = c
            mi = i
    if mi != -1:
        print(f"{b[mi]} - элемент с наибольшим числом английских гласных букв ({m})")
    else:
        print("В массиве нет строк с английскими гласными буквами")


def six(b: list):
    if len(b) == 0:
        print("Массив пуст")
        return b
    vowel = ['A', 'E', 'I', 'O', 'U', 'Y']  # гласные
    for i in range(len(b)):
        for k in vowel:
            b[i] = b[i].replace(k.lower(), k)  # процесс замены
    return b


# основная часть
a = []  # массив
print()
while 1:
    menu()
    print("Выберите пункт из меню: ", end='')
    q = fool_num(2)
    if 0 == q or q > 7:
        print("Введены неправильные данные. Выберите пункт (1-6). ")
        continue
    if q == 1:
        a = one()
    if q == 2:
        a = two(a)
    if q == 3:
        a = three(a)
    if q == 4:
        a = []
    if q == 5:
        five(a)
    if q == 6:
        a = six(a)
    print(a)
