#Пискунов Панте. Лабораторная работа №9
alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_to_index = dict(zip(alphabet,range(len(alphabet))))      #Определяем словарь с индексами
index_to_letter = dict(zip(range(len(alphabet)),alphabet))      #Oпределяем индекс к алфавиту
def encrypt(message,key):       #Шифруем строку
    encrypted = ''
    #Разделяем сообщение по длине ключа
    split_message = [message[i:i + len(key)]for i in range(0,len(message),len(key))]
    for each_split in split_message:
        i = 0
        #Преобразуем сообщение в индекс и добавить ключ (мод 26)
        for letter in each_split:
            number = (letter_to_index[letter]+letter_to_index[key[i]])%len(alphabet)
            encrypted += index_to_letter[number]
            i += 1
    return encrypted
def decrypt(cipher,key):    #Расшифруем строку
    decrypted = ''
    split_cipher = [cipher[i:i + len(key)]for i in range(0,len(cipher),len(key))]
    for each_split in split_cipher:
        i = 0
        for letter in each_split:
             number = (letter_to_index[letter]-letter_to_index[key[i]])%len(alphabet)
             decrypted += index_to_letter[number]
             i += 1
    return decrypted
choice = None
while choice != '0':
    print('\n'
          '...\n'
          '\nНажмите\n'                                             #Создаем  меню
          '\n'
          '1 - Введите строки.\n'
          '2 - Настройка шифрующего алгоритма.\n'
          '3 - Шифрование строки,используя шифр Виженера.\n'
          '4 - Расшифровывание строки.\n'
          '...'
          '\n')
    choice = input('Выбор: ')
    if choice == '1':                           #Вводим строку
        message = input('Введите строки: ')
        print('Ваша строка: ',message)
    elif choice == '2':                         #Вводим ключ
        key = input('Введите ключ: ')
        print('Ваша строка: ',message)
        print('Ваш ключ:',key)
    elif choice == '3':                         #Печатаем зашифрованную строку
        try:
            encrypted_message = encrypt(message,key)
            print('Ваша строка: ',message)
            print('Ваш ключ:',key)
            print('Зашифрованная строка: ',encrypted_message)
        except:
            print('Пожалуйста,сначало введите строку и ключ,потом используйте этот шаг!')
    elif choice == '4':                         #Печатаем расшифрованную строку
        try:
            decrypted_message = decrypt(encrypt(message,key),key)
            print('Зашифрованная строка: ',encrypted_message)
            print('Ваш ключ:',key)
            print('Начальная строка: ',decrypted_message)
        except:
            print('Пожалуйста,сначало зашифруйте строку,потом используйте этот шаг!')
