from tkinter import *
win = Tk()
win.title("CALCULATOR")
equation = StringVar()

expression = ""

def input_number(number, equation):
    global expression
    expression = expression + str(number)
    equation.set(expression)

def clear_input_field(equation):
    global expression
    expression = ""
    equation.set("0")
def evaluate(equation):
   global expression
   try:
       result = str(eval(expression))
       equation.set(result)
       expression = ""
   except:
       expression = ""

def main():

    win.geometry("325x175")

input_field = Entry(win,textvariable=equation)#,textvariable=equation)
input_field.place(height=200)
input_field.grid(columnspan=6, ipadx=90, ipady=6)
equation.set("0")

_1=Button(win,text="1", fg='white', bg='black', bd=0, height=2, width=10, command=lambda: input_number(1, equation))#, command=lambda: input_number(1, equation)
_1.grid(row=2,column=0)
_2=Button(win,text="2", fg='white', bg='black', bd=0, height=2, width=10, command=lambda: input_number(2, equation))#, command=lambda: input_number(2, equation)
_2.grid(row=2, column=1)
_3=Button(win,text="3", fg='white', bg='black', bd=0, height=2, width=10, command=lambda: input_number(3, equation))#, command=lambda: input_number(3, equation)
_3.grid(row=2, column=2)
_4=Button(win,text="4", fg='white', bg='black', bd=0, height=2, width=10, command=lambda: input_number(4, equation))#, command=lambda: input_number(4, equation)
_4.grid(row=3,column=0)
_5=Button(win,text="5", fg='white', bg='black', bd=0, height=2, width=10, command=lambda: input_number(5, equation))#, command=lambda: input_number(5, equation)
_5.grid(row=3,column=1)
_6=Button(win,text="6", fg='white', bg='black', bd=0, height=2, width=10, command=lambda: input_number(6, equation))#, command=lambda: input_number(6, equation)
_6.grid(row=3,column=2)
_7=Button(win,text="7", fg='white', bg='black', bd=0, height=2, width=10, command=lambda: input_number(7, equation))#, command=lambda: input_number(7, equation)
_7.grid(row=4,column=0)
_8=Button(win,text="8", fg='white', bg='black', bd=0, height=2, width=10, command=lambda: input_number(8, equation))#, command=lambda: input_number(8, equation)
_8.grid(row=4,column=1)
_9=Button(win,text="9", fg='white', bg='black', bd=0, height=2, width=10, command=lambda: input_number(9, equation))#, command=lambda: input_number(9, equation)
_9.grid(row=4,column=2)
_0=Button(win,text="0", fg='white', bg='black', bd=0, height=2, width=10, command=lambda: input_number(0, equation))#, command=lambda: input_number(0, equation)
_0.grid(row=5,column=0)
plus=Button(win,text="+", fg='white', bg='black', bd=0, height=2, width=10, command=lambda: input_number('+', equation))#, command=lambda: input_number(+, equation)
plus.grid(row=2, column=3)
minus=Button(win,text="-", fg='white', bg='black', bd=0, height=2, width=10, command=lambda: input_number('-', equation))#, command=lambda: input_number(-, equation)
minus.grid(row=3, column=3)
multiply=Button(win,text="*", fg='white', bg='black', bd=0, height=2, width=10, command=lambda: input_number('*', equation))#, command=lambda: input_number(*, equation)
multiply.grid(row=4, column=3)
divide=Button(win,text="/", fg='white', bg='black', bd=0, height=2, width=10, command=lambda: input_number('/', equation))#, command=lambda: input_number(/, equation)
divide.grid(row=5, column=3)
equal=Button(win,text="=", fg='white', bg='black', bd=0, height=2, width=10, command=lambda: evaluate(equation))#, command=lambda: evaluate(equation)
equal.grid(row=5, column=2)
clear=Button(win,text="clear", fg='white', bg='black', bd=0, height=2, width=10, command=lambda: clear_input_field(equation))#, command=lambda: clear_input_field(equation)
clear.grid(row=5, column=1)

win.mainloop()
if __name__ == '_main_':
      main()
