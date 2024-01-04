import tkinter as tk
import tkinter.font as tkFont

signs = ['+', '-', 'x', '/']

def add(symbol):
    equation = main_text.get()
    if (equation == '0' or equation == '') \
        and symbol not in signs:
        main_text.set(symbol)
        return

    if equation[-1] in signs and symbol in signs:
        print('sign overload')
        main_text.set(equation[:-1] + symbol)
        return

    main_text.set(equation + symbol)

def calculate():
    equation = main_text.get()

    # convert multiplication symbol to python multiplication symbol
    new_equation = equation.split('x')
    new_equation = '*'.join(new_equation)

    result = eval(new_equation)
    
    # round if zero floating point
    if isinstance(result, float) and result % 1 == 0.0:
        result = int(result)
        
    history_text.set(equation)
    main_text.set(result)

def clear():
    history_text.set('')
    main_text.set('0')

# main window
window = tk.Tk()
window.title('Simple Calculator')
window.geometry('384x600')

# content container
container = tk.Frame(master=window)
container.grid_rowconfigure([2,3,4,5,6], weight=1)
container.grid_columnconfigure([0,1,2,3], weight=1)
container.pack(fill='both', padx=16, pady=16)

title_font = tkFont.Font(family="Calibri", size=8)
main_font = tkFont.Font(family="Calibri", size=24)
history_font = tkFont.Font(family="Calibri", size=12)
button_font = tkFont.Font(family="Calibri", size=14)

# title label
title_label = tk.Label(master=container,
                        text='Simple Calculator',
                        font=title_font,
                        foreground='grey')
title_label.grid(column=0, 
                 columnspan=4,
                 row=0)

# navigation panel
nav_frame = tk.Frame(master=container)
history_text = tk.StringVar()
main_text = tk.StringVar(value='0')
history_label = tk.Label(master=nav_frame,
                         text='History Panel',
                         textvariable=history_text,
                         font=history_font,
                         foreground='grey')
main_label = tk.Label(master=nav_frame,
                      text='Main Panel',
                      textvariable=main_text,
                      font=main_font,
                      foreground='blue')
history_label.pack(fill='both')
main_label.pack(fill='both')
nav_frame.grid(column=0,
               columnspan=4,
               row=1,
               padx=16,
               pady=16)

blank_image = tk.PhotoImage()

# buttons
num_1_button = tk.Button(master=container,
                         image=blank_image,
                         text='1',
                         font=button_font,
                         width=80,
                         height=80,
                         command=lambda: add('1'),
                         compound=tk.CENTER)
num_2_button = tk.Button(master=container,
                         image=blank_image,
                         text='2',
                         font=button_font,
                         width=80,
                         height=80,
                         command=lambda: add('2'),
                         compound=tk.CENTER)
num_3_button = tk.Button(master=container,
                         image=blank_image,
                         text='3',
                         font=button_font,
                         width=80,
                         height=80,
                         command=lambda: add('3'),
                         compound=tk.CENTER)
num_4_button = tk.Button(master=container,
                         image=blank_image,
                         text='4',
                         font=button_font,
                         width=80,
                         height=80,
                         command=lambda: add('4'),
                         compound=tk.CENTER)
num_5_button = tk.Button(master=container,
                         image=blank_image,
                         text='5',
                         font=button_font,
                         width=80,
                         height=80,
                         command=lambda: add('5'),
                         compound=tk.CENTER)
num_6_button = tk.Button(master=container,
                         image=blank_image,
                         text='6',
                         font=button_font,
                         width=80,
                         height=80,
                         command=lambda: add('6'),
                         compound=tk.CENTER)
num_7_button = tk.Button(master=container,
                         image=blank_image,
                         text='7',
                         font=button_font,
                         width=80,
                         height=80,
                         command=lambda: add('7'),
                         compound=tk.CENTER)
num_8_button = tk.Button(master=container,
                         image=blank_image,
                         text='8',
                         font=button_font,
                         width=80,
                         height=80,
                         command=lambda: add('8'),
                         compound=tk.CENTER)
num_9_button = tk.Button(master=container,
                         image=blank_image,
                         text='9',
                         font=button_font,
                         width=80,
                         height=80,
                         command=lambda: add('9'),
                         compound=tk.CENTER)
num_0_button = tk.Button(master=container,
                         image=blank_image,
                         text='0',
                         font=button_font,
                         width=80,
                         height=80,
                         command=lambda: add('0'),
                         compound=tk.CENTER)

sign_pn_button = tk.Button(master=container,
                           image=blank_image,
                           text='+/-',
                           font=button_font,
                           width=80,
                           height=80,
                           command=lambda: add('+/-'),
                           compound=tk.CENTER)
sign_point_button = tk.Button(master=container,
                              image=blank_image,
                              text='.',
                              font=button_font,
                              width=80,
                              height=80,
                              command=lambda: add('.'),
                              compound=tk.CENTER)
sign_divide_button = tk.Button(master=container,
                               image=blank_image,
                               text='-',
                               font=button_font,
                               width=80,
                               height=80,
                               command=lambda: add('/'),
                               compound=tk.CENTER)
sign_multiply_button = tk.Button(master=container,
                                 image=blank_image,
                                 text='x',
                                 font=button_font,
                                 width=80,
                                 height=80,
                                 command=lambda: add('x'),
                                 compound=tk.CENTER)
sign_minus_button = tk.Button(master=container,
                              image=blank_image,
                              text='-',
                              font=button_font,
                              width=80,
                              height=80,
                              command=lambda: add('-'),
                              compound=tk.CENTER)
sign_plus_button = tk.Button(master=container,
                             image=blank_image,
                             text='+',
                             font=button_font,
                             width=80,
                             height=80,
                             command=lambda: add('+'),
                             compound=tk.CENTER)
sign_equal_button = tk.Button(master=container,
                              image=blank_image,
                              text='=',
                              font=button_font,
                              width=80,
                              height=80,
                              command= calculate,
                              compound=tk.CENTER)
bracket_open_button = tk.Button(master=container,
                                image=blank_image,
                                text='(',
                                font=button_font,
                                width=80,
                                height=80,
                                command=lambda: add('('),
                                compound=tk.CENTER)
bracket_close_button = tk.Button(master=container,
                                 image=blank_image,
                                 text=')',
                                 font=button_font,
                                 width=80,
                                 height=80,
                                 command=lambda: add(')'),
                                 compound=tk.CENTER)
clear_button = tk.Button(master=container,
                         image=blank_image,
                         text='C',
                         font=button_font,
                         width=80,
                         height=80,
                         command=clear,
                         compound=tk.CENTER)

bracket_open_button.grid(row=2, column=0, sticky='NSWE')
bracket_close_button.grid(row=2, column=1, sticky='NSWE')
clear_button.grid(row=2, column=2, sticky='NSWE')
sign_divide_button.grid(row=2, column=3, sticky='NSWE')
num_7_button.grid(row=3, column=0, sticky='NSWE')
num_8_button.grid(row=3, column=1, sticky='NSWE')
num_9_button.grid(row=3, column=2, sticky='NSWE')
sign_multiply_button.grid(row=3, column=3, sticky='NSWE')
num_4_button.grid(row=4, column=0, sticky='NSWE')
num_5_button.grid(row=4, column=1, sticky='NSWE')
num_6_button.grid(row=4, column=2, sticky='NSWE')
sign_minus_button.grid(row=4, column=3, sticky='NSWE')
num_1_button.grid(row=5, column=0, sticky='NSWE')
num_2_button.grid(row=5, column=1, sticky='NSWE')
num_3_button.grid(row=5, column=2, sticky='NSWE')
sign_plus_button.grid(row=5, column=3, sticky='NSWE')
sign_pn_button.grid(row=6, column=0, sticky='NSWE')
num_0_button.grid(row=6, column=1, sticky='NSWE')
sign_point_button.grid(row=6, column=2, sticky='NSWE')
sign_equal_button.grid(row=6, column=3, sticky='NSWE')

# run
window.mainloop()
