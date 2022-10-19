a = float(input('Введите начало интервала: '))
b = float(input('Введите конец интервала: '))
c = float(input('Введите шаг: '))
print(' --------------------------------')
print('|    x     |    y1    |    y2    |')
x = a
pmax = 512*x**10-1280*x**8-1120*x**6-400*x**4-5*x**2-1
pmin = 512*x**10-1280*x**8-1120*x**6-400*x**4-5*x**2-1
def frange(a, b, c):
    while a < b:
        yield a
        a += c
for a in frange(a, b+c, c):
    p = 512*x**10-1280*x**8-1120*x**6-400*x**4-5*x**2-1
    y1 = a
    y2 = p*a
    print('|{:6.3g}    |{:6.3g}    |'.format(a, y2, ))
while x <= b:
    
    if p > pmax:
        pmax = p
    if p < pmin:
        pmin = p
    x += c
y_axis = 60
print('Введите засечек (от 4 до 8): ',end='')
z = int(input())
while z < 4 or z > 8:
    print('Введите засечек (от 4 до 8): ',end='')
    z = int(input())
CenaDel = (pmax-pmin)/(z-1)
print(" "*8)
i=a
dlPr = 60
dlCher = int(dlPr / (z-1))
#Выводим значения над осью OY
print(" "*8,end='')
if z < 4 or z > 8:
    dlCher -= 1
for i in range(z):
    t = pmin + i * CenaDel
    if i==0:
        print('{:.5}'.format(t),end='   ')
        if z < 8:
            print("     ",end='')
    else:
        print(('{: ^' +str(dlCher+1)+'.5}').format(t),end="")
print()
print(" "*9 + "|" +("-"*int(60/(z-1))+"|")*(z-1))
l = 1*(int(60/(z-1)+1)*(z-1))
i=a
polLen = pmax+pmin
while i <= b:
    print('{: ^9.3}'.format(i)+"|",end='')
    f = 512*i**10-1280*i**8-1120*i**6-400*i**4-5*i**2-1
    pr = int(l*(f-pmin)/polLen)
    if pmin*pmax>0:
        print(" "*pr + "*")
    else:
        p0 = int(l*(0-pmin)/polLen)
        if p0<pr:
            print(" "*(p0) + "|" + " "*(pr-p0-2) + "*")
        if p0==pr:
            print(" "*(p0)+"|*")
        if p0>pr:
            print(" "*(pr) + "*" + " "*(p0-pr-1) + "|")
    i+=step






