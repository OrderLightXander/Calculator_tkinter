from tkinter import *


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def bntEqualsInput():
    try:
        global operator
        sumup=str(eval(operator))
        text_Input.set(sumup)
        operator=""
    except SyntaxError:
        text_Input.set("VALUE ERROR")
    except ZeroDivisionError:
        text_Input.set("∞, But you can't divide by 0")



cal = Tk()
cal.title("Calculator")
operator = ""
text_Input = StringVar()

txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable = text_Input, bd=30, insertwidth=4, bg='White', justify='right').grid(columnspan=4)

bnt0=Button(cal,padx=16,bd=8,fg='black', bg='White', font=('arial', 20, 'bold'),command=lambda:btnClick(0), text='0',height = 1, width = 2).grid(row=4,column=1)
bnt9=Button(cal,padx=16,bd=8,fg='black', bg='White', font=('arial', 20, 'bold'),command=lambda:btnClick(9), text='9',height = 1, width = 2).grid(row=3,column=2)
bnt8=Button(cal,padx=16,bd=8,fg='black', bg='White', font=('arial', 20, 'bold'),command=lambda:btnClick(8), text='8',height = 1, width = 2).grid(row=3,column=1)
bnt7=Button(cal,padx=16,bd=8,fg='black', bg='White', font=('arial', 20, 'bold'),command=lambda:btnClick(7), text='7',height = 1, width = 2).grid(row=3,column=0)
bnt6=Button(cal,padx=16,bd=8,fg='black', bg='White', font=('arial', 20, 'bold'),command=lambda:btnClick(6), text='6',height = 1, width = 2).grid(row=2,column=2)
bnt5=Button(cal,padx=16,bd=8,fg='black', bg='White', font=('arial', 20, 'bold'),command=lambda:btnClick(5), text='5',height = 1, width = 2).grid(row=2,column=1)
bnt4=Button(cal,padx=16,bd=8,fg='black', bg='White', font=('arial', 20, 'bold'),command=lambda:btnClick(4), text='4',height = 1, width = 2).grid(row=2,column=0)
bnt3=Button(cal,padx=16,bd=8,fg='black', bg='White', font=('arial', 20, 'bold'),command=lambda:btnClick(3), text='3',height = 1, width = 2).grid(row=1,column=2)
bnt2=Button(cal,padx=16,bd=8,fg='black', bg='White', font=('arial', 20, 'bold'),command=lambda:btnClick(2), text='2',height = 1, width = 2).grid(row=1,column=1)
bnt1=Button(cal,padx=16,bd=8,fg='black', bg='White', font=('arial', 20, 'bold'),command=lambda:btnClick(1), text='1',height = 1, width = 2).grid(row=1,column=0)
add=Button(cal,padx=16,bd=8,fg='black',bg='White',font=('arial', 20, 'bold'),command=lambda:btnClick("+"), text='+',height = 1, width = 2).grid(row=4,column=0)
substraction=Button(cal,padx=16,bd=8,fg='black',bg='White',font=('arial', 20, 'bold'),command=lambda:btnClick("-"), text='-',height = 1, width = 2).grid(row=4,column=2)
multiply=Button(cal,padx=16,bd=8,fg='black',bg='White',font=('arial', 20, 'bold'),command=lambda:btnClick("*"), text='x',height = 1, width = 2).grid(row=5,column=0)
division=Button(cal,padx=16,bd=8,fg='black',bg='White',font=('arial', 20, 'bold'),command=lambda:btnClick("/"), text='/',height = 1, width = 2).grid(row=5,column=2)
equals=Button(cal,padx=16,bd=8,fg='black',bg='White',font=('arial', 20, 'bold'),command=lambda:bntEqualsInput(), text='=',height = 1, width = 2).grid(row=5,column=1)
clear=Button(cal,padx=16,bd=8,fg='black',bg='White',font=('arial', 20, 'bold'),command=lambda:btnClearDisplay(), text='C',height = 1, width = 2).grid(row=6,column=1)
point=Button(cal,padx=16,bd=8,fg='black',bg='White',font=('arial', 20, 'bold'),command=lambda:btnClick("."), text='.',height = 1, width = 2).grid(row=6,column=0)
Exit=Button(cal,padx=16,bd=8,fg='black',bg='White',font=('arial', 20, 'bold'),command=lambda:sys.exit(), text='Exit',height = 1, width = 2).grid(row=6,column=2)
cal.mainloop()