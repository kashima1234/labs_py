from tkinter import *
from math import sqrt
import tkinter.messagebox as mb
circles_list = []
points_list = []
circle_drawing = []
act_log = []
res_line = [] 
#==========================================================================================
def str_to_float(str):
    try:
        x = float(str)
        return x
    except:
        return str

def create_circle(xc, yc, r):
    circle_id = canv.create_oval(xc - r, yc - r, xc + r, yc + r, width=3, outline='dark red', activeoutline='red3')
    circle_drawing.append(r)
    circle_drawing.append(circle_id)
    act_log.append(circle_id)

def create_point(x, y):
    point_id = canv.create_oval(x - 0.1, y - 0.1, x + 0.1, y + 0.1, width=3, outline='black', fill='black', activeoutline='gray34', activefill='gray34')
    act_log.append(point_id)
    points_list.append([x, y, point_id])

def xc_yc_coords(event):
    circle_drawing.clear()
    circle_drawing.append(event.x)
    circle_drawing.append(event.y)
    create_circle(circle_drawing[0], circle_drawing[1], 0.1)

def point_coords(event):
    xp = event.x
    yp = event.y
    create_point(xp, yp)

def radius(event):
    x1, y1 = event.x, event.y
    x2, y2 = circle_drawing[0], circle_drawing[1]
    circle_drawing[2] = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
    canv.coords(circle_drawing[3], x2 - circle_drawing[2], y2 - circle_drawing[2], x2 + circle_drawing[2], y2 + circle_drawing[2])

def finish_circle_draw(event):
    circles_list.append(circle_drawing.copy())
    canv.unbind('<Button-1>')
    canv.unbind('<B1-Motion>')
    canv.unbind('<ButtonRelease-1>')

def start_circle_draw():
    circle_drawing.clear()
    canv.bind('<Button-1>', xc_yc_coords)
    canv.bind('<B1-Motion>', radius)
    canv.bind('<ButtonRelease-1>', finish_circle_draw)

def finish_point_draw(event):
    canv.unbind('<Button-1>')
    canv.unbind('<ButtonRelease-1>')

def start_point_draw():
    lblpointerr.grid_forget()
    circle_drawing.clear()
    canv.bind('<Button-1>', point_coords)
    canv.bind('<ButtonRelease-1>', finish_point_draw)

def point_text():
    lblpointerr.grid_forget()
    pointx = str_to_float(entpointx.get())
    pointy = str_to_float(entpointy.get())
    if type(pointx) != float or type(pointy) != float:
        lblpointerr.grid(row=5, column=0)
        return
    create_point(pointx, pointy)
    entpointx.delete(0, END)
    entpointy.delete(0, END)

def circle_text():
    lblcircleerr.grid_forget()
    circlex = str_to_float(entcirclex.get())
    circley = str_to_float(entcircley.get())
    circler = str_to_float(entcircler.get())
    if type(circlex) != float or type(circley) != float or  type(circler) != float:
        lblcircleerr.grid(row=7, column=1)
        return
    create_circle(circlex, circley, circler)
    entcirclex.delete(0, END)
    entcircley.delete(0, END)
    entcircler.delete(0, END)

def undo_last_act():
    if len(act_log) != 0:
        try:
            canv.delete(res_line[0])
        except:
            None
        res_line.clear()
        canv.delete(act_log[-1])
        if len(circles_list) != 0:
            if circles_list[-1][3] == act_log[-1]:
                circles_list.pop()
        elif len(points_list) != 0:
            if points_list[-1][2] == act_log[-1]:
                points_list.pop()
        act_log.pop()

def zoom(event):
    if (event.delta > 0):
        canv.scale("all", event.x, event.y, 1.1, 1.1)
    elif (event.delta < 0):
        canv.scale("all", event.x, event.y, 0.9, 0.9)

def deleteitem(event):
    item = canv.find_withtag(CURRENT)
    if len(item) == 0:
        return
    for i in range(len(circles_list)):
        if circles_list[i][3] == item[0]:
            circles_list.pop()
            break
    for i in range(len(points_list)):
        if points_list[i][2] == item[0]:
            points_list.pop()
            break
    canv.delete(item[0])

def finish_deleteitem(event):
    canv.unbind('<Button-1>')
    canv.unbind('<ButtonRelease-1>')

def start_deleteitem():
    canv.bind('<Button-1>', deleteitem)
    canv.bind('<ButtonRelease-1>', finish_deleteitem)

def finish_edit_item(event):
    canv.unbind('<Button-1>')
    canv.unbind('<ButtonRelease-1>')

def start_edit_circle(circle_ind):
    entcirclex.insert(0, str(circles_list[circle_ind][0]))
    entcircley.insert(0, str(circles_list[circle_ind][1]))
    entcircler.insert(0, str(circles_list[circle_ind][2]))
    canv.delete(circles_list[circle_ind][3])
    circles_list.pop(circle_ind)

def start_edit_point(point_ind):
    entpointx.insert(0, str(points_list[point_ind][0]))
    entpointy.insert(0, str(points_list[point_ind][1]))
    canv.delete(points_list[point_ind][2])
    points_list.pop(point_ind)

def edit_item(event):
    item = canv.find_withtag(CURRENT)
    if len(item) == 0:
        return
    for i in range(len(circles_list)):
        if circles_list[i][3] == item[0]:
            start_edit_circle(i)
    for i in range(len(points_list)):
        if points_list[i][2] == item[0]:
            start_edit_point(i)

def start_edit_item():
    canv.bind('<Button-1>', edit_item)
    canv.bind('<ButtonRelease-1>', finish_edit_item)

def aboutprog():
    mb.showinfo(title='О программе', message='На плоскости заданы множество точек А и множество окружностей В. Найти \
две такие различные точки из А, что проходящая через них прямая пересекается \
с максимальным количеством окружностей из В и разделяет множество точек на две \
равные части.')

def aboutauthor():
    mb.showinfo(title='Об авторе', message='Золотухин Алексей ИУ7-44Б')

def quitprog():
    win.quit()

def calculate():
    print(points_list)
    print(circles_list)
    reslbl.grid_forget()
    points = points_list
    lines = []
    try:
        canv.delete(res_line[0])
    except:
        None
    res_line.clear()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            line = [points[i], points[j], 0, 0]
            for point0 in points:
                cross_prod = (points[j][0] - points[i][0])*(point0[1] - points[i][1]) - (points[j][1] - points[i][1])*(point0[0] - points[i][0])
                if cross_prod > 0:
                    line[2] += 1
                elif cross_prod < 0:
                    line[2] -= 1
            if line[2] != 0:
                continue
            else:
                lines.append(line)
    if len(lines) == 0:
        return
    for line in lines:
        for circle in circles_list:
            d = abs((line[1][0] - line[0][0]) * (circle[1] - line[0][1]) - (line[1][1] - line[0][1]) * (circle[0] - line[0][0])) / sqrt((line[1][1] - line[0][1]) * (line[1][1] - line[0][1]) + (line[1][0] - line[0][0]) * (line[1][0] - line[0][0]))
            if circle[2] > d:
                line[3] += 1
    max_line = lines[0]
    for line in lines:
        if max_line[3] < line[3]:
            max_line = line
    coords1 = canv.coords(max_line[0][2])
    coords2 = canv.coords(max_line[1][2])
    res_line_id = canv.create_line(coords1[0], coords1[1], coords2[0], coords2[1], fill='blue', width=2)
    res_line.append(res_line_id)
    reslbl.configure(text=f'Прямая проходит через точки \nx1 = {max_line[0][0]} y1 = {max_line[0][1]} \nx2 = {max_line[1][0]} y2 = {max_line[1][1]}')
    reslbl.grid(row=3, column=0, columnspan=3)
#==========================================================================================
win = Tk()

canv = Canvas(win, width=1000, height=1000, bg='white')
canv.grid(row=0, column=0)

frmpaint = Frame(win)
frmtext = Frame(win)
circ_btn = Button(frmpaint, text='◯',command=start_circle_draw)
circ_btn.grid(row=0, column=0)

point_btn = Button(frmpaint, text='◦',command=start_point_draw)
point_btn.grid(row=0, column=1)

undo_btn = Button(frmpaint, text='↺',command=undo_last_act)
undo_btn.grid(row=0, column=2)

del_btn = Button(frmpaint, text='⌫',command=start_deleteitem)
del_btn.grid(row=1, column=0)

edit_btn = Button(frmpaint, text='✎',command=start_edit_item)
edit_btn.grid(row=1, column=1)

calc_btn = Button(frmpaint, width=30, height=4, text='Найти прямую пересекающую\nнабольшее число окружностей\nи делящую множество\nточек пополам',command=calculate)
calc_btn.grid(row=2, column=0, columnspan=10)

reslbl = Label(frmpaint)
reslbl.grid(row=3, column=0, columnspan=10)

frmpaint.grid(row=0, column=1, sticky=N)

entpointx = Entry(frmtext)
lblpointx = Label(frmtext, text='Координата Х точки')
lblpointx.grid(row=0, column=0)
entpointx.grid(row=1, column=0)

entpointy = Entry(frmtext)
lblpointy = Label(frmtext, text='Координата Y точки')
lblpointy.grid(row=2, column=0)
entpointy.grid(row=3, column=0)

btnpointtext = Button(frmtext, text='Нарисовать точку', command=point_text)
lblpointerr = Label(frmtext, text='Некорректные координаты точки')
btnpointtext.grid(row=4, column=0)

entcirclex = Entry(frmtext)
lblcirclex = Label(frmtext, text='Координата Х \nцентра окружности')
lblcirclex.grid(row=0, column=1)
entcirclex.grid(row=1, column=1)

entcircley = Entry(frmtext)
lblcircley = Label(frmtext, text='Координата Y \nцентра окружности')
lblcircley.grid(row=2, column=1)
entcircley.grid(row=3, column=1)

entcircler = Entry(frmtext)
lblcircler = Label(frmtext, text='Радиус окружности')
lblcircler.grid(row=4, column=1)
entcircler.grid(row=5, column=1)

btncircletext = Button(frmtext, text='Нарисовать окружность', command=circle_text)
lblcircleerr = Label(frmtext, text='Некорректные данные окружности')
btncircletext.grid(row=6, column=1)

mainmenu = Menu(win) 
win.config(menu=mainmenu) 
 
mainmenu.add_command(label='О программе', command=aboutprog)
mainmenu.add_command(label='Об авторе', command=aboutauthor)
mainmenu.add_command(label='Выход', command=quitprog)

frmtext.grid(row=0, column=2, sticky=N)

canv.bind("<MouseWheel>", zoom)

