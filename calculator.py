from tkinter import *
exp=""
def press(num):
    global exp
    exp=exp+str(num)
    equation.set(exp)
def equal_press():
    try:
        global exp
        total=str(eval(exp))
        equation.set(total)
        exp=""
    except:
        equation.set("error")
        exp=""
def cl():
    global exp
    exp=""
    equation.set("")
def delete():
    global exp
    exp=exp[:-1]
    equation.set(exp)


root=Tk()
root.title("CALCULATOR")
root.geometry('400x400')#size
root.config(borderwidth=5, relief="solid")
equation=StringVar()#output screen
txt = Entry(root, font=('Arial', 24), bd=5, relief="solid", justify="right",textvariable=equation)
txt.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
#txt=Entry(root,textvariable=equation)#for taking input bg="lightblue"
#txt.grid(columnspan=4,row=1,ipadx=30)#size of button

button1=Button(root,text='1',fg='black',relief="solid",command=lambda:press(1),height=3,width=5)
button1.grid(row=5,column=0)
button2=Button(root,text='2',fg='black',relief="solid",command=lambda:press(2),height=3,width=5)
button2.grid(row=5,column=1)
button3=Button(root,text='3',fg='black',relief="solid",command=lambda:press(3),height=3,width=5)
button3.grid(row=5,column=2)
button4=Button(root,text='4',fg='black',relief="solid",command=lambda:press(4),height=3,width=5)
button4.grid(row=4,column=0)
button5=Button(root,text='5',fg='black',relief="solid",command=lambda:press(5),height=3,width=5)
button5.grid(row=4,column=1)
button6=Button(root,text='6',fg='black',relief="solid",command=lambda:press(6),height=3,width=5)
button6.grid(row=4,column=2)
button7=Button(root,text='7',fg='black',relief="solid",command=lambda:press(7),height=3,width=5)
button7.grid(row=3,column=0)
button8=Button(root,text='8',fg='black',relief="solid",command=lambda:press(8),height=3,width=5)
button8.grid(row=3,column=1)
button9=Button(root,text='9',fg='black',relief="solid",command=lambda:press(9),height=3,width=5)
button9.grid(row=3,column=2)
button0=Button(root,text='0',fg='black',relief="solid",command=lambda:press(0),height=3,width=5)
button0.grid(row=6,column=1)
addition=Button(root,text='+',fg='black',relief="solid",command=lambda:press('+'),height=3,width=5)
addition.grid(row=5,column=3)
subtraction=Button(root,text='-',fg='black',relief="solid",command=lambda:press('-'),height=3,width=5)
subtraction.grid(row=4,column=3)
multiplication=Button(root,text='x',fg='black',relief="solid",command=lambda:press('*'),height=3,width=5)
multiplication.grid(row=3,column=3)
remainder=Button(root,text='%',fg='black',relief="solid",command=lambda:press('%'),height=3,width=5)
remainder.grid(row=2,column=2)
division=Button(root,text='/',fg='black',relief="solid",command=lambda:press('/'),height=3,width=5)
division.grid(row=2,column=3)
power=Button(root,text='^',fg='black',relief="solid",command=lambda:press('**'),height=3,width=5)
power.grid(row=6,column=0)
equal=Button(root,text='=',fg='black',relief="solid",command=equal_press,height=3,width=5)
equal.grid(row=6,column=3)
clear=Button(root,text='AC',fg='black',relief="solid",command=cl,height=3,width=5)
clear.grid(row=2,column=0)
remove=Button(root,text='DEL',fg='black',relief="solid",command=delete,height=3,width=5)
remove.grid(row=2,column=1)
decimal=Button(root,text='.',fg='black',relief="solid",command=lambda:press('.'),height=3,width=5)
decimal.grid(row=6,column=2)
root.configure(background='pink')
root.mainloop()