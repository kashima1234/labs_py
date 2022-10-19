from random import randint, shuffle
import timeit
from tkinter import *

def ent_box(box):
    a = list(int(num) for num in box.get().strip().split())
    for i in range(len(a) - 1):
        idx_min = i
        j = i + 1
        while j < len(a):
            if a[j] < a[idx_min]:
                idx_min = j
            j += 1
        a[i], a[idx_min] = a[idx_min], a[i]
    return a

def reversed_array(array):
    a = array.get().split()
    for i in range (len(a)):
        idx = i
        for j in range(i+1,len(a)):
            if a[j] > a[idx]:
                idx = j
        tmp = a[idx]
        a[idx] = a[i]
        a[i] = tmp
    return a

def random_numbers(num):
    a = num.get()
    result = [i for i in range(int(a))]
    shuffle(result)
    g = ' '.join(str(j) for j in result)
    return g

def zero_ent_box():
    zero_result_entry_box.delete(0, 'end')
    zero_result_entry_box.insert(END, ent_box(zero_entry_box))

def first_ent_box():
    first_result_entry_box.delete(0, 'end')
    first_result_entry_box.insert(END, random_numbers(first_entry_box))
    first_sorted_list.delete(0, 'end')
    first_sorted_list.insert(END, ent_box(first_result_entry_box))
    first_reversed_list.delete(0, 'end')
    first_reversed_list.insert(END, ent_box(first_sorted_list))
    label_time1 = timeit.timeit(lambda: random_numbers(first_entry_box),number = 10)
    first_time1.delete(0, 'end')
    first_time1.insert(END, label_time1)
    label_time2 = timeit.timeit(lambda: ent_box(first_result_entry_box),number = 10)
    first_time2.delete(0, 'end')
    first_time2.insert(END, label_time2)
    label_time3 = timeit.timeit(lambda: reversed_array(first_sorted_list),number = 10)
    first_time3.delete(0, 'end')
    first_time3.insert(END, label_time3)
    

def second_ent_box():
    second_result_entry_box.delete(0, 'end')
    second_result_entry_box.insert(END, random_numbers(second_entry_box))
    second_sorted_list.delete(0, 'end')
    second_sorted_list.insert(END, ent_box(second_result_entry_box))
    second_reversed_list.delete(0, 'end')
    second_reversed_list.insert(END, ent_box(second_sorted_list))
    label_time1 = timeit.timeit(lambda: random_numbers(second_entry_box),number = 100)
    second_time1.delete(0, 'end')
    second_time1.insert(END, label_time1)
    label_time2 = timeit.timeit(lambda: ent_box(second_result_entry_box),number = 100)
    second_time2.delete(0, 'end')
    second_time2.insert(END, label_time2)
    label_time3 = timeit.timeit(lambda: reversed_array(second_sorted_list),number = 100)
    second_time3.delete(0, 'end')
    second_time3.insert(END, label_time3)

def third_ent_box():
    third_result_entry_box.delete(0, 'end')
    third_result_entry_box.insert(END, random_numbers(third_entry_box))
    third_sorted_list.delete(0, 'end')
    third_sorted_list.insert(END, ent_box(third_result_entry_box))
    third_reversed_list.delete(0, 'end')
    third_reversed_list.insert(END, ent_box(third_sorted_list))
    label_time1 = timeit.timeit(lambda: random_numbers(third_entry_box),number = 100)
    third_time1.delete(0, 'end')
    third_time1.insert(END, label_time1)
    label_time2 = timeit.timeit(lambda: ent_box(third_result_entry_box),number = 100)
    third_time2.delete(0, 'end')
    third_time2.insert(END, label_time2)
    label_time3 = timeit.timeit(lambda: reversed_array(third_sorted_list),number = 100)
    third_time3.delete(0, 'end')
    third_time3.insert(END, label_time3)

window = Tk()
window.title('Sorting tables')
window.geometry('1000x650')

Label(window, text = 'List').grid(row = 0,padx = 40)
Label(window, text = 'N1').grid(row = 4, column = 1,padx = 40)
Label(window, text = 'N2').grid(row = 4, column = 2,padx = 40)
Label(window, text = 'N3').grid(row = 4, column = 3,padx = 40)
Label(window, text = 'List').grid(row = 5, column = 0,padx = 40)
Label(window, text = 'Sorted List').grid(row = 6, column = 0,padx = 40)
Label(window, text = 'Reversed Sorted List').grid(row = 7, column = 0,pady = 10,padx = 40)
Label(window, text = 'Time1').grid(row = 8, column = 0, pady = 10, padx = 40)
Label(window, text = 'Time2').grid(row = 9, column = 0, pady = 10, padx = 40)
Label(window, text = 'Time3').grid(row = 10, column = 0, pady = 10, padx = 40)

zero_entry_box = Entry(window)
zero_entry_box.grid(row = 0, column = 1, ipadx = 60)
zero_result_entry_box = Entry(window)
zero_result_entry_box.grid(row = 0, column = 3, pady = 20, ipadx = 60)
zero_sort = Button(window, text = 'Sort',command = zero_ent_box)
zero_sort.grid(row = 0, column = 2, padx = 40)

first_entry_box = Entry(window)
first_entry_box.grid(row = 1, column = 1, pady = 20, ipadx = 60)
first_result_entry_box = Entry(window)
first_result_entry_box.grid(row = 5, column = 1, pady = 20, ipadx = 50)
first_sorted_list = Entry(window)
first_sorted_list.grid(row = 6, column = 1, pady = 20, ipadx = 50)
first_reversed_list = Entry(window)
first_reversed_list.grid(row = 7, column = 1, pady = 20, ipadx = 50)
first_time1 = Entry(window)
first_time1.grid(row = 8, column = 1, pady = 20, ipadx = 50)
first_time2 = Entry(window)
first_time2.grid(row = 9, column = 1, pady = 20, ipadx = 50)
first_time3 = Entry(window)
first_time3.grid(row = 10, column = 1, pady = 20, ipadx = 50)
first_sort = Button(window, text = 'N1', command = first_ent_box)
first_sort.grid(row = 1, column = 0, padx = 40)


second_entry_box = Entry(window)
second_entry_box.grid(row = 2, column = 1, pady = 20, ipadx = 60)
second_result_entry_box = Entry(window)
second_result_entry_box.grid(row = 5, column = 2, pady = 20, ipadx = 50)
second_sorted_list = Entry(window)
second_sorted_list.grid(row = 6, column = 2, pady = 20, ipadx = 50)
second_reversed_list = Entry(window)
second_reversed_list.grid(row = 7, column = 2, pady = 20, ipadx = 50)
second_time1 = Entry(window)
second_time1.grid(row = 8, column = 2, pady = 20, ipadx = 50)
second_time2 = Entry(window)
second_time2.grid(row = 9, column = 2, pady = 20, ipadx = 50)
second_time3 = Entry(window)
second_time3.grid(row = 10, column = 2, pady = 20, ipadx = 50)
second_sort = Button(window, text = 'N2', command = second_ent_box)
second_sort.grid(row = 2, column = 0, padx = 40)

third_entry_box = Entry(window)
third_entry_box.grid(row = 3, column = 1, pady = 20, ipadx = 60)
third_result_entry_box = Entry(window)
third_result_entry_box.grid(row = 5, column = 3, pady = 20, ipadx = 50)
third_sorted_list = Entry(window)
third_sorted_list.grid(row = 6, column = 3, pady = 20, ipadx = 50)
third_reversed_list = Entry(window)
third_reversed_list.grid(row = 7, column = 3, pady = 20, ipadx = 50)
third_time1 = Entry(window)
third_time1.grid(row = 8, column = 3, pady = 20, ipadx = 50)
third_time2 = Entry(window)
third_time2.grid(row = 9, column = 3, pady = 20, ipadx = 50)
third_time3 = Entry(window)
third_time3.grid(row = 10, column = 3, pady = 20, ipadx = 50)
third_sort = Button(window, text = 'N3', command = third_ent_box)
third_sort.grid(row = 3, column = 0, padx = 40)

window.mainloop()

