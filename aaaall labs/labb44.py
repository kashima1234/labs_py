 
# Кашима Aхмед, иу7и-13б
# Лабораторная работа №4
#  

a = float(input('Введите начало интервала: '))
b = float(input('Введите конец интервала: '))             #  Выводим начало, конец и шаг интервала
c = float(input('Введите шаг: '))
print(' -----------------------------')
print('|    x     |       f(x)       |')
ymax = a ** 7 - a ** 6 + 8 * a ** 5 - 4 * a **  4 + 6 * a ** 3 + 2 * a ** 2 - 5 * a + 1
ymin =  a ** 7 - a ** 6 + 8 * a ** 5 - 4 * a **  4 + 6 * a ** 3 + 2 * a ** 2 - 5 * a + 1
i = a

# Sadly missing in the Python standard library, this function allows to use ranges,
#  just as the built-in function range(), but with float arguments

def frange(start, stop, step):             # A range function that accepts float increments
    steps = []
    while start <= stop :
        steps.append(start)          # The append() method is used to add a new object at the end of the list.
        start += step
    return steps                      

for i in frange(a, b, c):
    y = i ** 7 - i ** 6 + 8 * i ** 5 - 4 * i ** 4 + 6 * i ** 3 + 2 * i ** 2 - 5 * i + 1
    if y > ymax:
        ymax = y
    elif y < ymin:  # 2f mn ajl alarqam ycon its shap hlo                           #Создаем и вычисляем таблицу значения функции
        ymin = y
    print('|{: ^10.2f}|'.format(i), end='')                  # 1010 its for distance between numberrs firs part...  
    if(y >= 1e4): 
        print('{: ^18.4e}|'.format(y))                    # 18 its for dstance between numbers second part from first part
    else:
        print('{: ^18.4g}|'.format(y))                   # 18 for distance between nfirst part from first part 
    i += c   
print('  -----------------------------')
y_axis = 70  # its for dist. bet.. nums. abov sec..                              #Выводим длину оси y
z = int(input("Введите засечек (от 4 дo 8): "))     # Выводим засечек от 4 до 8
while z < 4 or z > 8:
    z = int(input("Введите засечек (от 4 дo 8): "))
mid = (ymax-ymin)/(z-1)                         #Вычисляем среднбюю точку в графике
print(" "*8 )                                    #Пробел 8  # *8 distance betweenfirst table and sec.
dl = int(y_axis / (z-1))                        #Вычисляем отсечки           
print(" "*8 ,end='')                              # *8this line for distance between numberss above second table ...
if z < 6:
    dl -= 1                                       # this line for distance between.,.1, 234434..
for i in range(z):
    t = ymin + i * mid                          #Выводим значения над осью OY
    if i == 0:
        print('{:.5}'.format(t),end='   ')
        if z < 6:
            print("    ",end='')           # this is distance between fist num and others num
    else:
        print(('{: ^' +str(dl+1)+'.5}').format(t),end="")
print()
print(" "*9 + "|" +("-"*int(80/(z-1))+"|")*(z-1))        # 1010 its for -- under second number..
l = 1*(int(70/(z-1)+1)*(z-1))                            # this is super important for second helf of programm./.
i = a
polLen = ymax - ymin                      # veribel
for i in frange(a, b, c):
    print('{: ^9.3}'.format(i)+"|",end='')      #this is for distancein first ...
    f =  i ** 7 - i ** 6 + 8 * i ** 5 - 4 * i ** 4 + 6 * i ** 3 + 2 * i ** 2 - 5 * i + 1   #Выводим значения для ОХ
    pr = int(l*(f-ymin)/ (polLen if polLen > 0 else 1))       # var 
    if ymin*ymax > 0:
        print(" "*pr + "*")
    else:
        p0 = int(l*(0-ymin)/polLen)      
        if p0 < pr:                 # *" |"
            print(" "*(p0) + "|" + " "*(pr-p0-2) + "*")    # @ * thisstar belong to second halaf 
        if p0 == pr:
            if f == 0:                                    #Рисуем график
                print(" "**(p0)+"+")
                print('Эту функцию сечет график в '.format(p0))
            elif f > 0:
                print(" "*(p0)+"|*")       #@| u *  belong to first helf of gra..                  
            else:
                print(" " * (p0 - 1) + "*|")              # eto toje belomge to gra ..
        if p0 > pr:
            print(" "*(pr) + "*" + " "*(p0-pr-1) + "|")
    i += c