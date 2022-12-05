from tkinter import *

root = Tk()
root.title("simple calculator")
input = Entry(root, width=50, borderwidth=7.5)
input.grid(row=0, column=0, columnspan=6, padx=10, pady=10)


# entry function
def Click_Me(number):
    s = input.get()
    input.delete(0, END)
    input.insert(0,  str(s) + str(number))


# arithmetic and other functions
def button_clear():
    input.delete(0, END)

def Button_multiply():
    current = input.get()
    global mul_num
    global math
    math ="multiplication"
    mul_num = int(current)
    input.delete(0, END)

def button_add():
    current = input.get()
    global add_num
    global math
    math = "addition"
    add_num = int(current)
    input.delete(0, END)
def button_subtract():
    current = input.get()
    global sub_num
    global math
    math = "subtraction"
    sub_num = int(current)
    input.delete(0, END)
def button_division():
    current = input.get()
    global div_num
    global math
    math = "division"
    div_num = int(current)
    input.delete(0, END)

def Button_equal():
    equal = input.get()
    input.delete(0, END)
    if math == "multiplication":
        input.insert(0, mul_num * int(equal))
    elif math == "addition":
        input.insert(0, add_num + int(equal))
    elif math == "subtraction":
        input.insert(0, sub_num - int(equal))
    elif math == "division":
        input.insert(0, div_num / int(equal))


# the button command
button_1 = Button(root, text="7", padx=30, pady=20, borderwidth=4, command=lambda: Click_Me(7))
button_2 = Button(root, text="8", padx=30, pady=20, borderwidth=4, command=lambda: Click_Me(8))
button_3 = Button(root, text="9", padx=30, pady=20, borderwidth=4, command=lambda: Click_Me(9))
Button_multiply = Button(root, text="X", padx=30, pady=20, borderwidth=4, command=Button_multiply)
button_4 = Button(root, text="4", padx=30, pady=20, borderwidth=4, command=lambda: Click_Me(4))
button_5 = Button(root, text="5", padx=30, pady=20, borderwidth=4, command=lambda: Click_Me(5))
button_6 = Button(root, text="6", padx=30, pady=20, borderwidth=4, command=lambda: Click_Me(6))
button_division = Button(root, text="/", padx=30, pady=20, borderwidth=4, command=button_division)
button_7 = Button(root, text="1", padx=30, pady=20, borderwidth=4, command=lambda: Click_Me(1))
button_8 = Button(root, text="2", padx=30, pady=20, borderwidth=4, command=lambda: Click_Me(2))
button_9 = Button(root, text="3", padx=30, pady=20, borderwidth=4, command=lambda: Click_Me(3))
button_0 = Button(root, text="0", padx=30, pady=20, borderwidth=4, command=lambda: Click_Me(0))
button_add = Button(root, text="+", padx=30, pady=20, borderwidth=4, command=button_add)
button_clear = Button(root, text="Clear", padx=20, pady=20, borderwidth=4, command=button_clear)
Button_equal = Button(root, text="=", padx=30, pady=20, borderwidth=4, command=Button_equal)
button_subtract = Button(root, text="-", padx=30, pady=20, borderwidth=4, command=button_subtract)



# the grid styles for the buttons
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
Button_multiply.grid(row=1, column=3)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_division.grid(row=2, column=3)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=3, column=3)
button_clear.grid(row=4, column=1)
Button_equal.grid(row=4, column=2)
button_subtract.grid(row=4, column=3)

#setting the size and width of the window 
root.geometry("328x326")
root.minsize(328, 326)
root.maxsize(328, 326)
root.mainloop()

