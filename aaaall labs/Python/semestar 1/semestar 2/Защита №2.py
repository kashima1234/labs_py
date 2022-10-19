from tkinter import *

def bubble_sort(arr):
    a = list(int(num) for num in arr.get().strip().split())
    print(a)
    A = [4,9,3,7,1]
    B = {A[i]:i for i in range(len(A))}
    n = len(a)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if B[a[j]] > B[a[j+1]] :
                a[j], a[j+1] = a[j+1], a[j]   
    return a


def result():
    res_box.delete(0, 'end')
    res_box.insert(END, bubble_sort(entry_box))
    
window = Tk()
window.geometry('500x500')

Label(window, text = '4, 9, 3, 7, 1').grid(row = 0,padx = 40)
entry_box = Entry(window)
entry_box.grid(row = 1, ipadx = 60)
res_box = Entry(window)
res_box.grid(row = 2, pady = 20, ipadx = 60)
sort = Button(window, text = 'Sort',command = result)
sort.grid(row = 2, column = 3, padx = 40)


window.mainloop()
