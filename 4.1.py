import tkinter
from tkinter import *
from tkinter import messagebox
import csv

def main_window():

    info_window = tkinter.Tk(screenName='help me')
    info_window.title("mohit")
    wndw_frame = Frame(info_window, bd= 3 , height = 500 , width = 500)
    wndw_frame.pack()
    button = Button(wndw_frame,justify = CENTER, text="Display", command = print , message = "hello )
    button.grid(row=6,column=2)
    info_window.mainloop()

def print():
    tkinter.messagebox.showwarning(title="popup",message="WELCOME TO SRM")

main_window()
