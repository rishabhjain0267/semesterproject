from tkinter import *
from math import *


#Creating an interface
window = Tk()
window.title("Scientific Calculator")
window.configure(background="red")
# creating labels
myLabel1= Label(window,text="*Press equal to after every operation*",font=("Times",20),fg="black",bg="red")
myLabel1.grid(row=8,columnspan=2,column=1)
myLabel2= Label(window,text="*In one operation, you can only operate two numbers* ",font=("Times",20),fg="black",bg="red")
myLabel2.grid(row=9,columnspan=2,column=1)
myLabel3= Label(window,text="SCIENTIFIC CALCULATOR ", font=("Times",20),fg="Black",bg="red")
myLabel3.grid(row=0,column=0,columnspan=4)
#Creating an box which shows the numbers and answers
calculator_box = Entry(window, width=60, borderwidth=5,fg="black",bg="light green",font=("Times",20))
calculator_box.grid(row=1, column=0, columnspan=4, padx=10, pady=10)


#Creating functions

def button_click(number):

    current = calculator_box.get()
    calculator_box.delete(0, END)
    calculator_box.insert(0, str(current) + str(number))

# Operation functions
def button_clear():
    calculator_box.delete(0, END)




# function for performing operation when equal is pressed
def button_equal():
    second_number = calculator_box.get()
    calculator_box.delete(0, END)

    if operation == "addition":
        calculator_box.insert(0, f_num + float(second_number))

    if operation == "subtraction":
        calculator_box.insert(0, f_num - float(second_number))

    if operation == "multiplication":
        calculator_box.insert(0, f_num * float(second_number))

    if operation == "division":
        calculator_box.insert(0, f_num / float(second_number))

    if operation == "sine":
        calculator_box.insert(0, sin(f_num))

    if operation == "cosine":
        calculator_box.insert(0, cos(f_num))

    if operation == "tangent":
        calculator_box.insert(0, tan(f_num))

    if operation == "exponent":
        calculator_box.insert(0, (f_num)**float(second_number))

    if operation == "squareroot":
        calculator_box.insert(0, sqrt(f_num))
# operators
def button_add():
    first_number = calculator_box.get()
    global f_num
    global operation
    operation = "addition"
    f_num = float(first_number)
    calculator_box.delete(0, END)

def button_subtract():
    first_number = calculator_box.get()
    global f_num
    global operation
    operation = "subtraction"
    f_num = float(first_number)
    calculator_box.delete(0, END)


def button_multiply():
    first_number = calculator_box.get()
    global f_num
    global operation
    operation = "multiplication"
    f_num = float(first_number)
    calculator_box.delete(0, END)


def button_divide():
    first_number = calculator_box.get()
    global f_num
    global operation
    operation = "division"
    f_num = float(first_number)
    calculator_box.delete(0, END)

def button_sin():
    first_number = calculator_box.get()
    global f_num
    global operation
    operation = "sine"
    f_num = float(first_number)
    calculator_box.delete(0, END)

def button_cos():
    first_number = calculator_box.get()
    global f_num
    global operation
    operation = "cosine"
    f_num = float(first_number)
    calculator_box.delete(0, END)

def button_tan():
    first_number = calculator_box.get()
    global f_num
    global operation
    operation = "tangent"
    f_num = float(first_number)
    calculator_box.delete(0, END)

def button_exponent():
    first_number = calculator_box.get()
    global f_num
    global operation
    operation = "exponent"
    f_num = float(first_number)
    calculator_box.delete(0, END)

def button_sqrt():
    first_number = calculator_box.get()
    global f_num
    global operation
    operation = "squareroot"
    f_num = float(first_number)
    calculator_box.delete(0, END)
# Creating buttons

number_1 = Button(window, text="1", padx=100, pady=25, fg="white",bg="black",font=("Times",20), command=lambda: button_click(1))
number_2 = Button(window, text="2", padx=100, pady=25,fg="white",bg="black",font=("Times",20), command=lambda: button_click(2))
number_3 = Button(window, text="3", padx=100, pady=25,fg="white",bg="black",font=("Times",20), command=lambda: button_click(3))
number_4 = Button(window, text="4", padx=100, pady=25,fg="white",bg="black",font=("Times",20), command=lambda: button_click(4))
number_5 = Button(window, text="5", padx=100, pady=25,fg="white",bg="black",font=("Times",20), command=lambda: button_click(5))
number_6 = Button(window, text="6", padx=100, pady=25,fg="white",bg="black",font=("Times",20), command=lambda: button_click(6))
number_7 = Button(window, text="7", padx=100, pady=25, fg="white",bg="black",font=("Times",20),command=lambda: button_click(7))
number_8 = Button(window, text="8", padx=100, pady=25,fg="white",bg="black",font=("Times",20), command=lambda: button_click(8))
number_9 = Button(window, text="9", padx=100, pady=25,fg="white",bg="black",font=("Times",20), command=lambda: button_click(9))
number_0 = Button(window, text="0", padx=100, pady=25, fg="white",bg="black",font=("Times",20),command=lambda: button_click(0))
decimal_dot = Button(window, text=".", padx=100, pady=25,fg="white",bg="black",font=("Times",20), command=lambda :button_click("."))
operator_add = Button(window, text="+", padx=100, pady=25,fg="orange",bg="black",font=("Times",20), command=button_add)
finish_equal = Button(window, text="=", padx=218, pady=25, fg="pink",bg="black",font=("Times",20),command=button_equal)
finish_clear = Button(window, text="Clear", padx=200, pady=25,fg="pink",bg="black",font=("Times",20), command=button_clear)
operator_exponent = Button(window, text="x**y", padx=100, pady=25,fg="orange",bg="black",font=("Times",20), command=button_exponent)
operator_subtract = Button(window, text="-", padx=100, pady=25,fg="orange",bg="black",font=("Times",20), command=button_subtract)
operator_multiply = Button(window, text="*", padx=100, pady=25,fg="orange",bg="black",font=("Times",20), command=button_multiply)
operator_divide = Button(window, text="/", padx=100, pady=25,fg="orange",bg="black",font=("Times",20), command=button_divide)
operator_sin = Button(window, text="sin", padx=100, pady=25,fg="orange",bg="black",font=("Times",20), command=button_sin)
operator_cos = Button(window, text="cos", padx=100, pady=25,fg="orange",bg="black",font=("Times",20), command=button_cos)
operator_tan = Button(window, text="tan", padx=100, pady=25,fg="orange",bg="black",font=("Times",20), command=button_tan)
operator_sqrt = Button(window, text="x**1/2", padx=100, pady=25,fg="orange", bg="black",font=("Times",20), command=button_sqrt)

# Positioning the buttons on the interface

number_1.grid(row=4, column=0)
number_2.grid(row=4, column=1)
number_3.grid(row=4, column=2)

number_4.grid(row=3, column=0)
number_5.grid(row=3, column=1)
number_6.grid(row=3, column=2)

number_7.grid(row=2, column=0)
number_8.grid(row=2, column=1)
number_9.grid(row=2, column=2)

number_0.grid(row=5, column=0)
decimal_dot.grid(row=5, column=3)
operator_add.grid(row=6, column=0)
operator_subtract.grid(row=7, column=0)
operator_multiply.grid(row=7, column=1)
operator_divide.grid(row=7, column=2)
finish_equal.grid(row=6, column=1, columnspan=2)
finish_clear.grid(row=5, column=1, columnspan=2)
operator_sin.grid(row=2, column=3)
operator_cos.grid(row=3, column=3)
operator_tan.grid(row=4, column=3)
operator_exponent.grid(row=6, column=3)
operator_sqrt.grid(row=7, column=3)
# keeping interface open
window.mainloop()






