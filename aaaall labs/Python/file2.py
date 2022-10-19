with open('proba2.txt', 'r') as input1:
    with open('proba3.txt', 'r') as input2:
        with open('resenie2.txt', 'w') as output1:
            for line1 in input1:
                output1.write(line1)
                for line2 in input2:
                    output1.write(line2)
with open('resenie2.txt', 'r') as output1:
    with open('resenie3.txt', 'w') as output2: 
        for line in output1:
            x = int(line)
            if x == 12:
                output2.write(('XII'+'\n').center(3))
            elif x == 20:
                output2.write(('XX'+'\n').center(3))
            elif x == 30:
                output2.write(('XXX'+'\n').center(3))
            elif x == 40:
                output2.write(('XL'+'\n').center(3))
            elif x == 50:
                output2.write(('L'+'\n').center(3))
            elif x == 100:
                output2.write(('C'+'\n').center(3))
            elif x == 500:
                output2.write(('D'+'\n').center(3))
            

