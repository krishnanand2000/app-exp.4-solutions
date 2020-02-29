import tkinter
from tkinter import *
from tkinter import messagebox

def main_window():
    wdw = tkinter.Tk()
    wdw.title("Calculator")
    welcome = Label (wdw, text="Basic Calculator",justify = CENTER,borderwidth=0,bg = 'CYAN')
    welcome.pack()
    wdw_frame  = Frame(wdw, bd= 3 , height = 500 , width = 500)
    wdw_frame.pack()
    fst_num=Label(wdw_frame,justify=CENTER,text="Enter The First Number :",borderwidth=0,cursor="ARROW")
    fst_num.grid(row=1, column=1)
    global fst_num_entry
    fst_num_entry=Entry(wdw_frame,bd=1,justify=LEFT,width=20)
    fst_num_entry.grid(row = 1, column = 2)

    sec_num=Label(wdw_frame,justify=CENTER,text="Enter The Second Number :",borderwidth=0,cursor="ARROW")
    sec_num.grid(row=2, column=1)
    global sec_num_entry
    sec_num_entry=Entry(wdw_frame,bd=1,justify=LEFT,width=20)
    sec_num_entry.grid(row = 2, column = 2)


    button=Button(wdw_frame,text="ADD",justify=CENTER,borderwidth=2, command = add)
    button.grid(row=3,columnspan=3)

    button=Button(wdw_frame,text="MULTIPLICATION",justify=CENTER,borderwidth=2, command = mul)
    button.grid(row=4,columnspan=3)

    button=Button(wdw_frame,text="DIVISION",justify=CENTER,borderwidth=2, command = dev)
    button.grid(row=5,columnspan=3)

    button=Button(wdw_frame,text="SUBSTRACTION",justify=CENTER,borderwidth=2, command = sub)
    button.grid(row=6,columnspan=3)

    button=Button(wdw_frame,text="MODULO",justify=CENTER,borderwidth=2, command = mod)
    button.grid(row=7,columnspan=3)

    wdw.mainloop()



def add():
    global num1
    global num2

    string_num = fst_num_entry.get()
    num1 = float(string_num)
    string_num_2 = sec_num_entry.get()
    num2 = float(string_num_2)

    tkinter.messagebox.showwarning(title="Addition", message= float(num1+num2))

def mul():
    string_num = fst_num_entry.get()
    num1 = float(string_num)
    string_num_2 = sec_num_entry.get()
    num2 = float(string_num_2)

    tkinter.messagebox.showwarning(title="Addition", message= float(num1*num2))

def dev():
    string_num = fst_num_entry.get()
    num1 = float(string_num)
    string_num_2 = sec_num_entry.get()
    num2 = float(string_num_2)

    tkinter.messagebox.showwarning(title="Addition", message= float(num1/num2))

def sub():
    string_num = fst_num_entry.get()
    num1 = float(string_num)
    string_num_2 = sec_num_entry.get()
    num2 = float(string_num_2)

    tkinter.messagebox.showwarning(title="Addition", message= float(num1-num2))

def mod():
    string_num = fst_num_entry.get()
    num1 = float(string_num)
    string_num_2 = sec_num_entry.get()
    num2 = float(string_num_2)

    tkinter.messagebox.showwarning(title="Addition", message= float(num1%num2))

    
    
main_window()
