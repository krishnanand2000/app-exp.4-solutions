import tkinter
from tkinter import *
from tkinter import messagebox

def main_window():
    global window
    window = tkinter.Tk()
    window.title("GPA Calclator")
    heading = Label(window,text="Welcome to GPA Calculator", justify = CENTER)
    heading.pack()

    common_detail_frame=Frame(window,bd=3,height=500,width=500)
    common_detail_frame.pack(side=LEFT)

    name_label=Label(common_detail_frame,justify=LEFT,text="Name ",borderwidth=10)
    name_label.grid(row=1,column=1)
    global name_entry
    name_entry=Entry(common_detail_frame,justify=LEFT,width=20)
    name_entry.grid(row=1,column=2)

    register_label=Label(common_detail_frame,justify=LEFT,text="Registration Number ",borderwidth=10)
    register_label.grid(row=2,column=1)
    register_entry=Entry(common_detail_frame,justify=LEFT,width=20)
    register_entry.grid(row=2,column=2)

    email_label=Label(common_detail_frame,justify=LEFT,text="Email ID ",borderwidth=10)
    email_label.grid(row=3,column=1)
    email_entry=Entry(common_detail_frame,justify=LEFT,width=20)
    email_entry.grid(row=3,column=2)

    checkbox_detail_frame=Frame(window,bd=3,height=500,width=500)
    checkbox_detail_frame.pack(side=LEFT)

    department_label=Label(checkbox_detail_frame,justify=LEFT,text="Select the Student's Department",borderwidth=10)
    department_label.grid(row=1)

    var1=IntVar()
    CSE_CB=Checkbutton(checkbox_detail_frame,text="CSE",variable=var1, onvalue=1, offvalue=0)
    CSE_CB.grid(row=2)

    var2=IntVar()
    EEE_CB=Checkbutton(checkbox_detail_frame,text="EEE",variable=var2, onvalue=1, offvalue=0)
    EEE_CB.grid(row=3)

    var3=IntVar()
    ECE_CB=Checkbutton(checkbox_detail_frame,text="ECE",variable=var3, onvalue=1, offvalue=0)
    ECE_CB.grid(row=4)

    var4=IntVar()
    Civil_CB=Checkbutton(checkbox_detail_frame,text="Civil",variable=var4, onvalue=1, offvalue=0)
    Civil_CB.grid(row=5)

    var5=IntVar()
    Mech_CB=Checkbutton(checkbox_detail_frame,text="Mechanical",variable=var5, onvalue=1, offvalue=0)
    Mech_CB.grid(row=6)

    subject_selection_frame=Frame(window,bd=3,height=500,width=500)
    subject_selection_frame.pack(side=LEFT)

    subject_label=Label(subject_selection_frame,justify=LEFT,text="Select the Student's Subject",borderwidth=10)
    subject_label.grid(row=1)

    global varsub1
    varsub1=IntVar()
    Maths_CB=Checkbutton(subject_selection_frame,text="Maths",variable=varsub1)
    Maths_CB.grid(row=2)

    global varsub2
    varsub2=IntVar()
    English_CB=Checkbutton(subject_selection_frame,text="English",variable=varsub2, onvalue=1, offvalue=0)
    English_CB.grid(row=3)

    global varsub3
    varsub3=IntVar()
    Computer_CB=Checkbutton(subject_selection_frame,text="Computer",variable=varsub3, onvalue=1, offvalue=0)
    Computer_CB.grid(row=4)

    global varsub4
    varsub4=IntVar()
    Soil_CB=Checkbutton(subject_selection_frame,text="Soil",variable=varsub4, onvalue=1, offvalue=0)
    Soil_CB.grid(row=5)

    global varsub5
    varsub5=IntVar()
    Mechanics_CB=Checkbutton(subject_selection_frame,text="Mechanics",variable=varsub5, onvalue=1, offvalue=0)
    Mechanics_CB.grid(row=6)

    global varsub6
    varsub6=IntVar()
    Network_CB=Checkbutton(subject_selection_frame,text="Network",variable=varsub6, onvalue=1, offvalue=0)
    Network_CB.grid(row=7)

    global varsub7
    varsub7=IntVar()
    CC_CB=Checkbutton(subject_selection_frame,text="Computer Communication",variable=varsub7, onvalue=1, offvalue=0)
    CC_CB.grid(row=8)

    global varsub8
    varsub8=IntVar()
    Astrology_CB=Checkbutton(subject_selection_frame,text="Astrology",variable=varsub8, onvalue=1, offvalue=0)
    Astrology_CB.grid(row=9)
    
    global Marks_input_frame
    Marks_input_frame=Frame(window,bd=3,height=500,width=500)
    Marks_input_frame.pack(side=LEFT)

    Marks_label=Label(Marks_input_frame,justify=LEFT,text="Enter Student's Marks",borderwidth=20)
    Marks_label.grid(row=1,columnspan=3)

    subject1_Label=Label(Marks_input_frame,justify=LEFT,text="Subject 1",borderwidth=10)
    subject1_Label.grid(row=2,column=1)

    global Subject1_Entry
    Subject1_Entry=Entry(Marks_input_frame,justify=LEFT,width=10)
    Subject1_Entry.grid(row=2,column=2)

    subject2_Label=Label(Marks_input_frame,justify=LEFT,text="Subject 2",borderwidth=10)
    subject2_Label.grid(row=3,column=1)

    global Subject2_Entry
    Subject2_Entry=Entry(Marks_input_frame,justify=LEFT,width=10)
    Subject2_Entry.grid(row=3,column=2)

    subject3_Label=Label(Marks_input_frame,justify=LEFT,text="Subject 3",borderwidth=10)
    subject3_Label.grid(row=4,column=1)

    global Subject3_Entry
    Subject3_Entry=Entry(Marks_input_frame,justify=LEFT,width=10)
    Subject3_Entry.grid(row=4,column=2)

    subject4_Label=Label(Marks_input_frame,justify=LEFT,text="Subject 4",borderwidth=10)
    subject4_Label.grid(row=5,column=1)

    global Subject4_Entry
    Subject4_Entry=Entry(Marks_input_frame,justify=LEFT,width=10)
    Subject4_Entry.grid(row=5,column=2)

    subject5_Label=Label(Marks_input_frame,justify=LEFT,text="Subject 5",borderwidth=10)
    subject5_Label.grid(row=6,column=1)

    global Subject5_Entry
    Subject5_Entry=Entry(Marks_input_frame,justify=LEFT,width=10)
    Subject5_Entry.grid(row=6,column=2)

    submit_button=Button(window, text="Get CGPA", justify=CENTER,command=clicked_cgpa)
    submit_button.pack(side=LEFT)

    window.mainloop()

def clicked_cgpa():
    got_marks1=Subject1_Entry.get()
    got_marks2=Subject2_Entry.get()
    got_marks3=Subject3_Entry.get()
    got_marks4=Subject4_Entry.get()
    got_marks5=Subject5_Entry.get()
    got_name=name_entry.get()

    gpa=((int(got_marks1)+int(got_marks2)+int(got_marks3)+int(got_marks4)+int(got_marks5))/500)*10
    cat="GPA earned by ",got_name," is ", gpa
    tkinter.messagebox.showinfo(title="CGPA",message=cat)

main_window()