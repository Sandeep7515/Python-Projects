import tkinter as tk

def add():
    entry.insert(tk.END,"+")
def sub():
    entry.insert(tk.END,"-")
def mul():
    entry.insert(tk.END,"*")
def div():
    entry.insert(tk.END,"/")
def equal():
        expression = entry.get()
        
        if expression:
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(0, str(result))          
        else:
            entry.delete(0, tk.END)
            entry.insert(tk.END,"Error")
        
def clear():
    entry.delete(0,tk.END)
def greet():
    
    entry.delete(0,tk.END)
    entry.insert(tk.END,"Hello Sandeep")
def X():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])
def one():
    entry.insert(tk.END,"1")
def two():
    entry.insert(tk.END,"2")
def three():
    entry.insert(tk.END,"3")
def four():
    entry.insert(tk.END,"4")
def five():
    entry.insert(tk.END,"5")
def six():
    entry.insert(tk.END,"6")
def seven():
    entry.insert(tk.END,"7")
def eight():
    entry.insert(tk.END,"8")
def nine():
    entry.insert(tk.END,"9")
def zero():
    entry.insert(tk.END,"0")

sandeep = tk.Tk()
sandeep.title("Calculator")
sandeep.geometry("460x528")
sandeep.configure(bg='lightsteelblue')
label=tk.Label(sandeep,text="Calculator",font=('Arial',20,'italic','bold'),bg='lightsteelblue',fg='black')
label.grid(row=0,column=0,columnspan=4,pady=10)
entry=tk.Entry(sandeep,width=22,font=('Times New Roman',30),bd=5,bg='lightgray',fg='black')
entry.grid(row=1,column=0,columnspan=4,pady=5)
buttonAC = tk.Button(sandeep, text="AC",font='bold', padx=35, pady=20,command=clear,bg='steelblue4',fg='white')
buttonAC.grid(row=2, column=0)
buttongreet=tk.Button(text="Greeting",font='bold',padx=68,pady=20,command=greet,bg='lightsteelblue',fg='black')
buttongreet.grid(row=2, column=1,columnspan=2)
buttonX = tk.Button(sandeep, text="<x]",font='bold', padx=34, pady=20,command=X,bg='lightsteelblue',fg='black')
buttonX.grid(row=2, column=3)
button1 = tk.Button(sandeep, text="1",font='bold', padx=42, pady=20,command=one,bg='lightsteelblue',fg='black')
button1.grid(row=3, column=0)
button2 = tk.Button(sandeep, text="2",font='bold', padx=42, pady=20,command=two,bg='lightsteelblue',fg='black')
button2.grid(row=3, column=1)   
button3 = tk.Button(sandeep, text="3",font='bold', padx=45, pady=20,command=three,bg='lightsteelblue',fg='black')
button3.grid(row=3, column=2)
button4 = tk.Button(sandeep, text="4",font='bold', padx=42, pady=20,command=four,bg='lightsteelblue',fg='black')
button4.grid(row=4, column=0)
button5 = tk.Button(sandeep, text="5",font='bold', padx=42, pady=20,command=five,bg='lightsteelblue',fg='black')
button5.grid(row=4, column=1)
button6 = tk.Button(sandeep, text="6",font='bold', padx=45, pady=20,command=six,bg='lightsteelblue',fg='black')
button6.grid(row=4, column=2)
button7 = tk.Button(sandeep, text="7",font='bold', padx=42, pady=20,command=seven,bg='lightsteelblue',fg='black')
button7.grid(row=5, column=0)
button8 = tk.Button(sandeep, text="8",font='bold', padx=42, pady=20,command=eight,bg='lightsteelblue',fg='black')
button8.grid(row=5, column=1)
button9 = tk.Button(sandeep, text="9",font='bold', padx=45, pady=20,command=nine,bg='lightsteelblue',fg='black')
button9.grid(row=5, column=2)
button0 = tk.Button(sandeep, text="0",font='bold', padx=42, pady=20,command=zero,bg='lightsteelblue',fg='black')
button0.grid(row=6, column=0)
button_add = tk.Button(sandeep, text="+",font='bold', padx=42, pady=20,command=add,bg='lightsteelblue',fg='black')
button_add.grid(row=3, column=3)
button_sub = tk.Button(sandeep, text="-",font='bold', padx=44, pady=20,command=sub,bg='lightsteelblue',fg='black')
button_sub.grid(row=4, column=3)
button_mul = tk.Button(sandeep, text="*",font='bold', padx=44, pady=20,command=mul,bg='lightsteelblue',fg='black')
button_mul.grid(row=5, column=3)    
button_div = tk.Button(sandeep, text="/",font='bold', padx=45, pady=20,command=div,bg='lightsteelblue',fg='black')
button_div.grid(row=6, column=3)
button_equal = tk.Button(sandeep, text="=",font='bold', padx=100, pady=20,command=equal,bg='lightsteelblue',fg='black')
button_equal.grid(row=6, column=1,columnspan=2)
sandeep.mainloop()



