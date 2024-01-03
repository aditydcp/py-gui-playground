from tkinter import *

# Create a window
app = Tk()
app.title('Main Window')
app.geometry('700x350')

from actions import *

# Window
label_1 = Label(app, textvariable=main_text, font=('bold', 14), pady=20, padx=20)
label_1.grid(row=0, column=0, columnspan=5)
label_1.pack

# Buttons
num_button_1 = Button(app,
                      text='1', 
                      width=8,
                      height=3,
                      command=add_1)
num_button_1.grid(row=4, column=1)
num_button_2 = Button(app,
                      text='2', 
                      width=8,
                      height=3,
                      command=add_2)
num_button_2.grid(row=4, column=2)
num_button_3 = Button(app,
                      text='3', 
                      width=8,
                      height=3,
                      command=add_3)
num_button_3.grid(row=4, column=3)
num_button_4 = Button(app,
                      text='4', 
                      width=8,
                      height=3,
                      command=add_4)
num_button_4.grid(row=3, column=1)
num_button_5 = Button(app,
                      text='5', 
                      width=8,
                      height=3,
                      command=add_5)
num_button_5.grid(row=3, column=2)
num_button_6 = Button(app,
                      text='6', 
                      width=8,
                      height=3,
                      command=add_6)
num_button_6.grid(row=3, column=3)
num_button_7 = Button(app,
                      text='7', 
                      width=8,
                      height=3,
                      command=add_7)
num_button_7.grid(row=2, column=1)
num_button_8 = Button(app,
                      text='8', 
                      width=8,
                      height=3,
                      command=add_8)
num_button_8.grid(row=2, column=2)
num_button_9 = Button(app,
                      text='9', 
                      width=8,
                      height=3,
                      command=add_9)
num_button_9.grid(row=2, column=3)
num_button_0 = Button(app,
                      text='0', 
                      width=8,
                      height=3,
                      command=add_0)
num_button_0.grid(row=5, column=2)
num_button_point = Button(app,
                      text='.', 
                      width=8,
                      height=3,
                      command=add_point)
num_button_point.grid(row=5, column=3)
num_button_pn = Button(app,
                      text='+/-', 
                      width=8,
                      height=3,
                      command=toggle_pn)
num_button_pn.grid(row=5, column=1)

sign_button_equal = Button(app,
                      text='=', 
                      width=8,
                      height=3,
                      command=calculate)
sign_button_equal.grid(row=5, column=4)
sign_button_plus = Button(app,
                      text='+', 
                      width=8,
                      height=3,
                      command=add_plus)
sign_button_plus.grid(row=4, column=4)
sign_button_minus = Button(app,
                      text='-', 
                      width=8,
                      height=3,
                      command=add_minus)
sign_button_minus.grid(row=3, column=4)
sign_button_multiply = Button(app,
                      text='X', 
                      width=8,
                      height=3,
                      command=add_multiply)
sign_button_multiply.grid(row=2, column=4)
sign_button_divide = Button(app,
                      text='/', 
                      width=8,
                      height=3,
                      command=add_divide)
sign_button_divide.grid(row=1, column=4)


# Start the program
app.mainloop()