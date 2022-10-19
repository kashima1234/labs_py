from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def main():
    root = Tk()
    root.geometry("390x375")
    style = ttk.Style(root)
    style.configure('Die.TButton', background="blue")
    style.configure('TButton', background="yellow")
    style.configure('e.TButton', background="orange")
    root.resizable(FALSE,FALSE)
    root.title("Calculator 3rd base")
    def get_text(x):
        if entry_box.get() == 'O':
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
        status_bar.configure(text ="History: " + "|".join(result_list))
    def enter_operator(x):
        if entry_box.get() != 'O':
            length = len(entry_box.get())
            entry_box.insert(length,btn_operators[x]["text"])

    def fun_clear():
        entry_box.delete(0,"end")

    def about():
        messagebox.showinfo("About", "3rd Base Calculator by Ahmad Khalid Karimzai\n@All right's reserved by creator!")

    def help():
        messagebox.showinfo("Help", "1. To do mathematical operation just type and do it.\n2.for change from base 10 to base 3 click to change the number.\
            \n3.To change from 10 base to 3 just add the number and click The button or use the menu option for doing operation.\n@All right's reserved!")


    def func_delete():
        length = len(entry_box.get())
        entry_box.delete(length - 1,'end')
        if length == 1:
            entry_box.insert(0,"O")

    result_list = []
    def decimal_third():
        A = entry_box.get()
        if not isit_num(A):
            messagebox.showerror("Error", "Entered symbol's not number.")
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
            while m >= 2:
                result += str(m % 2)
                m = m // 2
            result += str(m)
            result = result[::-1]
            drob = ''
            n = float('0.' + chars[1])
            count = 0
            while count < 15:
                count += 1
                n *= 2
                drob += str(int(n // 1))
                n = n % 1
                if n == 0.0:
                    break
            final = float(result + '.' + drob) * sign
            entry_box.delete(0,"end")
            entry_box.insert(0,final)
            result_list.append(A)

        status_bar.configure(text ="History: " + "|".join(result_list))


    def third_decimal():
        A = entry_box.get()
        if not isit_num(A):
            messagebox.showerror("Error", "Entered symbol's Not Number's.")
            entry_box.delete(0, END)
        elif ('3' in A) or ('4' in A) or ('5' in A) or ('6' in A) or ('7' in A) or ('8' in A) or ('9' in A):
            messagebox.showerror("Error", "in Ternary only 0, 1, 2")
            entry_box.delete(0, END)
        else:
            if A[0] == '-':
                sign = -1
                A = A[1:]
            else:
                sign = 1
            result = 0
            chars = str(float(A)).split('.')
            chars[0], chars[1] = list(map(int, chars[0])), list(map(int, chars[1]))
            m = -1
            for i in range(len(chars[0])-1, -1, -1):
                m += 1
                result += chars[0][i]*(3**m)
            m = 0
            for i in range(len(chars[1])):
                m -= 1
                result += chars[1][i]*(3**m)
                
            result *= sign
            entry_box.delete(0, END)
            entry_box.insert(END, result)
            result_list.append(A)

        status_bar.configure(text ="History: " + "|".join(result_list))

    result = 0
    def equal():
        content = entry_box.get()
        result = eval(content)
        entry_box.delete(0,"end")
        entry_box.insert(0,str(result))
        result_list.append(content)

        status_bar.configure(text ="History: " + "|".join(result_list))

    def exit_():
        if(messagebox.askquestion("Exit","Are you Sure!")) == "yes":
            root.destroy()
    ##################################000000000000000000#####################################
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Third Base", command=decimal_third)
    filemenu.add_command(label="Decimal", command=third_decimal)
    filemenu.add_command(label="Clear", command=fun_clear)
    menubar.add_cascade(label="Option", menu=filemenu)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exit_)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help",command = help)
    helpmenu.add_command(label="About...",command = about)
    menubar.add_cascade(label="Licence", menu=helpmenu)
    ######################################Entry box#############
    entry_box = ttk.Entry(font = "verdana 12 bold",width = 25,justify = RIGHT)
    #entry_box.insert(0,"O")
    entry_box.place(x = 20, y = 10,width=350, height = 36)
    #3333333333333333333333333333333333333333333333333333333333333
    s = ttk.Style()
    #s.configure("TButton", background="blue")

    btn_numbers = []
    for i in range(10):
        btn_numbers.append(ttk.Button(text = str(i),command = lambda x = i: get_text(x),style='Die.TButton'))

    btn_operators = []
    #s.configure('TButton', font=('Arial 12'))
    for i in range(4):
        btn_operators.append(ttk.Button(command = lambda x = i: enter_operator(x),style='TButton'))
    btn_operators[0]["text"] = "+"
    btn_operators[1]["text"] = "-"
    btn_operators[2]["text"] = "*"
    btn_operators[3]["text"] = "/"

    btn_text = 1
    for i in range(3):
        for j in range(3):
            btn_numbers[btn_text].place(x = 25 + j *90,y = 70+i*50)
            btn_text += 1

    for i in range(4):
        btn_operators[i].place(x = 290,y = 70 + i * 50)


    #00000000000000000000000000000000000000000000000
    bt_zero = ttk.Button(text = "0",command = lambda x = 0:get_text(x),style='Die.TButton')
    btn_clear = ttk.Button(text = "C",command = fun_clear)
    btn_clear.place(x = 25,y = 260)
    bt_zero.place(x = 25, y =70 + 3 * 50,width=230)
    btn_dot = ttk.Button(text = ".",command = lambda x =".": get_text(x))
    btn_dot.place(x = 110,y = 260)
    btn_equal = ttk.Button(text = "=",command = equal)
    btn_equal.place(x = 200,y = 260)
    btn_del = ttk.Button(text = "del", command = func_delete)
    btn_del.place(x = 290,y = 260)
    btn_third = ttk.Button(text = "Third  Base", command = decimal_third,style='e.TButton')
    btn_third.place(x = 23,y = 300,width=130, height = 50)
    btn_clear_history = ttk.Button(text = "clear hist", command = clear_hist,style='e.TButton')
    btn_clear_history.place(x = 160,y = 300)
    btn_decimal = ttk.Button(text = "Decimal", command = third_decimal,style='e.TButton')
    btn_decimal.place(x = 240,y = 300,width=130, height = 50)
    status_bar = ttk.Label(root, text = "History: ",relief = SUNKEN)
    status_bar.pack(side = BOTTOM, fill = X)

    root.config(menu=menubar)
    root.mainloop()
main()
