import re
text = ["12-2.5*3+7/2+90"]
l = len(text)
len_sentences = []
max_len = 0
for i in range(l):
  x = len(text[i])
  len_sentences.append(x)
  if x > max_len:
    max_len = x
'''
def print_calc(numbers, operations):                            # Функция, которая выводит арифметическое выражение, используя его числа и операции!
  l = len(numbers)
  print(float(numbers[0]),end="")
  for i in range(l-1):
    print(operations[i],end="")
    print(float(numbers[i+1]), end="")
  print("")
'''
def calculator(numbers, operations):                            # Функция, вычисляющая арифметическое выражение

  nums_plus_minus = []
  ops_plus_minus = []
  added = 0
  nums_plus_minus = [float(numbers[0])]
  for i in range(len(operations)):
    op = operations[i]
    if op == '*' or op == '/':
      if op == '*':
        nums_plus_minus[-1] = round(nums_plus_minus[-1]*float(numbers[i+1]), 4)
      else:
        nums_plus_minus[-1] = round(nums_plus_minus[-1]/float(numbers[i+1]), 4)
    else:
      nums_plus_minus.append(round(float(numbers[i+1]),3))
      ops_plus_minus.append(op)
  #print_calc(nums_plus_minus, ops_plus_minus)

  res = nums_plus_minus[0]
  for i in range(len(ops_plus_minus)):
    op =  ops_plus_minus[i]
    if op == '+':
      res += nums_plus_minus[i+1]  
    elif op == '-':
      res -= nums_plus_minus[i+1]  
    else:
      print("Unknown operation'{}'".format(op))
      return
  print("В результате получается:\n")
  print(res)

def find_nums_ops(str_):                                # Функция, которая находит числа и операции в арифметическом выражении!
  nums = re.split("[-\+\*/]", str_)
  ops = re.findall("[-\+\*/]", str_)
  return nums, ops
  


choice = None
while choice != '0':
    print('\n'
        '...\n'
        '\nНажмите\n'
        '\n'
        '1 - Выравнивание текста по левому краю.\n'                             
        '2 - Выравнивание текста по правому краю.\n'                            # выравнивание будет сделано в соответствии с самым длинным предложением
        '3 - Выравнивание текста по ширине.\n'                                  # выравнивание будет сделано в соответствии с самым длинным предложением
        '4 - Удаление заданного слова.\n'   
        '5 - Замена одного слова другим во всем тексте.\n'                 
        '6 - Вычисление арифметического выражения.\n'   
        '7 - Нахождения предложение с максимальным количеством слов, начинающихся на заданную букву.\n'   
        '0 - Выход\n'
        '...'
        '\n')
    choice = input('Выбор: ')           #Создаем наший выбор 

    if choice == '0':                   #Создаем  наший выход из программы                       
        print('Выход!')

    elif choice == '1':                 #Создаем условие,которое будет выполнятся при нажимании 1
        print('Выравнивание текста по левому краю!\n\n')
        for i in range(l):
          print(text[i])
        
        
    elif choice == '2':                 #Создаем условие,которое будет выполнятся при нажимании 2
        print('Выравнивание текста по правому краю!\n\n')
        l = len(text)
        len_sentences = []
        max_len = 0
        for i in range(l):
          x = len(text[i])
          len_sentences.append(x)
          if x > max_len:
            max_len = x
        for i in range(l):
          len_spaces = max_len - len_sentences[i]       #Расчет количества необходимых пробелов
          spaces = " "*len_spaces
          print(spaces+text[i])
        
    elif choice == '3':                 #Создаем условие,которое будет выполнятся при нажимании 3
        print('Выравнивание текста по ширине!\n\n')
        l = len(text)
        len_sentences = []
        max_len = 0
        for i in range(l):
          x = len(text[i])
          len_sentences.append(x)
          if x > max_len:
            max_len = x
        for i in range(l):
          words = text[i].split()
          num_spaces = len(words)-1
          if num_spaces == 0:
            print(text[i])
            continue
          len_spaces = max_len - len_sentences[i]
          spaces_to_add = int(len_spaces/num_spaces)
          for j in range(len(words)-1):
            spaces = " "*(spaces_to_add+1)
            if j < (len_spaces%num_spaces):
              spaces+= " "
            print(words[j]+spaces, end="")
          print(words[-1])
       

    elif choice == '4':                 #Создаем условие,которое будет выполнятся при нажимании 4
        print('Удаление заданного слова!')
        new_text = []
        d_word = input("Пожалуйста, введите слово, которое вы хотите удалить: ")
        print("Новый текст:")
        re_exp = "[^a-zA-Z]{}[^a-zA-Z]|^{}[^a-zA-Z]|[^a-zA-Z]{}$".format(d_word, d_word, d_word)
        for i in range(l):
          words = text[i].split()

          while d_word in words:
            words.remove(d_word)              #Удалить выбранное слово
          line = ""
          if len(words) > 0:
            line = words[0]
            for w_ in range(1, len(words)):
              line+=" "+words[w_]

          new_text.append(line)
          print(line)
        text = new_text

    elif choice == '5':                 #Создаем условие,которое будет выполнятся при нажимании 5
        print('Замена одного слова другим во всем тексте!')
        new_text = []
        old_word = input("Пожалуйста, введите слово, которое вы хотите заменять: ")
        new_word = input("Каким словом вы хотите его заменить: ")
        print("\nНовый текст:\n\n")
        for i in range(l):
          words = text[i].split()
          for j in range(len(words)):
            if words[j] ==  old_word:         #Замените выделенное слово
              words[j] = new_word
          line = ""
          if len(words) > 0:
            line = words[0]
            for w_ in range(1, len(words)):
              line+=" "+words[w_]

          new_text.append(line)
          print(line)
        text = new_text
        
        
    elif choice == '6':                 #Создаем условие,которое будет выполнятся при нажимании 6
        #print('Вычисление арифметического выражения!')
        pat = r'[0-9\-+\*/.]+'
        arithmatic_exp = None
        for line in text:
          words = re.findall(pat, line)
          for w in words:
            if re.search(r'[0-9]', w) and re.search(r'[-+\*/]', w):       # Чтобы убедиться, что выражение имеет числа и операции, а не только число
              arithmatic_exp = w
              break
          if arithmatic_exp !=None:
            break
        if arithmatic_exp == None:
          print("В этом тексте нет арифметического выражения.")
          print("Вы можете добавить арифметическое выражение и повторить попытку!")
          continue
        nums, ops = find_nums_ops(arithmatic_exp)
        #print("Арифметическое выражение в тексте:")
        #print(arithmatic_exp)
        calculator(nums, ops)


    elif choice == '7':                 #Создаем условие,которое будет выполнятся при нажимании 7
        print('Нахождения предложение с максимальным количеством слов, начинающихся на заданную букву!')
        letter = input("Введите букву: ")
        while len(letter)!=1:
          print("Вы вводите пустую строку или более одной буквы")
          print("Пожалуйста, попробуйте еще раз!")
          letter = input("Введите букву: ")
        re_exp = r'\b{}\w+'.format(letter)
        max = 0
        max_id = -1
        for i in range(len(text)):
          words = re.findall(re_exp, text[i])
          if len(words)> max:
            max = len(words)
            max_id = i
        if max_id == -1:
          print("В этом тексте нет слов, начинающихся на букву '{}'".format(letter))
        else:
          print("Предложение с максимальным количеством слов, начинающихся на заданную букву:\n")
          print(text[max_id])
          print("В этом предложении есть {} слова/слов, начинающиеся с буквы {}".format(max, letter))



    else:                               #Создаем условие,которое будет выполнятся при нажимании неправильный выбор
        print("Вы ввели неправильный выбор!")
