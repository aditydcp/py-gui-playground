import tkinter
import customtkinter
from pytube import YouTube

# Download logic function
def download():
    try:
        ytLink = input_var.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except:
        print("YouTube link is invalid")
    print("Download Complete!")

# System settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# UI Elements
title = customtkinter.CTkLabel(master=app,
                               text="Insert a YouTube Link")
title.pack(padx=10, pady=10)

# Link input box
input_var = tkinter.StringVar()
input_box = customtkinter.CTkEntry(master=app,
                                   textvariable=input_var,
                                   width=350,
                                   height=40)
input_box.pack()

# Download button
button = customtkinter.CTkButton(master=app,
                                 text="Download",
                                 command=download)
button.pack(padx=10, pady=10)

# Run app
app.mainloop()