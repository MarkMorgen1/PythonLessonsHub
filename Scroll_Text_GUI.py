import tkinter as tk
from tkinter import *  # with this import, no need to call tk or tkinter
from tkinter import scrolledtext

root = Tk()  # define primary window (instead of tk.Tk() due to from tkinter import *)
root.geometry("500x600")  # width x height

app_header = Label(
    root, font=("Georgia", 18), text="Scrolled Text Demo", bg="dark blue", fg="white"
)  # white letters on dark blue background
app_header.pack()
# places a scrollable textbox into window 'root'
text_scroll1 = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15, bg="#B7E7F7")
text_scroll1.pack(fill=tk.BOTH, expand=True)
# places a second scrollable textbox below the first
text_scroll1 = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=5, bg="#B7F7B8")
text_scroll1.pack(fill=tk.BOTH, expand=True)


root.mainloop()
