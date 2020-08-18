from tkinter import *
import parser

root = Tk()
root.title('Calculator')
root.configure(background="light blue")
root.geometry("260x220")
# Input_Section
x = 0


def Set_Value(num):
    global x
    dis.insert(x, num)
    x += 1


def Back_space():
    all_value = dis.get()
    if len(all_value):
        new_value = all_value[:-1]
        All_Clear()
        dis.insert(0, new_value)
    else:
        All_Clear()
        dis.insert(0, "Invalid")


def All_Clear():
    dis.delete(0, END)


def operator(op):
    global x
    ln = len(op)
    dis.insert(x, op)
    x += ln


# Expression
def cal():
    all_value = dis.get()
    try:
        a = parser.expr(all_value).compile()
        res = eval(a)
        All_Clear()
        dis.insert(0, res)
    except Exception:
        All_Clear()
        dis.insert(0, "Invalid")


def facto(num):
    if num == 1:
        return 1
    elif num < 1:
        All_Clear()
        dis.insert(0, "Invalid")
    else:
        return num * facto(num - 1)


def factorial_dis():
    all_value = dis.get()
    try:
        num = int(all_value)
        num1 = facto(num)
        All_Clear()
        dis.insert(0, num1)
    except Exception:
        All_Clear()
        dis.insert(0, "Invalid")
def menu_fun():
    All_Clear()
    dis.insert(0, "---------  Mahadi Hasan Tanmoy  ---------")
mymenu = Menu(root)
root.config(menu=mymenu)
submenu = Menu(mymenu)
mymenu.add_cascade(label="View",menu=submenu)
submenu.add_command(label="Dev. Detail",command=menu_fun)
submenu.add_separator()

# Display_Section
dis = Entry(root)
dis.grid(row=0, column=0, columnspan=8, ipadx=55,ipady=10, padx=10, pady=12)

# Button_Num_Section
Button(root, text="  7  ", width=5, height=2, fg='black', bg='light blue', bd=1, command=lambda: Set_Value(7)).grid(row=2, column=0)
Button(root, text="  8  ", width=5, height=2, fg='black', bg='light blue', bd=1, command=lambda: Set_Value(8)).grid(row=2, column=1)
Button(root, text="  9  ", width=5, height=2, fg='black', bg='light blue', bd=1, command=lambda: Set_Value(9)).grid(row=2, column=2)

Button(root, text="  4  ", width=5, height=2, fg='black', bg='light blue', bd=1, command=lambda: Set_Value(4)).grid(row=3, column=0)
Button(root, text="  5  ", width=5, height=2, fg='black', bg='white', bd=1, command=lambda: Set_Value(5)).grid(row=3, column=1)
Button(root, text="  6  ", width=5, height=2, fg='black', bg='light blue', bd=1, command=lambda: Set_Value(6)).grid(row=3, column=2)

Button(root, text="  1  ", width=5, height=2, fg='black', bg='light blue', bd=1, command=lambda: Set_Value(1)).grid(row=4, column=0)
Button(root, text="  2  ", width=5, height=2, fg='black', bg='light blue', bd=1, command=lambda: Set_Value(2)).grid(row=4, column=1)
Button(root, text="  3  ", width=5, height=2, fg='black', bg='light blue', bd=1, command=lambda: Set_Value(3)).grid(row=4, column=2)

# Button_functional_section
Button(root, text="  C  ", fg='white', bg='grey', bd=1, width=5, height=2, command=lambda: All_Clear()).grid(row=5,column=0)
Button(root, text="  0  ", width=5, height=2, fg='black', bg='light blue', bd=1, command=lambda: Set_Value(0)).grid(row=5, column=1)
Button(root, text="  .  ", width=5, height=2, fg='white', bg='grey', bd=1, command=lambda: operator(".")).grid(row=5,column=2)

Button(root, text="  +  ", width=5, height=2, fg='white', bg='grey', bd=1, command=lambda: operator("+")).grid(row=2,column=3)
Button(root, text="  -  ", width=5, height=2, fg='white', bg='grey', bd=1, command=lambda: operator("-")).grid(row=3,column=3)
Button(root, text="  x  ", width=5, height=2, fg='white', bg='grey', bd=1, command=lambda: operator("*")).grid(row=4,column=3)
Button(root, text="  ÷  ", width=5, height=2, fg='white', bg='grey', bd=1, command=lambda: operator("/")).grid(row=5,column=3)

Button(root, text="  π  ", width=5, height=2, fg='white', bg='grey', bd=1, command=lambda: operator("*3.1415926535")).grid(row=2, column=4)
Button(root, text="  %  ", width=5, height=2, fg='black', bg='white', bd=1, command=lambda: operator("%")).grid(row=3,column=4)
Button(root, text="   (   ", width=5, height=2, fg='white', bg='grey', bd=1, command=lambda: operator("(")).grid(row=4,column=4)
Button(root, text="  =  ", width=5, height=2, fg='black', bg='light blue', bd=1, command=lambda: cal()).grid(row=5, column=4)

Button(root, text=" ⌫ ", width=5, height=2, fg='white', bg='grey', bd=1, command=lambda: Back_space()).grid(row=2, column=5)
Button(root, text="   !   ", width=5, height=2, fg='white', bg='grey', bd=1, command=lambda: factorial_dis()).grid(row=3, column=5)
Button(root, text="   )   ", width=5, height=2, fg='white', bg='grey', bd=1, command=lambda: operator(")")).grid(row=4,column=5)
Button(root, text="  x²  ", width=5, height=2, fg='white', bg='grey', bd=1, command=lambda: operator("**2")).grid(row=5,column=5)

root.mainloop()
