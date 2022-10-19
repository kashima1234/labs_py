#Пискунов Панте. Лабораторная работа №6
#y = ((-1)**n)*(((2*n)-1)/(factorial(2*n)))*(x**(2*n))
from math import factorial,sqrt
import re,itertools
A = []                    #Создаем пустой список
choice = None
while choice != '0':
    print('\n'
        '...\n'
        'A = ((-1)**n)*(((2*n)-1)/(factorial(2*n)))*(x**(2*n))\n'
        '\nНажмите\n'
        '\n'
        '1 - Проинициализировать список первыми N элементами заданного ряда.\n'
        '2 - Добавить элемент в произвольное место списка.\n'
        '3 - Удалить произвольный элемент из списка.\n'
        '4 - Удалить все элементы в списке A.\n'
        '5 - Найти значение К-го экстремума в списке,если он являестя списком чисел.\n'     #Создаем нашее меню по условию
        '6 - Найти возростающую последовательность простых чисел в списке.\n'
        '7 - Найти наибольшая последовательность слов,где каждое последующее слово получается из букв предыдушего.\n'
        '0 - Выход\n'
        '...'
        '\n')
    choice = input('Выбор: ')           #Создаем наший выбор 
    if choice == '0':                   #Создаем  наший выход из программы                       
        print('Выход!')
    elif choice == '1':                 #Создаем условие,которое будет выполнятся при нажимании 1
            N = int(input('Введите сколько элементов хотите в ряде: '))
            x = int(input('Введите значение для x: '))
            for i in range (0,N):
                t = ((-1)**i)*(((2*i)-1)/(factorial(2*i)))*(x**(2*i))
                A.append(str(t))
            print('Список ваших элементов: ',A)
            m = len(A) 
    elif choice == '2':         #Создаем условие,которое будет выполнятся при нажимании 2
        if A == []:
            print('Список пустой!')
            x = list(map(str,input('Введите элементы: ').split()))
            A = x
            print('Список ваших элементов: ',A)
            m = len(A)
        else:
            x = int(input('2 - Введите на какое место хотите ввести элемент: '))
            y = input('    Введите элемент, который вы хотите ввести: ')
            A.insert(x,y)
            print('Список ваших элементов: ',A)
            m = len(A)
    elif choice == '3':         #Создаем условие,которое будет выполнятся при нажимании 3
        y = input('Введите элемент,который хотите удалить: ')
        if y in A:
            A.remove(y)
            print('Обновленный список: ',A)
            m = len(A)
        else:
            print('Введеного элемента ',y,'нет в списке')
    elif choice == '4':         #Создаем условие,которое будет выполнятся при нажимании 4
        A.clear()
        print('Вы удалили все элементы в списке A =',A)
    elif choice == '5':         #Создаем условие,которое будет выполнятся при нажимании 5
        if A == []:
            print('Список пустой!')
        else:
            try:
                print('Значения К-го экстремума в списке:')
                A = list(map(float,A))
                m = len(A)
                for i in range (1,m-1):       #Создаем условие,которое будет искать число которое одновременно больше предыдушего и меньше следующего         
                    if ((A[i-1] < A[i] and A[i] > A[i+1]) or (A[i-1] > A[i] and A[i] < A[i+1])):
                        print(A[i],end=' ')
            except:
                print('Нет,потому что в списке содержатся элементы, не являющиеся числами!')
    elif choice == '6':         #Создаем условие,которое будет выполнятся при нажимании 6
        def is_prime(x):
            try:
                x = int(x)
                c = 0
                if x < 0 :
                  return False
                for i in range(1, x):
                  if x % i == 0:
                      c += 1
                if c==1:
                  return True
                return False
            except:
                return False
            
            return False
        if A == []:
            print('Список пустой!')
        else:
            try:
                numbers = [int(i) for i in A if i.isdigit()]
            except:
                print('В списке содержатся элементы, не являющиеся числами!')
            try:
                if numbers == []:
                    print('В списке нет целых чисел!')
                else:
                    prime = []
                    primes = []
                    i = 0
                    while i < len(A):
                      prime = []
                      while len(prime) == 0 and i < len(A):
                        if is_prime(A[i]):
                          prime = [A[i]]
                        i+=1
                      if i < len(A) and len(prime)>0:
                        while is_prime(A[i]) and int(A[i])>int(prime[-1]):
                          prime.append(A[i])
                          i+=1
                          if i == len(A):
                            break
                      primes.append(prime)
                    if len(prime) == 0:
                      print('В списке нет простых чисел!')
                    if len(primes) == 0:
                      print('В списке нет простых чисел!')
                    max = 0
                    idx = 0
                    for i in range(len(primes)):
                      if len(primes[i]) > max:
                        max = len(primes[i])
                        idx = i
                    print(primes[idx])
            except:
                pass
    elif choice == '7':         #Создаем условие,которое будет выполнятся при нажимании 7
            arr = A
            if arr == []:
                print('В списке нет слов!')
            else:
                idx = 0
                arrs = []
                prev = set(arr[idx])
                res = [arr[idx]]
                for i in range(1, len(arr)):
                    curr = set(arr[i])
                    if prev > curr:
                        res.append(arr[i])
                        prev = set(arr[i])
                    else:
                        arrs.append(res)
                        res = [arr[i]]
                        prev = set(arr[i])
                if len(res)!= 0:
                  arrs.append(res)
            
                if len(arrs) > 1:
                  max = 0
                  idx = 0;
                  for i in range(len(arrs)):
                    if max < len(arrs[i]):
                      max = len(arrs[i])
                      idx = i
                  print(arrs[idx])
                else:
                    print("В списке нет такой последовательности!")

            
            if len(res) > 1:
                print(res)
            else:
                print("В списке есть такая последовательность!")
    else:                       #Создаем условие, когда вывели неверный номер
        print('Введенного номера нет!',choice)
input('\nНажмите Enter.')       #Выходим из программы



