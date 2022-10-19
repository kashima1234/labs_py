import tkinter as tk
window = tk.Tk()
window.resizable(0,0)
window.geometry('600x300')
window.title('Калькулятор')

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)
    
def btn_clear():    #btn_clear function clears the
#input field and previous calculations using the ’Clear’ button
    global expression
    expression = ''
    input_text.set('')
    
def get_text(x):
    if input_field.get() == '0':
        input_field.delete(0,'end')
        input_field.insert(0,str(x))
    else:
        length = len(input_field.get())
        input_field.insert(length,str(x))
    
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
def btn_equal():
    result = 0
    content = input_field.get()
    result = eval(content)
    input_field.delete(0,"end")
    input_field.insert(0,str(result))
    input_text.append(content)
    
def enter_operator(x):
    if input_field.get() != '0':
        length = len(input_field.get())
        input_field.insert(length,btn_operators[x]["text"])
def fun_clear():
    input_field.delete(0,"end")
btn_numbers = []
for i in range(10):
    btn_numbers.append(tk.Button(text = str(i),command = lambda x = i: get_text(x)))
btn_operators = []
for i in range(4):
    btn_operators.append(tk.Button(command = lambda x = i: enter_operator(x)))
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
'''    
def btn_equal(item):    #btn_equal function calculates the expression entered in the input field
    #try:
    global expression
    global result
    result = float(eval(expression))
    input_text.set(result)
    expression = ''
    #except:
     #   input_text.set('ERROR')
      #  expression = ''
'''
def del_number():
    length = len(input_field.get())
    input_field.delete(length - 1,'end')
    if length == 1:
        input_field.insert(0,"0")
        


def Bin_number():
    try:
        global expression
        global result
        whole,res = str(result).split('.')
        whole = int(whole)
        res = int(res)
        whole_list = []
        dec_list = []
        places = 4
        counter = 1
        while whole / 7 >= 1:
            remainder = int(whole % 7)
            whole_list.append(remainder)
            whole /= 7
        decproduct = res      
        while (counter <= places):
            decproduct = decproduct * (10**-(len(str(decproduct))))
            decproduct *= 7
            decwhole, decdec = str(decproduct).split('.')
            decwhole = int(decwhole)
            decdec = int(decdec)
            dec_list.append(decwhole)
            decproduct = decdec
            counter += 1
        if(len(whole_list) > 1):
            whole_list.reverse()
        dec_list.insert(0, '.')
        whole_list.extend(dec_list)
        whole_list.insert(0, 1)
        input_text.set(whole_list)
    except:
        whole,res = expression.split('.')
        whole = int(whole)
        res = int(res)
        whole_list = []
        dec_list = []
        places = 4
        counter = 1
        while whole / 7 >= 1:
            remainder = int(whole % 7)
            whole_list.append(remainder)
            whole /= 7
        decproduct = res      
        while (counter <= places):
            decproduct = decproduct * (10**-(len(str(decproduct))))
            decproduct *= 7
            decwhole, decdec = str(decproduct).split('.')
            decwhole = int(decwhole)
            decdec = int(decdec)
            dec_list.append(decwhole)
            decproduct = decdec
            counter += 1
        if(len(whole_list) > 1):
            whole_list.reverse()
        dec_list.insert(0, '.')
        whole_list.extend(dec_list)
        whole_list.insert(0, 1)
        input_text.set(whole_list)
input_text = []        
bin_number = Bin_number    
expression = ''
input_frame = tk.Frame(window,width = 312,height=50,bd=0)
input_frame.pack()
input_field = tk.Entry(input_frame,width=50,bd = 0)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)
btns_frame = tk.Frame(window, width = 312, height = 272.5)
btns_frame.pack()

#clear = tk.Button(btns_frame, text = "Clear",bg = "white",width = 10, height = 3, bd = 0,command = fun_clear).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
#Exit = tk.Button(btns_frame, text = 'Exit',bg = 'white', width = 10, height = 3, bd = 0, command = exit).grid(row = 0, column = 1, columnspan = 3, padx = 1, pady = 1)
#divide = tk.Button(btns_frame, text = "/",bg = "white",width = 10, height = 3, bd = 0,command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
#seven = tk.Button(btns_frame, text = "7",bg = "white",width = 10, height = 3, bd = 0,command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
#eight = tk.Button(btns_frame, text = "8",bg = "white",width = 10, height = 3, bd = 0,command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
#nine = tk.Button(btns_frame, text = "9",bg = "white",width = 10, height = 3, bd = 0,command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
#multiply = tk.Button(btns_frame, text = "*",bg = "white",width = 10, height = 3, bd = 0,command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
#four = tk.Button(btns_frame, text = "4",bg = "white",width = 10, height = 3, bd = 0,command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
#five = tk.Button(btns_frame, text = "5",bg = "white",width = 10, height = 3, bd = 0,command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
#six = tk.Button(btns_frame, text = "6",bg = "white",width = 10, height = 3, bd = 0,command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
#minus = tk.Button(btns_frame, text = "-",bg = "white",width = 10, height = 3, bd = 0,command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
#one = tk.Button(btns_frame, text = "1",bg = "white",width = 10, height = 3, bd = 0,command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
#two = tk.Button(btns_frame, text = "2",bg = "white",width = 10, height = 3, bd = 0,command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
#three = tk.Button(btns_frame, text = "3",bg = "white",width = 10, height = 3, bd = 0,command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
#plus = tk.Button(btns_frame, text = "+",bg = "white",width = 10, height = 3, bd = 0,command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
zero = tk.Button(btns_frame, text = "0",bg = "white",width = 10, height = 3, bd = 0,command = lambda x = 0:get_text(x)).grid(row = 4, column = 0,padx = 1, pady = 1)
point = tk.Button(btns_frame, text = ".",bg = "white",width = 10, height = 3, bd = 0,command = lambda x =".": get_text(x)).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = tk.Button(btns_frame, text = "=",bg = "white",width = 10, height = 3, bd = 0,command = btn_equal).grid(row = 4, column = 3, padx = 1, pady = 1)
Bin = tk.Button(btns_frame, text = '7-й',bg = "white",width = 10, height = 3, bd = 0,command = lambda: bin_number()).grid(row = 0, column = 0,padx = 1, pady = 1)
C = tk.Button(btns_frame, text = 'C',bg = "white",width = 10, height = 3, bd = 0,command = lambda: Bin_number()).grid(row = 4, column = 1,padx = 1, pady = 1)



