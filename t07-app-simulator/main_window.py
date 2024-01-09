import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from customtkinter import filedialog as fd
import subprocess
import time

# System settings
ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

# Window
window = ctk.CTk()
window.title('BAISim')
window.geometry('480x600')

# Font definitions
submit_font = ctk.CTkFont(size=16, weight="bold")
more_font = ctk.CTkFont(weight="bold")

# region - Functions

def set_visual_state(state):
    if state == "disabled":
        file_input.configure(state="disabled")
        method_input.configure(state="disabled")
        name_input.configure(state="disabled")
        open_loc_opt.configure(state="disabled")
        notify_opt.configure(state="disabled")
        submit_button.configure(state="disabled")
        link_label.configure(state="disabled")
    else:
        file_input.configure(state="normal")
        method_input.configure(state="normal")
        name_input.configure(state="normal")
        open_loc_opt.configure(state="normal")
        notify_opt.configure(state="normal")
        submit_button.configure(state="normal")
        link_label.configure(state="normal")

def browse_files():
    global file_path
    filename = fd.askopenfilename(initialdir = "/",
                                  title = "Select a File",
                                  filetypes = (("Text files","*.txt*"),
                                               ("Images",["*.jpg*", "*.jpeg*", "*.png*"]),
                                               ("Vector images","*.svg*"),
                                               ("PDF document", "*.pdf*"),
                                               ("All files","*.*")))
    if filename:
        file_path.set(filename)

def select_target():
    dir = fd.askdirectory(initialdir = target_path,
                          title = "Select Output Directory")
    if dir:
        print(dir)
        target_path.set(dir + "/" + target_name.get() + ".txt")

def on_filename_change(*args):
    path = target_path.get()
    dir = "/".join(path.split("/")[:-1])
    target_path.set(dir + "/" + target_name.get() + ".txt")

def process():
    if file_path.get() == "":
        messagebox.showerror(title="BAISim Error",
                             message="Please provide a file as the input.")
        return
    
    try:
        set_visual_state("disabled")

        # Simulate working progress
        ticks = [20, 40, 60, 80, 100]
        for tick in ticks:
            time.sleep(1)
            progress_label.configure(text=str(tick) + "% Processing...")
            progress_label.update()
            progress_bar.set(float(tick) / 100)
            progress_bar.update()
        if progress_bar.get() < 1.0:
            progress_bar.set(1)

        # Output
        with open(target_path.get(), 'w+') as f:
            f.write("New text file")

        # Visual indicator on done
        progress_label.configure(text="100% Complete")
        
        # Post-work actions
        set_visual_state("normal")
        if open_loc_var.get():
            open_target()
        if notify_var.get():
            messagebox.showinfo(title="BAISim",
                                message="Process has succesfully finished.")
    except Exception as err:
        print(err)
        progress_label.configure(text="Process failed!")
        messagebox.showerror(title="BAISim Error",
                             message="An error occured!")
        set_visual_state("normal")

def open_target():
    path = target_path.get()
    dir = "\\".join(path.split("/")[:-1])
    subprocess.Popen('explorer "' + dir + '"')

# endregion - Functions

# region - UI Elements

master_container = ctk.CTkFrame(master=window,
                                fg_color='transparent',
                                border_width=0)

# File input
file_input_label = ctk.CTkLabel(master=master_container,
                                text='Select a file')
file_input_frame = ctk.CTkFrame(master=master_container,
                                fg_color='transparent',
                                border_width=0)
file_input_frame.columnconfigure(0, weight=9)
file_input_frame.columnconfigure(1, weight=1)
file_path = tk.StringVar()
file_input = ctk.CTkEntry(master=file_input_frame,
                          textvariable=file_path)
file_more_button = ctk.CTkButton(master=file_input_frame,
                            text="...",
                            font=more_font,
                            width=32,
                            command=browse_files)

file_input.grid(row=0, column=0, sticky="ew")
file_more_button.grid(row=0, column=1, sticky="ew", padx=(8,0))
file_input_label.pack(anchor="nw")
file_input_frame.pack(fill="x")

# Method dropdown
method_input_label = ctk.CTkLabel(master=master_container,
                                  text="Choose algorithm")
options = ["Algorithm 1", "Algorithm 2", "Algorithm 3"]
algorithm = tk.StringVar()
algorithm.set(options[0])
method_input = ctk.CTkOptionMenu(master=master_container,
                                 variable=algorithm,
                                 values=options)

method_input_label.pack(anchor="nw", pady=(8,0))
method_input.pack(fill="x")

master_container.pack(padx=16, pady=16, expand=True, fill="both")

# Target input
name_input_label = ctk.CTkLabel(master=master_container,
                                text='Output filename')
target_name = tk.StringVar()
target_name.trace_add("write", on_filename_change)
name_input = ctk.CTkEntry(master=master_container,
                          textvariable=target_name)

name_input_label.pack(anchor="nw", pady=(8,0))
name_input.pack(fill="x")

dir_input_label = ctk.CTkLabel(master=master_container,
                               text='Output will be saved as')
target_path = tk.StringVar()
target_path.set("C:/Users/123/Downloads/output.txt")
dir_input = ctk.CTkEntry(master=master_container,
                            state="disabled",
                            fg_color="lightgray",
                            border_width=1,
                            textvariable=target_path)
dir_select_button = ctk.CTkButton(master=master_container,
                                  text="Change directory",
                                  command=select_target)

dir_input_label.pack(anchor="nw", pady=(8,0))
dir_input.pack(fill="x")
dir_select_button.pack(anchor="nw", pady=(8,0))

# Misc options
open_loc_var = ctk.IntVar()
open_loc_opt = ctk.CTkCheckBox(master=master_container,
                               text="Open target location on finish",
                               checkbox_height=22,
                               checkbox_width=22,
                               variable=open_loc_var)
open_loc_opt.pack(anchor="nw", pady=8)
notify_var = ctk.IntVar()
notify_opt = ctk.CTkCheckBox(master=master_container,
                             text="Notify me on finish",
                             checkbox_height=22,
                             checkbox_width=22,
                             variable=notify_var)
notify_opt.pack(anchor="nw")

# Progress bar
progress_frame = ctk.CTkFrame(master=master_container,
                              fg_color="transparent",
                              border_width=0)
progress_label = ctk.CTkLabel(master=progress_frame,
                              text="Awaiting order")
progress_label.pack()
progress_bar = ctk.CTkProgressBar(master=progress_frame)
progress_bar.set(0)
progress_bar.pack(fill="x")
progress_frame.pack(fill="x", pady=24)

# Primary button
submit_button = ctk.CTkButton(master=master_container,
                              text="PROCESS",
                              font=submit_font,
                              height=32,
                              command=process)
submit_button.pack(fill="x", pady=8)

# Link to output location
link_label = ctk.CTkButton(master=master_container,
                          text="Open output file location",
                          state="disabled",
                          command=open_target)
link_label.pack()

# endregion - UI Elements

window.mainloop()