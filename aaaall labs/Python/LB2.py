import random
import timeit
from tkinter import *

class First: 
      
    def __init__(self,root): 
          
        # code for creating table 
        for i in range(1): 
            for j in range(4): 
                  
                self = Entry(root, width=40) 
                self.grid(row=i, column=j) 
                self.insert(END, lst[i][j])
class Second:
    def __init__(self2,root):
        for i in range(1): 
            for j in range(4): 
                
                self2 = Entry(root, width=20,) 
                self2.grid(row=i, column=j,pady = 30,rowspan = 100,ipadx = 60, padx = 10, ipady = 1) 
                self2.insert(END, lst2[i][j])

class Third:
    def __init__(self3,root):
        for i in range(1): 
            for j in range(4): 
                
                self3 = Entry(root, width=20,) 
                self3.grid(row=i, column=j,pady = 60,rowspan = 200,ipadx = 60, padx = 10, ipady = 1) 
                self3.insert(END, lst3[i][j])

class Time:
    def __init__(self3,root):
        for i in range(1): 
            for j in range(4): 
                
                self3 = Entry(root, width=20,) 
                self3.grid(row=i, column=j,pady = 90,rowspan = 300,ipadx = 60, padx = 10, ipady = 1) 
                self3.insert(END, time[i][j]) 

def insertion_sort(array_to_sort):
    a = array_to_sort.copy()
    for i in range(len(a)):
        j = i - 1 
        key = a[i]
        while a[j] > key and j >= 0:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def reversed_array(array):
    a = array.copy()
    for i in range(len(a)):
        j = i - 1 
        key = a[i]
        while a[j] < key and j >= 0:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


  
n = 10
first_random_arr = random.sample(range(0, 100), 10)
second_random_arr = random.sample(range(0, 100), 10)
third_random_arr = random.sample(range(0, 100), 10)


first_time = timeit.timeit(lambda: insertion_sort(first_random_arr),number = n)
second_time = timeit.timeit(lambda: insertion_sort(second_random_arr),number = n)
third_time = timeit.timeit(lambda: insertion_sort(third_random_arr),number = n)

lst = [['List',first_random_arr,second_random_arr,third_random_arr]]
lst2 = [['Sorted list',insertion_sort(first_random_arr),insertion_sort(second_random_arr),insertion_sort(third_random_arr)]]
lst3 = [['Reversed array',reversed_array(insertion_sort(first_random_arr)),reversed_array(insertion_sort(second_random_arr)),reversed_array(insertion_sort(third_random_arr))]]
time = [['Time',first_time,second_time,third_time]]
    
 
root = Tk() 
t = First(root)
t2 = Second(root)
t3 = Third(root)
time = Time(root)
root.mainloop() 
