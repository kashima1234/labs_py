from tkinter import*
from tkinter import ttk
import matplotlib.pyplot as plt
from numpy import*
from tkinter import messagebox
from math import sin, ceil, cos
import pylab

class root_spec:
    def __init__(self, root_no, interval, value, number_of_iter, error_code):
        self.root_no = root_no
        self.interval = interval
        self.value = value
        self.fun_value = f(self.value)
        self.number_of_iter = number_of_iter
        self.error_code = error_code
#function
def f(x):
    return sin(x)

def f1(x):
    return cos(x)

def combined_method(a, b, step, epsilon, max_iterations, flag = False):
    border_a = a
    border_b = b
    list_x_approximate = []
    res = []
    total_interval = border_b - border_a 
    temp_a = border_a
    count_roots = 0

    for i in range(ceil(total_interval / step)):
        temp_b =  temp_a + step 
        count_iterations = 1
        try_search = 1
        code_error = "0"


        if (f(temp_b) * f(temp_a)) < 0:  
            count_roots += 1 

            while try_search < 3:

                if try_search == 1:
                    left_border = temp_a - ((f(temp_a) * \
                                             (temp_b - temp_a)) / (f(temp_b) - f(temp_a)))  
                    right_border = temp_b - (f(temp_b) / f1(temp_b))

                    while abs(right_border - left_border) > epsilon \
                          and count_iterations < max_iterations:
                        left_border = left_border - ((f(left_border) * \
                                                      (right_border - left_border)) / \
                                                     (f(right_border) - f(left_border)))
                        right_border = right_border - (f(right_border) / f1(right_border))
                        count_iterations += 1

                    if temp_a < (right_border + left_border) / 2 < temp_b:
                        break

                else:
                    left_border = temp_a - (f(temp_a) / f1(temp_a))
                    right_border = temp_b + ((f(temp_b) * (temp_b - temp_a)) / (f(temp_b) - f(temp_a)))

                    while abs(right_border - left_border) > epsilon and \
                          count_iterations < max_iterations:
                        right_border = right_border - ((f(right_border) * \
                                                        (right_border - left_border)) \
                                                       / (f(right_border) - f(left_border)))
                        left_border = left_border - (f(left_border) / f1(left_border))
                        count_iterations += 1

                try_search += 1
                
            if not (temp_a < ((right_border + left_border) / 2) < temp_b):  
                code_error = "3"
            else:
                list_x_approximate.append((right_border + left_border) / 2)

            if max_iterations <= count_iterations:
                code_error = "2"

            res.append(root_spec(count_roots, [temp_a, temp_b], (right_border + left_border) / 2, count_iterations, code_error))
        temp_a = temp_b
        
    return res if flag == False else list_x_approximate

#Graph function
def graph(start, end, list_x_approximate):
    dx = 0.001
    fig = pylab.gcf()
    fig.canvas.set_window_title("Fuction graph")
    xlist = arange(start, end, dx)
    ylist = [f(x) for x in xlist]
    x_list_OX = arange(start, end, dx)
    y_list_OX = [0 for x in (x_list_OX)]

    pylab.xlabel("x")
    pylab.ylabel("y")
    pylab.plot(xlist, ylist, label="f(x)")
    pylab.plot(x_list_OX, y_list_OX) 
    
    if len(list_x_approximate):
        for i in range(len(list_x_approximate)):
            y = f(list_x_approximate[i])
            if i == 0:
                pylab.scatter(list_x_approximate[i], y, color="red", \
                              label="Solutions")
            else:
                pylab.scatter(list_x_approximate[i], y, color="red")
    
    pylab.legend()
    pylab.title("f(x)")
    pylab.tick_params(labelsize=14)
    pylab.grid()
    pylab.show()

#Table
def root_menu(start, end, step, eps, max_iteration):
    a = start
    b = end
    h = step
    eps = eps
    n = max_iteration

    res = combined_method(a, b, h, eps, n)
    root = Tk()
    root.title("Root table")
    root.geometry("755x355+300+300")
    root.resizable(False, False)
    treeview = ttk.Treeview(root,columns = ("#0","#1","#2","#3","#4",))
    treeview.heading("#0",text ='Elementary interval' )
    treeview.heading('#1', text ='№ interval')
    treeview.heading('#2', text ='Value of root')
    treeview.heading('#3', text ='function Value')
    treeview.heading('#4', text ='Number of iteration')
    treeview.heading('#5', text ='Error code')
    treeview.column("#0",minwidth=0,width=100, stretch=NO)
    treeview.column("#1",minwidth=0,width=130, stretch=NO)
    treeview.column("#2",minwidth=0,width=140, stretch=NO)
    treeview.column("#3",minwidth=0,width=140, stretch=NO)
    treeview.column("#4",minwidth=0,width=115, stretch=NO)
    treeview.column("#5",minwidth=0,width=120, stretch=NO)
    treeview.pack()
    # print()
    if len(res) == 0:
        messagebox.showerror(title = "Error", message="root not finded!")
        root.destroy()
    else:
        # print(len(roots))
        for i in range(len(res) - 1, -1, -1):
            
            treeview.insert("", 0, text=res[i].root_no, values=("({:7.3f};{:7.3f})".format(res[i].interval[0], res[i].interval[1]), "{:9.4}".format(res[i].value), 
                                                "{:10.3e}".format(f(res[i].fun_value)),"{:8d}".format(res[i].number_of_iter), "{:8}".format(res[i].error_code)))
    lbl = ttk.Label(root, text="0. Метод сошелся", font="Times 12").place(x = 270, y = 240)
    lbl2 = ttk.Label(root, text="1. Превышено максимальное. ", font="Times 12").place(x = 270, y = 270)
    lbl3 = ttk.Label(root, text="2. Метод не сошелся.", font="Times 12").place(x = 270, y = 300)
    lbl3 = ttk.Label(root, text="3. Из-за особенностей графика касательная в одной из точек вышла за интервалы разбиения.", font="Times 12").place(x = 40, y = 330)
    root.mainloop()

def main_window():
    root = Tk()
    root.title("First lab")
    root.geometry("400x380")
    #solve root


    def callback():
        start = float(var1.get())
        end = float(var2.get())
        step = float(var3.get())
        eps = float(var4.get())
        max_iteration = float(var5.get())
        root_menu(start,end,step,eps,max_iteration)



    #graph call
    def callback1():
        start = float(var1.get())
        end = float(var2.get())
        graph(start, end, combined_method(float(var1.get()), float(var2.get()),
                 float(var3.get()), float(var4.get()), float(var5.get()), True))


    #labels
    lbl = ttk.Label(root,text = "Enter start point:",font = "Times 12").grid(row = 0,column = 0,pady = 20)
    lbl2 = ttk.Label(root,text = "Enter last point:",font = "Times 12").grid(row = 1,column = 0,pady = 20)
    lbl3 = ttk.Label(root,text = "Enter step:",font = "Times 12").grid(row = 2,column = 0,pady = 20)
    lbl4 = ttk.Label(root,text = "Enter eps:",font = "Times 12").grid(row = 3,column = 0,pady = 20)
    lbl5 = ttk.Label(root,text = "Maximum iteration:",font = "Times 12").grid(row = 4,column = 0,pady = 20)


    #entry var
    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()
    var5 = StringVar()


    #Entries
    entry1 = ttk.Entry(root,textvariable = var1,width = 30).grid(row = 0,column = 1,pady = 20)
    entry2 = ttk.Entry(root,textvariable = var2,width = 30).grid(row = 1,column = 1,pady = 20)
    entry3 = ttk.Entry(root,textvariable = var3,width = 30).grid(row = 2,column = 1,pady = 20)
    entry4 = ttk.Entry(root,textvariable = var4,width = 30).grid(row = 3,column = 1,pady = 20)
    entry5 = ttk.Entry(root,textvariable = var5,width = 30).grid(row = 4,column = 1,pady = 20)

    #button
    button = ttk.Button(root,text = "Solve",command = callback).grid(row = 5,column = 0,pady = 10)
    button1 = ttk.Button(root,text = "Graph",command = callback1).grid(row = 5,column = 1,pady = 10,sticky = E)

    # root.resizable(False, False)
    root.mainloop()
main_window()
