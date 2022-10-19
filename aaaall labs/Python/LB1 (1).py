from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def align(a,b):   #to make a and b equal in length and to align the '.'
    p_ind1 = a.find('.')
    p_ind2 = b.find('.')
    len1 = len(a)-1 - p_ind1
    len2 = len(b)-1 - p_ind2
    
    if p_ind1 == -1 and p_ind2 > -1:
        a = a + '.' + '0' * len2
    if p_ind2 == -1 and p_ind1 > -1:
        b = b + '.' + '0' * len1
    if p_ind1 > -1 and p_ind2 > -1:
        a = a + '0' * (len2-len1)
        b = b + '0' * (len1-len2)

    prefx = abs(len(a) - len (b))
    if len(a)>len(b):
        b = '0'*prefx + b
    else:
        a =  '0'*prefx + a
    return a,b  # aligned a and b and

def Subtract(a,b):  # gives a-b
    a,b = align(a,b)

    neg = 0
    if float(a) < float(b):
        neg = 1
        a,b = b,a
    
    point_ind = a.find('.')    # index of '.' in the number
    a = a.replace('.','')
    b = b.replace('.','')
    # len_a = len(a)
    a = list(a)
    b = list(b)
    res = ''
    for i in reversed(range(len(a))):
        d1 = a[i]
        d2 = b[i]
        if d1 >= d2:
            res = str(int(d1) - int(d2)) + res    
        else:
            j = i-1
            while a[j] == 0:
                j -= 1
            a[j] = str(int(a[j]) - 1)
            j += 1
            while j < i:
                a[j] = '6'
                j+=1

            res = str(7 + int(d1) - int(d2)) + res
    res = res[:]
    if point_ind > -1:
        res = res[:point_ind] + '.' + res[point_ind:]
    if neg == 1:
        res = '-' + res
    
    return res


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
    '''
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
    '''
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
        if '9' in content or '8' in content or '7' in content:
            pass
        else:
            exp = content
            if '+' in exp:
                left,right = exp.split('+')
                a = str(float(left)).split('.')
                b = str(float(right)).split('.')
                a1 = [*map(int,str(a[0]))]
                b1 = [*map(int,str(b[0]))]
                a1 = a1[::-1]
                b1 = b1[::-1]
                size = max(len(a1), len(b1))
                a1 += [0] * (size - len(a1))
                b1 += [0] * (size - len(b1))
                overflow = 0
                result = []
                for obj in zip(a1, b1):
                    value = obj[0] + obj[1] + overflow
                    overflow = value // 7 #delim na 7
                    result.append(value % 7) #zacuvuvame ostatok
                if overflow == 1:
                    result.append(1)
                result = result[::-1]
                left1 = [*map(int,str(a[1]))]
                left2 = [*map(int,str(b[1]))]
                size = max(len(left1), len(left2))
                left1 += [0] * (size - len(left1))
                left2 += [0] * (size - len(left2))
                left1 = left1[::-1]
                left2 = left2[::-1]
                overflow2 = 0
                result2 = []
                for obj in zip(left1, left2):
                    value2 = obj[0] + obj[1] + overflow2
                    overflow2 = value2 // 7 #delim na 7
                    s = value2%7
                    result2.append(s) #zacuvuvame ostatok
                if overflow2 == 1:
                    result2.append(1)
                result2 = result2[::-1]
                if result2[0] == 1:
                    result2 = list(result2)
                    del result2[0]
                    result2.insert(0,'.')
                    strings = [str(i) for i in result]
                    a_string = ''. join(strings)
                    an_integer = int(a_string)
                    an_integer = an_integer+1
                    an_integer = list(str(an_integer))
                    an_integer.extend(result2)
                elif result2[0] == 0:
                    result2 = list(result2)
                    result2.insert(0,'.')
        
                    strings = [str(i) for i in result]
                    a_string = ''. join(strings)
                    an_integer = int(a_string)
                    an_integer = an_integer
                    an_integer = list(str(an_integer))
                    an_integer.extend(result2)
                else:
                    result2 = list(result2)
                    result2.insert(0,'.')
                    strings = [str(i) for i in result]
                    a_string = ''. join(strings)
                    an_integer = int(a_string)
                    an_integer = an_integer
                    an_integer = list(str(an_integer))
                    an_integer.extend(result2)
                    an_integer = an_integer
                
                entry_box.delete(0,'end')
                entry_box.insert(0,an_integer)
                result_list.append(content)
            status_bar.configure(text ='History: ' + '|'.join(result_list))
    
    def equal_minus():
        content = entry_box.get()
        a = content.split()
        content = content.replace(' ', '')
        if '9' in content or '8' in content or '7' in content:
            pass
        else:
            exp = content
            if '-' in exp:
                left,right = exp.split('-')
                # a = str(float(left)).split('.')
                # b = str(float(right)).split('.')
                # a1 = [*map(int,str(a[0]))]
                # b1 = [*map(int,str(b[0]))]
                # a1 = a1[::-1]
                # b1 = b1[::-1]
                # size = max(len(a1), len(b1))
                # a1 += [0] * (size - len(a1))
                # b1 += [0] * (size - len(b1))
                # print(a1)
                # print(b1)
                # overflow = 0
                # result = []
                # for obj in zip(a1, b1):
                #     value = obj[1] - obj[0] - overflow
                #     overflow = value // 7 #delim na 7
                #     result.append(value % 7) #zacuvuvame ostatok
                # if overflow == 1:
                #     result.append(1)
                # result = result[::-1]
                # left1 = [*map(int,str(a[1]))]
                # left2 = [*map(int,str(b[1]))]
                # size = max(len(left1), len(left2))
                # left1 += [0] * (size - len(left1))
                # left2 += [0] * (size - len(left2))
                # left1 = left1[::-1]
                # left2 = left2[::-1]
                # overflow2 = 0
                # result2 = []
                # for obj in zip(left1, left2):
                #     value2 = obj[0] - obj[1] - overflow2
                #     overflow2 = value2 // 7 #delim na 7
                #     s = value2%7
                #     result2.append(s) #zacuvuvame ostatok
                # if overflow2 == 1:
                #     result2.append(1)
                # result2 = result2[::-1]
                # if result2[0] == 1:
                #     result2 = list(result2)
                #     del result2[0]
                #     result2.insert(0,'.')
                #     strings = [str(i) for i in result]
                #     a_string = ''. join(strings)
                #     an_integer = int(a_string)
                #     an_integer = an_integer+1
                #     an_integer = list(str(an_integer))
                #     an_integer.extend(result2)
                # elif result2[0] == 0:
                #     result2 = list(result2)
                #     result2.insert(0,'.')
        
                #     strings = [str(i) for i in result]
                #     a_string = ''. join(strings)
                #     an_integer = int(a_string)
                #     an_integer = an_integer
                #     an_integer = list(str(an_integer))
                #     an_integer.extend(result2)
                # else:
                #     result2 = list(result2)
                #     result2.insert(0,'.')
                #     strings = [str(i) for i in result]
                #     a_string = ''. join(strings)
                #     an_integer = int(a_string)
                #     an_integer = an_integer
                #     an_integer = list(str(an_integer))
                #     an_integer.extend(result2)
                #     an_integer = an_integer
                
                res = Subtract(left,right)
                entry_box.delete(0,'end')
                entry_box.insert(0,res)

                result_list.append(content)
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
    filemenu.add_command(label='Del', command=func_delete)
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
