from math import fabs, sqrt, trunc
from sys import flags
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def clear_coord():
    global coord, canvas
    coord.clear()
    canvas.delete("all")
def get_points(_entry):
    try:
        new_points = list(float(elem) for elem in  _entry.get().split())
    except ValueError:
        showerror("Incorect Input!", "Try Again")
        clear_coord()
        return None
    return new_points
def add_points():
    x_points = get_points(x_point_entry)
    y_points = get_points(y_point_entry)
    if not x_points or not y_points:
        showerror("Incorect Input!", "Empty points.")
    else:
        length = min(len(x_points), len(y_points))
        for i in range(length):
            new_point = point(x_points[i], y_points[i]);
            coord.append(new_point)
            add_point(new_point)
def add_point(p):
    canvas.create_oval(p.x - 2, p.y - 2, p.x + 2, p.y + 2, width = 3)
def add_line(lhs, rhs):
    canvas.create_line(lhs.x, lhs.y, rhs.x, rhs.y)
def find_triangles(coords):
    count = count1 = 0
    flag = [True, True]
    for i in range(len(coord)):
        if coord[i] != coord[0]:
            count += 1
            if flag[0] and coord[i].x - coord[0].x != 0:
                tg = (coord[i].y - coord[0].y) / (coord[i].x - coord[0].x)
                flag[0] = False
                count1 += 1
            elif coord[i].x - coord[0].x != 0:
                if tg != (coord[i].y - coord[0].y) / (coord[i].x - coord[0].x):
                    count1 += 1
            elif flag[1]:
                count1 += 1
                flag[1] = True
    if len(coord) < 3:
        showerror("Find Error!", "its not possible to find trianlge \
                        from less than tree points.")
    elif count1 < 2 or count < 2:
        showerror("Incorrect Input!", "finded points have tangenat.")
    else:
        eps = 1e-5
        flag = True
        for i in range(len(coord)):
            for j in range(i + 1, len(coord)):
                for k in range(j + 1, len(coord)):
                    x1, x2, x3 = coord[i].x, coord[j].x, coord[k].x
                    y1, y2, y3 = coord[i].y, coord[j].y, coord[k].y
                    if (x3 - x1) * (x2 - x1) != (y3 - y1) * (y2 - y1):
                        len_1 = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                        len_2 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
                        len_3 = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
                        if flag:
                            eps = abs(len_1 - len_2)
                            temp_1, temp_2, temp_3 = coord[i], coord[j], coord[k]
                            flag = False
                        if abs(len_1 - len_2) < eps:
                            e = abs(len_1 - len_2)
                            temp_1, temp_2, temp_3 = coord[i], coord[j], coord[k]
                        if abs(len_2 - len_3) < eps:
                            e = abs(len_2 - len_3)
                            temp_1, temp_2, temp_3 = coord[i], coord[j], coord[k]
                        if abs(len_3 - len_1) < eps:
                            e = abs(len_1 - len_2)
                            temp_1, temp_2, temp_3 = coord[i], coord[j], coord[k]
                           
        x_m = temp_1.x
        y_m = temp_1.y
        min_x = temp_1.x
        min_y = temp_1.y
        for i in range(len(coord)):
            if coord[i].x < min_x:
                min_x = coord[i].x
            if coord[i].y < min_y:
                min_y = coord[i].y
            if coord[i].x > x_m:
                x_m = coord[i].x
            if coord[i].y > y_m:
                y_m = coord[i].y
        add_line(temp_1, temp_2)
        add_line(temp_2, temp_3)
        add_line(temp_1, temp_3)
def click(event):
    p = point(event.x, event.y)
    coord.append(p)
    add_point(p)
root = Tk()
root.geometry("800x600")
root.title("Triangles With minimum area")
canvas = Canvas(root, width = 600, height = 600)
canvas.place(x = 210, y = 10)
canvas.bind('<1>',click)
coord = []
Label(root, text="X Coordinates by single Space").place(x = 10, y = 10)
Label(root, text="Y Coordinates by single Space").place(x = 10, y = 100)
x_point_entry = ttk.Entry(root)
y_point_entry = ttk.Entry(root)
Button(text="Add Points",font="20",pady="20",\
    command = lambda : add_points()).place(x = 10, y = 180, width=190)
Button(text="Find Triangle",font="20",pady="20",\
    command = lambda : find_triangles(coord)).place(x = 10, y = 270, width=190)
Button(text="Clear Coordinate",font="20",pady="20",\
    command = lambda : clear_coord()).place(x = 10, y = 360, width=190)
Button(text="Exit",font="20",pady="20",\
    command = lambda : root.destroy()).place(x = 10, y = 450, width=190)
x_point_entry.place(height = 25, width=190, x = 10, y = 44)
y_point_entry.place(height = 25, width=190, x = 10, y = 134)
root.mainloop()
