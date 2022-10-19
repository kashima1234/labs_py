
from ast import Bytes
from asyncore import write
from audioop import byteswap
from cgitb import text
from io import BytesIO
import os
from pickle import bytes_types 
import sys 
import json

def compute_readability(text):
    pass



def shifr():
    byte_s = int(input("choose how many byte in pixel 1/2/4/8 ?"))
    
    file = open ("text1.txt", "w", encoding= 'utf-8')
    file_01 = open ("pict.bmp", "w", encoding= 'utf-8')
    x = input ("Enter text :")
    print("lenghth of your texta: ", len(x))
    file.write(x)
    file.close()
    file_01.close()

    len_text = os.stat("text1.txt").st_size
    pict_len = os.stat("pict.bmp").st_size

    if len_text > (pict_len * byte_s/8 -54):
        print("text maybe long for coordinat in the same photo or format ")
        return 

    text = open("text1.txt ", "r")
    pict = open("pict.bmp", "rb")
    shifrpict = open("shifrpict.bmp", "wb")

    copied = pict.read(54)
    shifrpict.write(copied)

    
    mask_add(byte_s)

    text_mask, pict_mask = mask_add(byte_s)

#print('text: {0;b}; pict; {1;b}" .format(text_mask, pict_mask ))

    while True:
        sym = text
        if not sym:
            break
        #print("|nsym {0}, bin {1;b} ". format(sym, ord(sym)))
        sym = ord(sym)

        for byte_amount in range(0, 8, byte_s):
            pict_byte = int.from_bytes(pict.read(1), sys.beteorder) & pict_mask
            bits = sym &  text_mask
            bits >>= (8 - byte_s)


            #pri....

            pict_byte != bits
            pict_byte = pict_byte.to_byte(1, sys.byteorder)


            shifrpict,write(pict_byte)


            sym <<= bytes_types

    #pri    ........
    shifrpict.write(pict.read())
    text.close()
    pict.close()
    shifrpict.close()

    print("recording photoka which located in your work in folder STEGAN ")

def deshifr():
    byye_s = int(input("choose how many byte in code in pixel: 1/2/4/8/ "))
    for_read = int(input("how many symbole chetivaet?"))

    pict_len = os.stat("shifrpict.bmp").st_size


    if for_read > (pic_len * Bytes/8 - 54):
        print("text maybe long for code in the same photoke and the same format")
        return

    text = open("rashifr.tst", "w")
    shifrpict = open("shifrpict.bmp", "rb")

    shifrpict.seek(54)

    test_mask, pict_mask = mask_add(byteswap)

    pict_mask = ~pict_mask

    read = 0

    while read < for_read:
        sys = 0
        
        for bits_read in range(0, 8, BytesIO):
            pict_byte = int.from_bytes(shifrpict.read(1), sys.byteorder) & pict_mask

            sym <<= bytes_s
            sym |= pict_byte

        #prin.... s
        read += 1
        text.write(chr(sym))

    text.close()
    shifrpict.close()
    file = open("rashifr.txt")
    x = file.read()
    print("encrypt text: ", x)

def mask_add(byte_s):
    text_mask = 0b11111111
    pict_mask = 0b11111111

    text_mask >>= (8 - byte_s)
    pict_mask <<= byte_s
    text_mask %= 256
    pict_mask %= 256

    return text_mask, pict_mask


print("place your photoko, in folder STEGAN, in rapochem ctol , and name it 'pic.bmp' ")
a = int(input("choose: 1-coding, 2-decryption, 3-exite "))

if a == 1:
    shifr()
elif a == 2:
    deshifr()
elif a == 3:
    print("OK")
