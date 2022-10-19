
#лаб 5


from re import M


n = 1#Счётчик
x = float(input("Введите x = "))
t = 1#член суммы ряда
y = 1#Сумма
e = float(input("Точность = "))
maxi = int(input("Максимальное количество итераций = "))
step = int(input("Шаг печати = "))

#табличка!
print("-----------------------------------")
print("|  №  |      t      |      y      |")
print("|---------------------------------|")
print(f"| {n}" + (4 - len(str(n))) * " " + f"| {t:g}" + (12 - len(f"{t:g}")) * " " + f"| {y:g}" +
              (12 - len(f"{y:g}")) * " " + "|")

while abs(t) > e and n < maxi:    #пока член ряда больше заданной точности и счётчик меньше максимальной итерации
    n += 1
    t = ((x)**n)/n
    #t = t * x * (n-1)/n
    y += t
    if (n - 1) % step == 0:   #вывод элементов, соответствующих шагу
        print(f"| {n}" + (4 - len(str(n))) * " " + f"| {t:g}" + (12 - len(f"{t:g}")) * " " + f"| {y:g}" +
              (12 - len(f"{y:g}")) * " " + "|")    #табличка

print("-----------------------------------")

if abs(t) <= e:      #проверка
    print(f"Сумма бесконечного ряда - {y:g}, вычислена за {n} итераций")
else:
    print("За указанное число итераций необходимой точности достичь не удалось")







    ''' hello world how are you i hope  that i can do anything for my self 
    i hope that i can die this day this is my bigest wish in this life i dont need anything else 
    my god help me  make me disappeaer form this life i beg you i beg you i beg you i beg you i beg you i beg you 
    i beg you , i wanna commit sucide next year i swear i will , i cant stand this life its bigger than me 
    and in general i dont wanna live i get tired, so hope someone kill me or allah will make me disappear 
    from this life    ya allah hear me i beg you i beg you i beg you i beg  you i beg you 
    i swear i that i get tired from this life i dont live even i am richest man in thr world 
    so i repeat and say i wanna disappear from this lifeeeee  , i wanna that a lot of people 
    will say commit sucide but unfortunately i dont wanna go to hell cuz my god will make go to hell 
    if i kill my self             


    




    '''