import tkinter
import customtkinter
from customtkinter import filedialog
from pytube import YouTube

# Download logic function
def download():
    try:
        ytLink = input_var.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        status_label.configure(text="Downloading\n" + ytObject.title, text_color="white")
        progress_bar.configure(width=400)
        print("Saving " + ytObject.title + " to " + output_dir)

        video.download(output_path=output_dir)

        status_label.configure(text="Download complete!", text_color="white")

    except:
        status_label.configure(text="Download failed", text_color="red")

# Download On Progress Callback function
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress_percentage = bytes_downloaded / total_size * 100
    s_progress = str(int(progress_percentage))

    progress_label.configure(text=s_progress + '%')
    progress_label.update()

    progress_bar.set(float(progress_percentage) / 100)

# Open directory dialog
def search_dir():
    global output_dir
    output_dir = filedialog.askdirectory(initialdir = "/",
                                        title = "Select Output Directory")
    output_label.configure(text="Video will be saved to " + output_dir)

# System settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# UI Elements
title_label = customtkinter.CTkLabel(master=app,
                               text="Insert a YouTube Link")
title_label.pack(padx=10, pady=10)

# Link input box
input_var = tkinter.StringVar()
input_box = customtkinter.CTkEntry(master=app,
                                   textvariable=input_var,
                                   width=350,
                                   height=40)
input_box.pack()

# Output directory
output_dir = "C:/Users/123/Downloads"
output_label = customtkinter.CTkLabel(master=app,
                                      text="Video will be saved to C:/Users/123/Downloads")
output_label.pack()

output_change_button = customtkinter.CTkButton(master=app,
                                               text = "Change output directory",
                                               command = search_dir)
output_change_button.pack()

# Download status label
status_label = customtkinter.CTkLabel(master=app,
                                      text="")
status_label.pack(padx=10, pady=10)

# Download progress bar
progress_label = customtkinter.CTkLabel(master=app,
                                        text="")
progress_label.pack()

progress_bar = customtkinter.CTkProgressBar(master=app,
                                            width=0)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# Download button
button = customtkinter.CTkButton(master=app,
                                 text="Download",
                                 command=download)
button.pack(padx=10, pady=10)

# Run app
app.mainloop()