# Create graphical output of beam deflection

import tkinter as tk  # imports the GUI program tkinter
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox, ttk  # used for defining messageboxes
from tkinter import PhotoImage  # used to place image in window background
from Deflec_Simple_SuperPos import plot_deflection

# each call returns a list of x-positions and corresponding y deflections
from Deflec_Cantilever import cantilever_deflection  # (L, P, a, step)

root = tk.Tk()  # creates the primary window for the app

# define some variables for the textboxes
padx_val = (50, 50)  # define horz space L & R of a label or box
pady_val = (0, 15)  # define vertical space above and below a label or box
font_and_size = ("Arial", 11)
# r in next line means raw string to prevent reading \U... as escape characters
# used for background of root window.  Must be .png format
image_path = PhotoImage(file=r"C:\Users\markm\OneDrive\Desktop\plumeria colors.png")


# define what happens when the 'Submit' buttin is clicked
def OnClick_Submit():
    # get the contents of textboxes and convert to floats
    beam_length = float(beam_length_textbox.get())
    left_spt_pos = float(left_spt_pos_textbox.get())  # get positon of supports
    rt_spt_pos = float(rt_spt_pos_textbox.get())
    point_load = float(point_load_textbox.get())
    load_pos = float(load_pos_textbox.get())
    num_points = float(num_points_textbox.get())

    if (
        (left_spt_pos >= 0)
        and (rt_spt_pos > left_spt_pos)
        and (beam_length >= rt_spt_pos)
        and (0 <= load_pos <= beam_length)
        and bool(beam_length)
        and bool(rt_spt_pos)
        and bool(point_load)
        and bool(load_pos)
        and bool(num_points)  # all input fields must be filled and not zero (i.e. True)
    ):
        # create a messagebox confirmation in next line
        # messagebox.showinfo("Status", "Calculating...")
        # call deflection function from Deflec_Simple.py
        L = beam_length
        P = point_load
        a = load_pos
        step = L / num_points
        # call function plot_deflection from outside file
        x, y_flat = plot_deflection(L, 0, a, step)
        x, y1 = cantilever_deflection(L, P, a, step)
        # x, y2 = plot_deflection(L, (P * 1.5), (a / 2), step)
        # x, y3 = plot_deflection(L, (P * 2), (a / 3), step)
        # y_added = y1 + y2 + y3
        plt.plot(x, y1)
        # plt.plot(x, y2)
        # plt.plot(x, y3)
        # plt.plot(x, y_added)
        plt.plot(x, y_flat)
        plt.xlabel("X-values")
        plt.ylabel("Y-values")
        plt.title("Deflection Curve")
        plt.show()

    else:  # show a warning if it didn't work
        messagebox.showwarning("Warning", "Incorrect Data")


# define the 'root' window characteristics
root.geometry("500x800")  # width x height
root.configure(bg="#F376BF")  # background color.  Click on color square to change.
root.title("Beam Deflection Plot")  # title in menu bar
bg_image = tk.Label(root, image=image_path)  # backround image
bg_image.place(relheight=1, relwidth=1)  # place the image


title_label = tk.Label(
    root, text="Simply Supported Beam Deflection", font=("Arial", 18, "bold")
)  # define title label of window...
title_label.pack(pady=20)  # then place it top center of window

# define textboxes and labels
# define the 'Length' label and its data textbox:
beam_length_label = tk.Label(root, text="Enter Beam Length [ft]", font=font_and_size)
beam_length_label.pack(anchor=tk.W, padx=padx_val, pady=(15, 0))  # pad above only
beam_length_textbox = tk.Entry(
    root, font=font_and_size
)  # creates the object "beam_length_textbox"
beam_length_textbox.pack(anchor=tk.W, padx=padx_val, pady=pady_val)


# define the 'left_spt_pos' label and textbox
left_spt_pos_label = tk.Label(
    root, text="Enter Left Support Position:", font=font_and_size
)
# packs labels and boxes in the window 'root'
left_spt_pos_label.pack(anchor=tk.W, padx=padx_val)
left_spt_pos_textbox = tk.Entry(
    root, font=font_and_size
)  # creates the object "left_spt_pos_textbox"
left_spt_pos_textbox.pack(anchor=tk.W, padx=padx_val, pady=pady_val)

# define the 'rt_spt_pos' label and textbox
rt_spt_pos_label = tk.Label(
    root, text="Enter Right Support Position:", font=font_and_size
)
rt_spt_pos_label.pack(anchor=tk.W, padx=padx_val)
rt_spt_pos_textbox = tk.Entry(
    root, font=font_and_size
)  # create and position the object "left_spt_pos_textbox"
rt_spt_pos_textbox.pack(anchor=tk.W, padx=padx_val, pady=pady_val)

# define 'point load value' label and textbox
point_load_label = tk.Label(root, text="Load Value:", font=font_and_size)
point_load_label.pack(anchor=tk.W, padx=padx_val)
point_load_textbox = tk.Entry(root, font=font_and_size)
point_load_textbox.pack(anchor=tk.W, padx=padx_val, pady=pady_val)

# define 'load position' label and textbox
load_pos_label = tk.Label(root, text="Position of Load:", font=font_and_size)
load_pos_label.pack(anchor=tk.W, padx=padx_val)
load_pos_textbox = tk.Entry(root, font=font_and_size)
load_pos_textbox.pack(anchor=tk.W, padx=padx_val, pady=pady_val)

# define 'Number of Points' label and textbox
num_points_label = tk.Label(
    root, text="Number of beam segments for calcs:", font=font_and_size
)
num_points_label.pack(anchor=tk.W, padx=padx_val)
num_points_textbox = tk.Entry(root, font=font_and_size)
num_points_textbox.pack(anchor=tk.W, padx=padx_val, pady=pady_val)


# define the Dropdown box and label:
# choices = ["CS", "EL", "ME"]
# branch_label = tk.Label(root, text="Select Branch", font=font_and_size)
# branch_label.pack(anchor=tk.W, padx=padx_val)
# branch_dropdown = ttk.Combobox(root, font=font_and_size, values=choices)
# branch_dropdown.pack(anchor=tk.W, padx=padx_val, pady=pady_val)

# define the checkbox status
# agree_value = tk.IntVar()  # unchecked=0, checked=1
# agree_checkbox = tk.Checkbutton(
#     root, text="Do you agree with terms?", variable=agree_value, font=font_and_size
# )
# agree_checkbox.pack(anchor=tk.W, padx=padx_val, pady=pady_val)

#
# define the Submit button characteristics and use it to call OnClick_Submit function
submit_btn = tk.Button(
    root, text="Submit Info", font=font_and_size, command=OnClick_Submit
)
submit_btn.pack(anchor=tk.W, padx=padx_val, pady=pady_val)  # locate button


root.mainloop()  # loop the program to keep 'root' window open
