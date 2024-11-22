from tkinter import *
exp = ""

def press(num):
    global exp
    exp = exp + str(num)
    equation.set(exp)

def equal_press():
    try:
        global exp
        total = str(eval(exp))
        equation.set(total)
        exp = ""
    except:
        equation.set("error")
        exp = ""

def cl():
    global exp
    exp = ""
    equation.set("")

def delete():
    global exp
    exp = exp[:-1]
    equation.set(exp)

root = Tk()
root.title("CALCULATOR")
root.geometry('400x500')
root.config(borderwidth=5, relief="solid")
equation = StringVar()
txt = Entry(root, font=('Arial', 24), bd=5, relief="solid", justify="right", textvariable=equation)
txt.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button1 = Button(root, text='1', fg='black', relief="raised", command=lambda: press(1), height=2, width=5, bg='lightblue', font=('Arial', 16, 'bold'), bd=4)
button1.grid(row=5, column=0, padx=5, pady=5)

button2 = Button(root, text='2', fg='black', relief="raised", command=lambda: press(2), height=2, width=5, bg='lightblue', font=('Arial', 16, 'bold'), bd=4)
button2.grid(row=5, column=1, padx=5, pady=5)

button3 = Button(root, text='3', fg='black', relief="raised", command=lambda: press(3), height=2, width=5, bg='lightblue', font=('Arial', 16, 'bold'), bd=4)
button3.grid(row=5, column=2, padx=5, pady=5)

button4 = Button(root, text='4', fg='black', relief="raised", command=lambda: press(4), height=2, width=5, bg='lightblue', font=('Arial', 16, 'bold'), bd=4)
button4.grid(row=4, column=0, padx=5, pady=5)

button5 = Button(root, text='5', fg='black', relief="raised", command=lambda: press(5), height=2, width=5, bg='lightblue', font=('Arial', 16, 'bold'), bd=4)
button5.grid(row=4, column=1, padx=5, pady=5)

button6 = Button(root, text='6', fg='black', relief="raised", command=lambda: press(6), height=2, width=5, bg='lightblue', font=('Arial', 16, 'bold'), bd=4)
button6.grid(row=4, column=2, padx=5, pady=5)

button7 = Button(root, text='7', fg='black', relief="raised", command=lambda: press(7), height=2, width=5, bg='lightblue', font=('Arial', 16, 'bold'), bd=4)
button7.grid(row=3, column=0, padx=5, pady=5)

button8 = Button(root, text='8', fg='black', relief="raised", command=lambda: press(8), height=2, width=5, bg='lightblue', font=('Arial', 16, 'bold'), bd=4)
button8.grid(row=3, column=1, padx=5, pady=5)

button9 = Button(root, text='9', fg='black', relief="raised", command=lambda: press(9), height=2, width=5, bg='lightblue', font=('Arial', 16, 'bold'), bd=4)
button9.grid(row=3, column=2, padx=5, pady=5)

button0 = Button(root, text='0', fg='black', relief="raised", command=lambda: press(0), height=2, width=5, bg='lightblue', font=('Arial', 16, 'bold'), bd=4)
button0.grid(row=6, column=1, padx=5, pady=5)

addition = Button(root, text='+', fg='black', relief="raised", command=lambda: press('+'), height=2, width=5, bg='lightblue', font=('Arial', 16, 'bold'), bd=4)
addition.grid(row=5, column=3, padx=5, pady=5)

subtraction = Button(root, text='-', fg='black', relief="raised", command=lambda: press('-'), height=2, width=5, bg='lightblue', font=('Arial', 16, 'bold'), bd=4)
subtraction.grid(row=4, column=3, padx=5, pady=5)

multiplication = Button(root, text='x', fg='black', relief="raised", command=lambda: press('*'), height=2, width=5, bg='lightblue', font=('Arial', 16, 'bold'), bd=4)
multiplication.grid(row=3, column=3, padx=5, pady=5)

remainder = Button(root, text='%', fg='black', relief="raised", command=lambda: press('%'), height=2, width=5, bg='lightblue', font=('Arial', 16, 'bold'), bd=4)
remainder.grid(row=2, column=2, padx=5, pady=5)

division = Button(root, text='/', fg='black', relief="raised", command=lambda: press('/'), height=2, width=5, bg='lightblue', font=('Arial', 16, 'bold'), bd=4)
division.grid(row=2, column=3, padx=5, pady=5)

power = Button(root, text='^', fg='black', relief="raised", command=lambda: press('**'), height=2, width=5, bg='lightblue', font=('Arial', 16, 'bold'), bd=4)
power.grid(row=6, column=0, padx=5, pady=5)

equal = Button(root, text='=', fg='black', relief="raised", command=equal_press, height=2, width=5, bg='lightcoral', font=('Arial', 16, 'bold'), bd=4)
equal.grid(row=6, column=3, padx=5, pady=5)

clear = Button(root, text='AC', fg='black', relief="raised", command=cl, height=2, width=5, bg='lightcoral', font=('Arial', 16, 'bold'), bd=4)
clear.grid(row=2, column=0, padx=5, pady=5)

remove = Button(root, text='DEL', fg='black', relief="raised", command=delete, height=2, width=5, bg='lightcoral', font=('Arial', 16, 'bold'), bd=4)
remove.grid(row=2, column=1, padx=5, pady=5)

decimal = Button(root, text='.', fg='black', relief="raised", command=lambda: press('.'), height=2, width=5, bg='lightblue', font=('Arial', 16, 'bold'), bd=4)
decimal.grid(row=6, column=2, padx=5, pady=5)

root.configure(background='pink')
root.mainloop()
