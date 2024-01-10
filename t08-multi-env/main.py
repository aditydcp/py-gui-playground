import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import subprocess

# TODO: Implement GUI

# System settings
ctk.set_appearance_mode('Light')
ctk.set_default_color_theme('blue')

# Window
window = ctk.CTk()
window.title('Mulev: Multi Env')
window.geometry('480x480')

# region - Functions

def run():
    output1 = subprocess.run('conda run -n ' + env1.get() + ' python script.py', capture_output=True, text=True, shell=True)
    output2 = subprocess.run('conda run -n ' + env2.get() + ' python script.py', capture_output=True, text=True, shell=True)

    print(output1)
    print(output2)

    ver1 = output1.stdout.split(' ')[0]
    ver2 = output2.stdout.split(' ')[0]

    result1_label.configure(text=ver1)
    result2_label.configure(text=ver2)

# endregion - Functions

# region - UI Elements

# tooltip label
ctk.CTkLabel(master=window,
             text="Insert two virtual environment names").pack(pady=16)

content_frame = ctk.CTkFrame(master=window)

env1 = tk.StringVar()
frame1 = ctk.CTkFrame(master=content_frame,
                      fg_color="transparent",
                      border_width=0)
name1_label = ctk.CTkLabel(master=frame1,
                           text="Environment Name 1")
name1_input = ctk.CTkEntry(master=frame1,
                           textvariable=env1)
python1_label = ctk.CTkLabel(master=frame1,
                             text="Python")
result1_label = ctk.CTkLabel(master=frame1,
                             text="")
name1_label.pack()
name1_input.pack(pady=8)
python1_label.pack()
result1_label.pack()

env2 = tk.StringVar()
frame2 = ctk.CTkFrame(master=content_frame,
                      fg_color="transparent",
                      border_width=0)
name2_label = ctk.CTkLabel(master=frame2,
                           text="Environment Name 2")
name2_input = ctk.CTkEntry(master=frame2,
                           textvariable=env2)
python2_label = ctk.CTkLabel(master=frame2,
                             text="Python")
result2_label = ctk.CTkLabel(master=frame2,
                             text="")
name2_label.pack()
name2_input.pack(pady=8)
python2_label.pack()
result2_label.pack()

frame1.pack(side="left", padx=(16,8), pady=16)
frame2.pack(side="left", padx=(8,16), pady=16)

content_frame.pack(padx=16)

button = ctk.CTkButton(master=window,
                       text="Go",
                       command=run)
button.pack(pady=16)

# endregion - UI Elements

window.mainloop()