from tkinter import *
from tkinter import messagebox

def details():
    messagebox.showinfo("Your Details",f"Name: {name.get()}\nRoll No.:{Roll.get()}\nDepartment:{Dept.get()}\nPassword:{Pas.get()}")
    
sandeep=Tk()
sandeep.title("Details form created by Sandeep") 
sandeep.geometry('500x500')
sandeep.config(bg="black") 


head=Label(sandeep,text="DETAILS FORM",
           font=('',20,'italic'),
           fg='white',
           bg='green',  
           bd=10,
           padx=100)
head.pack(side='top',pady=40)

name_frame=Frame(sandeep,bg='black')
name_frame.pack(pady=10)
Name=Label(name_frame,text="Enter your Name          : ",width=20,font=20,fg='lime',bg='black',anchor='w')
Name.pack(side='left',padx=3)
name=Entry(name_frame,width=20,font=20,bg='gray21',fg='white',insertbackground='white')
name.pack(side='left',padx=5)


roll_frame=Frame(sandeep,bg='black')
roll_frame.pack(pady=10)
roll=Label(roll_frame,text="Enter your Roll No.       : ",width=20,font=20,fg='lime',bg='black',anchor='w')
roll.pack(side='left',padx=3)
Roll=Entry(roll_frame,width=20,font=20,bg='gray21',fg='white',insertbackground='white')
Roll.pack(side='left',padx=5)


dept_frame=Frame(sandeep,bg='black')
dept_frame.pack(pady=10)
dept=Label(dept_frame,text="Enter your Department : ",width=20,font=20,fg='lime',bg='black',anchor='w')
dept.pack(side='left',padx=3)
Dept=Entry(dept_frame,width=20,font=20,bg='gray21',fg='white',insertbackground='white')
Dept.pack(side='left',padx=5)


pass_frame=Frame(sandeep,bg='black')
pass_frame.pack(pady=10)
pas=Label(pass_frame,text="Enter your Password    : ",width=20,font=20,fg='lime',bg='black',anchor='w')
pas.pack(side='left',padx=3)
Pas=Entry(pass_frame,show="*",width=20,font=20,bg='gray21',fg='white',insertbackground='white')
Pas.pack(side='left',padx=5)


submit=Button(sandeep,text="Submit",
             font=20,
             width=10,
             bd=5,
             command=details,
             bg='green',  
             fg='white',
             activebackground='darkgreen', 
             activeforeground='white')
submit.pack(pady=20)

sandeep.mainloop()