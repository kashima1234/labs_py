#Панте Пискунов. Лабораторная работа №11
import pickle
choice = None
clear = "\n" * 5
books = None
keys = ["Name", "Author", "Year"]
while choice != '0':
    print('\n'
          '...\n'
          '\nНажмите\n'                                             #Создаем  меню
          '\n'
          '1 - Создание БД.\n'
          '2 - Добавление записи в БД.\n'
          '3 - Вывод всей БД.\n'
          '4 - Поиск записи по одному полю.\n'
          '5 - Поиск записи по двум полям.\n'
          '...'
          '\n')
    choice = input('Выбор: ')
    if choice == '1':																							#Создаем  БД
        print(clear)
        if books == None:		#Создаем базу данных																				#Если БД ещё не создана!
          books = "book.bin"
          print('Вы создали новую базу данных')
          f = open(books, "wb")
          f.close()
        else:
          print('БД уже Создана!') 
    elif choice == '2':																							#Добавление записи в БД
        print(clear)
        if books == None:																						#Если БД ещё не создана!
          print('БД ещё не создана!')
          print('Сначала вам нужно создать базу данных!')
          continue
        with open(books, 'ab') as file_:     #Добавляем запис в базу данных
          print("Добавить запис в базу данных")
          name = input('Название книга: ')
          author = input('Имя автора: ')
          year = input('Год издания: ')
          # file.seek(0)
          # file.write(b'\n')
          # file.write(bytes(l.encode()))
          dict_ = {"Name": name, "Author":author, "Year": year}
          pickle.dump(dict_, file_)
          file_.close()
        print("Добавили новой запис в базу данных:")
        #print(f"{idx}- Name: {name}, Author: {author}, Year: {year}")
        print("Name: {}, Author: {}, Year: {}".format(name, author, year))
    elif choice == '3':																							#Вывод всей БД
        print(clear)
        if books == None:																						#Если БД ещё не создана!			
          print('БД ещё не создана!')
          print('Сначала вам нужно создать базу данных!')
          continue

        print("Вывод всей БД ...")
        with open(books,'rb') as file_: #Выводим всей БД на экране
          idx = 0
          while True:
            try:
                data_ = pickle.load(file_)
                name = data_["Name"]
                author = data_["Author"]
                year = data_["Year"]
                idx+=1
                #print(f"{idx}- Name: {name}, Author: {author}, Year: {year}")
                print("{}- Name: {}, Author: {}, Year: {}".format(idx, name, author, year))
            except EOFError:
                break
          if idx ==0:
            print("База данных пуста!")
          file_.close()
    elif choice == '4':			#Поиск записи по одному полю																			#Поиск записи по одному полю
        print(clear)
        if books == None:																						#Если БД ещё не создана!
          print('БД ещё не создана!')
          print('Сначала вам нужно создать базу данных!')
          continue
        print("Поиск записи по одному полю: Нажмите"
          '\n'
          '1 - Поиск по названию книги.\n'
          '2 - Поиск по автору.\n'
          '3 - Поиск по год издания.\n'
          '\n')
        num = int(input("... "))											#Вибрать полю по которому будим искать!
        key = keys[num-1]
        d = input("данные, которые вы хотите найти: ")							#Написать данные, которые мы хотим искать!
        with open(books,'rb') as file_:
          idx = 0
          while True:
            try:
                data_ = pickle.load(file_)
                if data_[key]==d:
                  name = data_["Name"]
                  author = data_["Author"]
                  year = data_["Year"]
                  idx+=1
                  #print(f"{idx}- Name: {name}, Author: {author}, Year: {year}")
                  print("{}- Name: {}, Author: {}, Year: {}".format(idx, name, author, year))
            except EOFError:
                break

          file_.close()
          #print(f"Мы нашли {idx} совпадений!")
          print("Мы нашли {} совпадений!".format(idx))
    elif choice == '5':			#Поиск записи по двум полям																				#Поиск записи по двум полям
        print(clear)
        if books == None:																						#Если БД ещё не создана!
          print('БД ещё не создана!')
          print('Сначала вам нужно создать базу данных!')
          continue
        print("Поиск записи по первому полю: Нажмите"
          '\n'
          '1 - Поиск по названию книги.\n'
          '2 - Поиск по автору.\n'
          '3 - Поиск по год издания.\n')
        num = int(input("... "))																									#Випрать первую полю по которому будим искать!
        key1 = keys[num-1]
        d1 = input("данные, которые вы хотите найти по этму полю: ")							#Написать данные, которые мы хотим искать!

        print("Поиск записи по второму полю: Нажмите"
          '\n'
          '1 - Поиск по названию книги.\n'
          '2 - Поиск по автору.\n'
          '3 - Поиск по год издания.\n')
        num = int(input("... "))																									#Випрать вторую полю по которому будим искать!
        key2 = keys[num-1]
        d2 = input("данные, которые вы хотите найти по этму полю: ")							#Написать данные, которые мы хотим искать!
        with open(books,'rb') as file_:
          idx = 0
          while True:
            try:
                data_ = pickle.load(file_)
                if data_[key1]==d1 and data_[key2]==d2:
                  name = data_["Name"]
                  author = data_["Author"]
                  year = data_["Year"]
                  idx+=1
                  #print(f"{idx}- Name: {name}, Author: {author}, Year: {year}")
                  print("{}- Name: {}, Author: {}, Year: {}".format(idx, name, author, year))
            except EOFError:
                break

          file_.close()
          #print(f"Мы нашли {idx} совпадений!")
          print("Мы нашли {} совпадений!".format(idx))
    elif choice == '6':
        if books == None:
            books = change_file_name()
        else:
            print('Вы уже открилы файл!')
