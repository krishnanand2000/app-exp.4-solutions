import tkinter
from tkinter import *
from tkinter import messagebox

def main_window():
    wdw = tkinter.Tk()
    wdw.title("Prime Number")
    wdw_frame  = Frame(wdw, bd= 3 , height = 500 , width = 500)
    wdw_frame.pack()
    
    num_in=Label(wdw_frame,justify=CENTER,text="Enter The Number",borderwidth=0,cursor="ARROW")
    num_in.grid(row=1, column=2)
    
    global num_in_entry
    num_in_entry=Entry(wdw_frame,bd=1,justify=LEFT,width=20)
    num_in_entry.grid(row = 2, column = 2)
    
    button=Button(wdw_frame,text="Check",justify=CENTER,borderwidth=2,command = prime_no)
    button.grid(row=6,columnspan=3)
    wdw.mainloop()



def prime_no():
    global num
    string_num = num_in_entry.get()
    num = int(string_num)
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                flag = 1
                break
            else:
                flag = 0
    else:
        flag = 1
    if (flag == 1):
        tkinter.messagebox.showwarning(title="Result",message="The number is not prime")
    if (flag == 0):
        tkinter.messagebox.showwarning(title="Result",message="The number is prime")
    
    
main_window()
