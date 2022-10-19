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
    sign = '+-'

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

    def clear_hist():
        result_list.clear()
        status_bar.configure(text ='History: ' + '|'.join(result_list))
    def enter_operator(x):
        if entry_box.get() != '0':
            length = len(entry_box.get())
            entry_box.insert(length,btn_operators[x]['text'])

    def fun_clear():
        entry_box.delete(0,'end')

    def about():
        messagebox.showinfo('About', "Calculator by Piskunov Pante\n@All right's reserved by creator!")


    def func_delete():
        length = len(entry_box.get())
        entry_box.delete(length - 1,'end')
        if length == 1:
            entry_box.insert(0,'0')

    result_list = []

    def equal_plus():
        content = entry_box.get()
        a = content.split()
        content = content.replace(' ', '')
        exp = content
        result = 0
        if '+' in exp:
            left,right = exp.split('+')
            a = float(left)
            b = float(right)
            c = a+b
            c = str(c)
            if c[0] == '-':
                sign = -1
                c = c[1:]
            else:
                sign = 1
            result = 0
            chars = str(float(c)).split('.')
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
            result_list.append(c)
        status_bar.configure(text ='History: ' + '|'.join(result_list))

    def equal_minus():
        content = entry_box.get()
        a = content.split()
        content = content.replace(' ', '')
        exp = content
        result = 0
        if '-' in exp:
            left,right = exp.split('-')
            a = float(left)
            b = float(right)
            c = a+b
            c = str(c)
            if c[0] == '-':
                sign = -1
                c = c[1:]
            else:
                sign = 1
            result = 0
            chars = str(float(c)).split('.')
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
            result_list.append(c)
        status_bar.configure(text ='History: ' + '|'.join(result_list))
            

            
    #if '9' in content or '8' in content or '7' in content:
    #pass
    #else:
    #result = eval(content)
    #entry_box.delete(0,'end')
    #entry_box.insert(0,str(result))
    #result_list.append(content)

    def exit_():
        if(messagebox.askquestion('Exit','Are you Sure!')) == 'yes':
            window.destroy()
    #########Menu#######
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label='7th Base Plus', command=equal_plus)
    filemenu.add_command(label='7th Base Minus', command=equal_minus)
    filemenu.add_command(label='Clear', command=fun_clear)
    menubar.add_cascade(label='Option', menu=filemenu)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=exit_)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label='About...',command = about)
    menubar.add_cascade(label='Licence', menu=helpmenu)
    ########Entry box######
    entry_box = ttk.Entry(font = 'verdana 12 bold',width = 25,justify = RIGHT)
    entry_box.place(x = 20, y = 10,width=350, height = 36)


    btn_numbers = []
    for i in range(10):
        btn_numbers.append(ttk.Button(text = str(i),command = lambda x = i: get_text(x)))

    btn_operators = []
    for i in range(2):
        btn_operators.append(ttk.Button(command = lambda x = i: enter_operator(x)))
    btn_operators[0]['text'] = '+'
    btn_operators[1]['text'] = '-'

    btn_text = 1
    for i in range(3):
        for j in range(3):
            btn_numbers[btn_text].place(x = 20 + j *90,y = 70+i*50)
            btn_text += 1

    for i in range(2):
        btn_operators[i].place(x = 290,y = 70 + i * 50)

    #######Buttons######
    bt_zero = ttk.Button(text = '0',command = lambda x = 0:get_text(x))
    btn_clear = ttk.Button(text = 'C',command = fun_clear)
    btn_clear.place(x = 25,y = 260)
    bt_zero.place(x = 25, y =70 + 3 * 50,width=230)
    btn_dot = ttk.Button(text = '.',command = lambda x ='.': get_text(x))
    btn_dot.place(x = 110,y = 260)
    btn_equal = ttk.Button(text = '7th Base Plus',command = equal_plus)
    btn_equal.place(x = 200,y = 260)
    btn_del = ttk.Button(text = 'del', command = func_delete)
    btn_del.place(x = 290,y = 260)
    btn_7th_minus = ttk.Button(text = '7th Base Minus', command = equal_minus)
    btn_7th_minus.place(x = 285,y = 70 + i * 150,width=90, height = 30)
    btn_clear_history = ttk.Button(text = 'clear hist', command = clear_hist)
    btn_clear_history.place(x = 290,y = 70 + i * 100)
    status_bar = ttk.Label(window, text = 'History: ',relief = SUNKEN)
    status_bar.pack(side = BOTTOM, fill = X)

    window.config(menu=menubar)
    window.mainloop()
main()
