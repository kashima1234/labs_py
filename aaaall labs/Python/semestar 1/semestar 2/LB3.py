from tkinter import*
from tkinter import ttk
import matplotlib.pyplot as plt
from numpy import*
from tkinter import messagebox
from math import sin,cos

def f(x):
    return sin(x)

def f1(x):
    return cos(x)

def f2(x):
    return -sin(x)

def root_search(a,b,eps,n):
    if f(a) == 0:
        return a,1,0
    if f(b) == 0:
        return b,1,0
    
    # 1-я итерация
    x1 = a
    if f(b)*f2(b) > 0: #для выбора начальной точки проверяем
        x1 = b
    i = 1
    
    while (i <= n):
        x = x1 - (f(x1) / f1(x1)) #считаем первое приближение
        if abs(x - x1) < eps:  #считаем с точностью
            if a <= x <= b:
                return x, i, 0
            return '-', i, 2
        
        x1 = x
        i += 1     #итерации
        
    return '-', i, 1
    

def finding(a,b,h,eps, n):    
    roots = []  # список корней
    res = []    # список интервалов
    kol = 0     # количество итераций
    aa = a      # начало отрезка
    bb = a      # конец отрезка

    #нахождение интервалов
    while bb < b:
        bb += h
        if bb > b:
            bb = b
        if f(aa)*f(bb)<=0:
            kol += 1
            res.append([aa,bb])
        aa += h

    #нахождение корней
    i = 0
    while len(res) > i:
        #список с информацией о корне
        rootX = root_search(res[i][0],res[i][1],eps,n)
        if (len(roots) == 0 or rootX[0] == '-' or
            roots[-1][0] == '-' or abs(rootX[0] - roots[-1][0]) > 1e-9):
            roots.append(rootX)
        else:
            res.pop(i)
            i -= 1
        i += 1
    return roots, res

#Graph function
def graph(start,end,step):
    x = [i for i in arange(start,end +step,step)]
    n  = len(x)
    y = []
    for i in x:
        y.append(float(f(i)))
    ymin = min(y)
    ymax = max(y)
    ymini,ymaxi = y.index(ymin),y.index(ymax)
    #plt.title("Function Graph\nMax point is:{:.4f}\nMin point is:{:.4f}".format(ymax,ymin))
    plt.xlabel("X points")
    plt.ylabel("Y points")
    plt.plot(x,y,label = "x*x-2")
    plt.scatter(x[ymini],ymin, color = "red",label = "minimum")
    plt.scatter(x[ymaxi],ymax, color = "blue",label ="maximum")
    plt.legend()
    plt.grid()
    plt.show()

#Table
def root_menu(start, end, step, eps, max_iteration):
    a = start
    b = end
    h = step
    eps = eps
    n = max_iteration

    roots, res = finding(a, b, h, eps, n)
    root = Tk()
    root.title("Root table")
    root.geometry("755x325+300+300")
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
    print()
    if len(roots) == 0 and len(res) == 0:
        messagebox.showerror(title = "Error", message="root not finded!")
        root.destroy()
    else:
        #print(len(roots))
        for i in range(len(roots) - 1, -1, -1):
            a1 = res[i][0]
            b1 = res[i][1]
            
            if roots[i][0] != '-':
                treeview.insert("", 0, text=i + 1, values=("({:7.3f};{:7.3f})".format(a1, b1), "{:9.4}".format(roots[i][0]), "{:10.3e}".format(f(roots[i][0])),"{:8d}".format(roots[i][1]), roots[i][2]))
            else:
                treeview.insert("", 0, text=i + 1, values=("({:7.3f};{:7.3f})".format(a1, b1), "".format(9 * "-"), "{}".format(10 * "-","{:8d}".format(roots[i][1]), roots[i][2])))

            # treeview.insert("", 0, text = i + 1, values=("({:7.3} ;{:7.3})".format(a1, b1), "{:9.4f}".format(roots[i][0]),"{:10.3e}".format(f(roots[i][0])),"{:8d}".format(roots[i][1]), roots[i][2]))
    lbl = ttk.Label(root, text="0 - нет ошибок", font="Times 12").place(x = 270, y = 240)
    lbl2 = ttk.Label(root, text="1 - большое количество итераций", font="Times 12").place(x = 270, y = 270)
    lbl3 = ttk.Label(root, text="2 - метод расходится", font="Times 12").place(x = 270, y = 300)
    root.mainloop()

def main_window():
    root = Tk()
    root.title("Third lab")
    root.geometry("400x380")
    #solve root


    def callback():
        try:
            start = float(var1.get())
            end = float(var2.get())
            step = float(var3.get())
            eps = float(var4.get())
            max_iteration = float(var5.get())
            root_menu(start,end,step,eps,max_iteration)
        except:
            pass



    #graph call
    def callback1():
        start = float(var1.get())
        end = float(var2.get())
        step = float(var3.get())
        graph(start, end, step)


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
