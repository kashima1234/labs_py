def Octal(number):
    octal_num = 0
    count_val = 1
    dno = float(number)
    while dno != 0:
        remainder = dno % 8
        octal_num += remainder * count_val
        count_val = count_val *10
        dno //= 8
    return octal_num
def decToHex(dec_value):
    while float(dec_value) > 0:
        hex_value = float(dec_value) % 16
        dec_value = float(dec_value) // 16
    return getHexChar(hex_value)
def getHexChar(dec_digit):
    if float(dec_digit) < 10:
        return dec_digit
    if float(dec_digit) == 10:
        return "A"
    if float(dec_digit) == 11:
        return "B"
    if float(dec_digit) == 12:
        return "C"
    if float(dec_digit) == 13:
        return "D"
    if float(dec_digit) == 14:
        return "E"
    if float(dec_digit) == 15:
        return "F"

arr_dec = []
arr_oct = []
arr_hex = []
with open ('proba1.txt','r') as input_:
    with open ('resenie1.txt', 'w') as output:
        line = input_.read()
        words = line.split()
        a = 0
        for word in words:
            if '.' in word and ('0' in word or '1' in word or '2' in word
                                or '3' in word or '4' in word or '5' in
                                word or '6' in word or '7' in word or
                                '8' in word or '9' in word):
                if float(word) < 0:
                    pass
                else:
                    arr_dec.append(word)
                    arr_oct.append(str(Octal(word)))
                    arr_hex.append((str(decToHex(word))))
                    print(word)

        for i in range(len(arr_dec)):
            output.write(arr_dec[i] + '\n')
        output.write('\n')
        for i in range(len(arr_oct)):
            output.write(arr_oct[i] + '\n')
        output.write('\n')
        for i in range(len(arr_hex)):
            output.write(arr_hex[i] + '\n')
