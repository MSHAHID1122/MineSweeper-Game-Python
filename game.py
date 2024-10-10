from tkinter import *
from Class.Cell import CELL 
import Class.percentge as p
import Class.setting as setting


root = Tk()
root.title("MINESWEEPER")
root.minsize(setting.WIDTH, setting.HEIGHT)
root.resizable(False, False)


l1 = Label(root, text="welcome to tkinter", bg="gray", fg="white")
l1.place(x=90, y=800)
l1.pack()

top_frame = Frame(root, bg="light blue", width=p.width_percnt(100), height=p.height_percnt(15))
top_frame.place(x=0, y=0)

center_frame = Frame(root, bg="light green", width=setting.WIDTH -
                     p.width_percnt(5), height=setting.HEIGHT-p.height_percnt(10))
center_frame.place(x=p.width_percnt(10) + 60, y=p.height_percnt(15))

right_frame = Frame(root, bg='light green',
                    width=p.width_percnt(20), height=700)
right_frame.place(x=setting.WIDTH-p.width_percnt(5)-99, y=p.height_percnt(15))

left_frame = Frame(root, bg="light green",
                   width=p.width_percnt(17), height=700)
left_frame.place(x=0, y=p.height_percnt(15))


for x in range(setting.GRID_SIZE):
    for y in range(setting.GRID_SIZE):
        c = CELL(x, y)
        c.createbutton(center_frame)
        c.btn.grid(row=x, column=y)

CELL.rand_mine_gern()
CELL.createlabel(top_frame)
CELL.Label.place(x=390, y=0)
root.mainloop()
