# ``
#   If you want to use the default ttk styling,
#   uncomment lines 8, 18 and 21
#   and don't use lines 9 & 19
# ``

import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# logical function for the value conversion
def convert():
    miles = entry_int.get()
    kilometers = miles * 1.61
    output_string.set(kilometers)

# window
# window = tk.Tk()
window = ttk.Window(themename='journal', size=(300, 150))
window.title('Demo')
# window.geometry('300x150')

# title label
title_label = ttk.Label(master=window,
                        text='Miles to Kilometers',
                        font='Calibri 24 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame,
                  textvariable=entry_int)
button = ttk.Button(master=input_frame,
                    text='Convert',
                    command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# output label
output_string = tk.StringVar()
output_label = ttk.Label(master=window,
                        text='Output',
                        textvariable=output_string,
                        font='Calibri 24')
output_label.pack(pady=5)

# run
window.mainloop()