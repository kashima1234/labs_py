from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def main():
    window = Tk()
    window.geometry('390x375')
    window.title('Calculator')
    def get_text(x):
        if entry_box.get() == '0':
            entry_box.delete(0,'end')
            entry_box.insert(0,str(x))
        else:
            length = len(entry_box.get())
            entry_box.insert(length,str(x))
    
    numbers = '0123456789'
    sign = '+-*/'

    def isit_num(num):
        dot = 0
        for i in range(len(num)):
            digit = num[i]
            if digit not in numbers:
                if digit in sign and i == 0:
                    continue
                elif digit == '.' and dot == 0:
                    dot = 1
                else:
                    return False
            else:
                continue
        return True

    def fun_clear():
        entry_box.delete(0,'end')
    def Exit():
        window.destroy()
        
    def func_delete():
        length = len(entry_box.get())
        entry_box.delete(length - 1,'end')
        if length == 1:
            entry_box.insert(0,'0')
    
    def other_system():
        A = entry_box.get()
        if not isit_num(A):
            messagebox.showerror('Error')
            entry_box.delete(0, END)
        else:
            if A[0] == '-':
                sign = -1
                A = A[1:]
            else:
                sign = 1
            result = 0
            chars = str(float(A)).split('.')
            m = int(chars[0])
            result = ''
            while m >= 1:
                result += str(m % 7)
                m = m // 7
            result += str(m)
            result = result[::-1]
            #reverse
            drob = ''
            n = float('0.' + chars[1])
            count = 0
            while count < 15:
                count += 1
                n *= 7
                drob += str(int(n // 1))
                n = n % 1
                if n == 0.0:
                    break
            final = float(result + '.' + drob) * sign
            entry_box.delete(0,'end')
            entry_box.insert(0,final)
            result_list.append(A)


    result = 0
    def equal():
        try:
            content = entry_box.get()
            result = eval(content)
            entry_box.delete(0,'end')
            entry_box.insert(0,str(result))
            result_list.extend(content)
        except:
            result_list.append('Error')

    result_list = []

    entry_box = ttk.Entry(font = 'verdana 12 bold',width = 25,justify = RIGHT)

    entry_box.place(x = 20, y = 10,width=350, height = 36)



    btn_numbers = []
    for i in range(10):
        btn_numbers.append(ttk.Button(text = str(i),command = lambda x = i: get_text(x)))

    def enter_operator(x):
        if entry_box.get() != '0':
            length = len(entry_box.get())
            entry_box.insert(length,btn_operators[x]['text'])
    btn_operators = []
    for i in range(4):
        btn_operators.append(ttk.Button(command = lambda x = i: enter_operator(x)))
    btn_operators[0]['text'] = '+'
    btn_operators[1]['text'] = '-'
    btn_operators[2]['text'] = '*'
    btn_operators[3]['text'] = '/'

    btn_text = 1
    for i in range(3):
        for j in range(3):
            btn_numbers[btn_text].place(x = 25 + j *90,y = 70+i*50)
            btn_text += 1

    for i in range(4):
        btn_operators[i].place(x = 290,y = 70 + i * 50)

    btn_other_system = ttk.Button(text = '7-й', command = other_system)
    btn_other_system.place(x = 113, y =70 + 3 * 50, width = 75)
    btn_exit = ttk.Button(text = 'Exit', command = Exit)
    btn_exit.place(x= 200,y =70 + 3 * 50,width = 75)
    bt_zero = ttk.Button(text = '0',command = lambda x = 0:get_text(x))
    btn_clear = ttk.Button(text = 'C',command = fun_clear)
    btn_clear.place(x = 25,y = 260)
    bt_zero.place(x = 25, y =70 + 3 * 50,width=75)
    btn_dot = ttk.Button(text = '.',command = lambda x =".": get_text(x))
    btn_dot.place(x = 110,y = 260)
    btn_equal = ttk.Button(text = '=',command = equal)
    btn_equal.place(x = 200,y = 260)
    btn_del = ttk.Button(text = 'del', command = func_delete)
    btn_del.place(x = 290,y = 260)
    
    window.mainloop()
main()







































#Label widgets don’t have .get() like Entry and Text widgets do. However, you can retrieve the text from the label by accessing the text attribute with a dictionary-style subscript notatio
