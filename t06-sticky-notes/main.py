import tkinter as tk
import customtkinter as ctk
import file_manager as fm
from customtkinter import filedialog

# Functions
read_mode = True
def toggle_read_mode(target=None):
    global read_mode
    if target is not None:
        read_mode = target
    else:
        read_mode = not read_mode
    
    if not read_mode:
        widget_state = tk.NORMAL
        primary_button_text = "Save"
        secondary_button_text = "Cancel"
        mode_text = "Editing Mode"
        border_width = 1
        primary_button_command = save_note
        secondary_button_command = lambda: toggle_read_mode(True)
    else:
        widget_state = tk.DISABLED
        primary_button_text = "Edit"
        secondary_button_text = "Delete"
        mode_text = "Reading Mode"
        border_width = 0
        primary_button_command = lambda: toggle_read_mode(True)
        secondary_button_command = delete_note

    focus_title_entry.configure(state=widget_state, border_width=border_width)
    focus_content_entry.configure(state=widget_state, border_width=border_width)
    focus_edit_button.configure(text=primary_button_text, command=primary_button_command)
    focus_cancel_button.configure(text=secondary_button_text, command=secondary_button_command)
    focus_mode_label.configure(text=mode_text)

def create_new():
    # reset focus styling
    for child in dir_content.winfo_children():
        child.configure(border_width=0)

    toggle_read_mode(False)
    title_var.set("New Note")
    focus_content_entry.delete(1.0, "end")
    focus_content_entry.insert("end", "Insert you note here")

def save_note():
    try:
        fm.create_file(title_var.get(), focus_content_entry.get(1.0, "end-1c"))
        toggle_read_mode(True)
        update_nav_panel()
    except:
        print("Error when saving " + title_var.get())

def delete_note():
    try:
        fm.delete_file(title_var.get())
        update_nav_panel()
    except:
        print("Error when deleting " + title_var.get())

def on_hover(widget, color):
    widget.configure(fg_color=color)

def set_focus(filename, widget):
    title_var.set(filename)
    
    lines = fm.read_file(filename)
    content = "".join(lines)

    focus_content_entry.configure(state="normal")
    focus_content_entry.delete(1.0, "end")
    focus_content_entry.insert("end", content)
    if read_mode:
        focus_content_entry.configure(state="disabled")

    # reset focus styling
    for child in dir_content.winfo_children():
        child.configure(border_width=0)
    widget.configure(border_width=1)

def change_directory():
    output_dir = filedialog.askdirectory(initialdir=fm.directory,
                                         title = "Select Working Directory")
    if output_dir:
        fm.set_directory(output_dir)
        update_nav_panel()

def update_nav_panel():
    # destroy last list
    for widget in dir_content.winfo_children():
        if widget.winfo_id() != create_button.winfo_id():
            widget.destroy()
    create_button.pack_forget()

    # get list of files
    notes = fm.scan_files()
    for filename in notes:
        title = filename.split(".")[0]
        frame = ctk.CTkFrame(master=dir_content,
                             fg_color="transparent",
                             border_width=0,
                             corner_radius=8,
                             cursor="hand2")
        label = ctk.CTkLabel(master=frame,
                             text=title,
                             bg_color="transparent",
                             cursor= "hand2")
        
        label.bind('<Button-1>', lambda e, title=title, widget=frame:set_focus(title, widget))
        label.bind('<Enter>', lambda e, widget=frame:on_hover(widget, "lightgray"))
        label.bind('<Leave>', lambda e, widget=frame:on_hover(widget, "transparent"))
        
        frame.bind('<Button-1>', lambda e, title=title, widget=frame:set_focus(title, widget))
        frame.bind('<Enter>', lambda e, widget=frame:on_hover(widget, "lightgray"))
        frame.bind('<Leave>', lambda e, widget=frame:on_hover(widget, "transparent"))
        
        label.pack(anchor="nw", pady=1, padx=8)
        frame.pack(fill="x")
    create_button.pack(pady=8, fill="x")

# System settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Window
window = ctk.CTk()
window.title('Save-it')
window.geometry('600x600')

# Font definitions
title_font = ctk.CTkFont(family="Calibri", size=32, weight="bold")
subtitle_font = ctk.CTkFont(family="Calibri", size=18, slant="italic")

#startregion - UI Elements
# Title
title_frame = ctk.CTkFrame(master=window,
                           fg_color="transparent",
                           border_width=0)
title_label = ctk.CTkLabel(master=title_frame,
                           text="Save-it",
                           font=title_font)
subtitle_label = ctk.CTkLabel(master=title_frame,
                              text="Digital Post-it",
                              font=subtitle_font)
title_label.pack(side="left", padx=8, anchor="sw")
subtitle_label.pack(side="left", padx=4, anchor="sw")
title_frame.pack(pady=(0,8), padx=16, ipady=8, anchor="nw")

# Main Panel
main_frame = ctk.CTkFrame(master=window,
                          fg_color="transparent",
                          border_width=0)

# Navigation Panel
nav_panel = ctk.CTkFrame(master=main_frame,
                         fg_color="transparent",
                         border_width=0,
                         width=150)
nav_panel.rowconfigure(0, weight=1)
nav_panel.columnconfigure(0, weight=1)

dir_panel = ctk.CTkFrame(master=nav_panel,
                         fg_color="white",
                         border_width=1,
                         corner_radius=8)
dir_content = ctk.CTkFrame(master=dir_panel,
                           fg_color="transparent",
                           border_width=0)

create_button = ctk.CTkButton(master=dir_content,
                              text="Create New Note",
                              command=create_new)

update_nav_panel()

dir_button = ctk.CTkButton(master=nav_panel,
                           text="Change Directory",
                           command=change_directory)

dir_content.pack(pady=8, padx=8, ipady=8, expand=True, fill="both")
dir_panel.grid(row=0,
               column=0,
               pady=(0,8),
               sticky="nsew")
dir_button.grid(row=1,
                column=0,
                sticky="nsew")

# Focus Panel
focus_panel = ctk.CTkFrame(master=main_frame,
                           fg_color="transparent",
                           border_width=0)
focus_panel.rowconfigure(2, weight=1)
focus_panel.columnconfigure([0,1,2], weight=1)

title_var = tk.StringVar()
focus_title_entry = ctk.CTkEntry(master=focus_panel,
                                 placeholder_text="Title",
                                 textvariable=title_var,
                                 state="disabled",
                                 border_width=0)
focus_mode_label = ctk.CTkLabel(master=focus_panel,
                                text="Reading Mode")
                                
focus_content_entry = ctk.CTkTextbox(master=focus_panel,
                                     state="disabled",
                                     border_width=0)
focus_edit_button = ctk.CTkButton(master=focus_panel,
                                  text="Edit",
                                  command=toggle_read_mode)
focus_cancel_button = ctk.CTkButton(master=focus_panel,
                                    text="Delete",
                                    command=delete_note)

focus_title_entry.grid(row=0,
                       column=0,
                       columnspan=3,
                       sticky="nsew")
focus_mode_label.grid(row=1,
                      column=0,
                      columnspan=3,
                      sticky="nsw")
focus_content_entry.grid(row=2,
                         column=0,
                         columnspan=3,
                         pady=(0,8),
                         sticky="nsew")
focus_cancel_button.grid(row=3,
                         column=0,
                         sticky="nsw")
focus_edit_button.grid(row=3,
                       column=2,
                       sticky="nse")

main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=3)
main_frame.rowconfigure(0, weight=1)

nav_panel.grid(row=0, column=0, padx=8, sticky="nsew")
focus_panel.grid(row=0, column=1, padx=8, sticky="nsew")

main_frame.pack(padx=8, pady=8, ipadx=8, expand=True, fill="both")

#endregion - UI Elements

window.mainloop()