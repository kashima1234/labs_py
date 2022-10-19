fin1 = open('in1.txt', 'r')
fin2 = open ('in2.txt', 'r')
fout1 = open('out1.txt', 'w')
i = 0
j = 0
eof1 = False
eof2 = False
while True:
    num1 = fin1.readline()
    num2 = fin2.readline()
    if (num1 == ''):
        eof1 = True
        break
    if(num2 == ''):
        eof2 = true
        break
    if (not eof1 and not eof2):
        num1 = int(num1)
        num2 = int(num2)
        if (num1 < num2):
            fout1.write(str(num1)+'\n')
            i += 1
        else:
            fout1.write(str(num2)+'\n')
            j += 1
if (not eof1):
    while num1 != '':
        num1 = int(num1)
        fout1.write(str(num1)+'\n')
        num1 = fin1.readline()
if (not eof1):
    while num2 != '':
        num2 = int(num2)
        fout1.write(str(num2)+'\n')
        num2 = fin1.readline()
fout1.close()
fin1.close()
fin2.close()
        












