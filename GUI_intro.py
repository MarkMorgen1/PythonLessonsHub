import tkinter as tk  # imports the GUI program tkinter
from tkinter import messagebox, ttk  # used for defining messageboxes
from tkinter import PhotoImage  # used to place image in window background

# needed to work with XL files from Python:
import openpyxl
from openpyxl import load_workbook

root = tk.Tk()  # creates the primary window for the app

# define some variables
padx_val = (50, 50)  # define horz space L & R of a label or box
pady_val = (0, 15)  # define vertical space above and below a label or box
font_and_size = ("Arial", 11)
# r in next line means raw string to prevent reading \U... as escape characters
# this is the write-file location and name
file_path = r"C:\Users\markm\OneDrive\Desktop\py_jazz.xlsx"
A = openpyxl.load_workbook(file_path)  # open the XL file
B = A["Registration"]  # use the sheet named in the brackets
image_path = PhotoImage(file=r"C:\Users\markm\OneDrive\Desktop\Berlin.png")
# image needs to be a .png, not a .jpg


def OnClick_Submit():  # call this when "Submit" button is clicked
    name = name_textbox.get()  # get the contents of name_textbox,
    email = email_textbox.get()  # and email_textbox,
    phone = phone_textbox.get()  # and phone_textbox
    branch = branch_dropdown.get()  # and value from dropdown
    agree = agree_value.get()  # agree can only be 0 or 1
    #   print(agree) # test to view value of agree

    if name and email and phone and branch and agree == 1:  # all must be True
        B.append([name, email, phone, branch, "Yes"])  # append items to sheet B
        A.save(file_path)  # save the file named in file_path
        # create a messagebox confirmation
        messagebox.showinfo("Status", "All Data Submitted")
    else:  # show a warning if it didn't work
        messagebox.showwarning("Warning", "Missing Data")


# define the 'root' window characteristics
root.geometry("500x800")  # width x height
root.configure(bg="#F376BF")  # background color.  Click on color square to change.
root.title("Student Registration Form")  # title in menu bar
bg_image = tk.Label(root, image=image_path)  # backround image
bg_image.place(relheight=1, relwidth=1)  # place the image


title_label = tk.Label(
    root, text="Student Registration", font=("Arial", 18, "bold")
)  # define title label of window...
title_label.pack(pady=20)  # then place it top center of window


# define the 'name' label and its data textbox:
name_label = tk.Label(root, text="Enter Name:", font=font_and_size)
# positions name_label at West + padx_val
name_label.pack(anchor=tk.W, padx=padx_val, pady=(15, 0))  # pad above only
name_textbox = tk.Entry(root, font=font_and_size)  # creates the object "name_textbox"
name_textbox.pack(anchor=tk.W, padx=padx_val, pady=pady_val)

# define the 'email' label and textbox
email_label = tk.Label(root, text="Enter Email:", font=font_and_size)
# packs labels and boxes in the window 'root'
email_label.pack(anchor=tk.W, padx=padx_val)
email_textbox = tk.Entry(root, font=font_and_size)  # creates the object "name_textbox"
email_textbox.pack(anchor=tk.W, padx=padx_val, pady=pady_val)

# define the 'phone' label and textbox
phone_label = tk.Label(root, text="Enter Phone #:", font=font_and_size)
phone_label.pack(anchor=tk.W, padx=padx_val)
phone_textbox = tk.Entry(root, font=font_and_size)  # creates the object "name_textbox"
phone_textbox.pack(anchor=tk.W, padx=padx_val, pady=pady_val)

# define the Dropdown box and label:
choices = ["CS", "EL", "ME"]
branch_label = tk.Label(root, text="Select Branch", font=font_and_size)
branch_label.pack(anchor=tk.W, padx=padx_val)
branch_dropdown = ttk.Combobox(root, font=font_and_size, values=choices)
branch_dropdown.pack(anchor=tk.W, padx=padx_val, pady=pady_val)

# define the checkbox
agree_value = tk.IntVar()  # unchecked=0, checked=1
agree_checkbox = tk.Checkbutton(
    root, text="Do you agree with terms?", variable=agree_value, font=font_and_size
)
agree_checkbox.pack(anchor=tk.W, padx=padx_val, pady=pady_val)

#
# define the Submit button characteristics and call OnClick_Submit
submit_btn = tk.Button(
    root, text="Submit Info", font=font_and_size, command=OnClick_Submit
)
submit_btn.pack(anchor=tk.W, padx=padx_val, pady=pady_val)  # locate button

root.mainloop()  # loop the program to keep 'root' window open
