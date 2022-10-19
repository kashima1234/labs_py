a = int(input("Input number: "))

a_bin = bin(a)
# to gray
a_gray = a ^ (a >> 1)

# from gray to bin
a1 = a_gray
b = a1 >> 1
for i in range(len(bin(a)) - 2):
    a1 = a1 ^ b
#print(bin(b)[2:], bin(a_gray)[2:])
b = b >> 1

print('Bin: ', bin(a))
print('Gray: ', bin(a_gray))
print('Bin2: ', bin(a1))
