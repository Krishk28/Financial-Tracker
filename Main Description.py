from tkinter import *           
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import pandas as pd
import customtkinter

# Our app Frame
app = customtkinter.CTk(fg_color="#0b1024")
app.title("Financial Tracker")
app.minsize(app.winfo_screenwidth(), app.winfo_screenheight())
app.state('zoomed')
app.attributes('-fullscreen', True)


# Creating a frame for my widgets
Directions_Frame = customtkinter.CTkFrame(app, corner_radius=25, fg_color="#181a2f")
Directions_Frame.grid(row=0, column=0, pady=15, padx=20, ipady=4)

# Configure rows and columns to expand and fill the available space
app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)
Directions_Frame.rowconfigure(0, weight=1)
Directions_Frame.columnconfigure(0, weight=1)

# Adding UI elements, Text Frame
title = customtkinter.CTkLabel(Directions_Frame, text="Directions:", font=("", 30))
title.grid(row=3, column=4)
header = customtkinter.CTkLabel(app, text="BudgetBuddy", font=("", 50), fg_color="white")
header.grid(row=0, column=0, sticky="nw", padx = 20, pady=20)


def insert_numbered_list():
    items = [
        "Export Financial Data: Go to your banking app or website and export your financial data as a CSV file. This file should contain details of your income and expenses.\n",
        "Upload Data: On the Expense Tracker, use the 'Upload CSV' button to upload the CSV file containing your financial data.\n",
        "Enter Hourly Wage and Savings Goals: After uploading the data, the program will ask you to enter your hourly wage and set your savings goals. Follow the on-screen instructions to enter this information.\n",
        "Track Finances: Once you've uploaded your data and entered your hourly wage and savings goals, you can start tracking your finances.\n",
        "Log Out: Finally, remember to log out of the Expense Tracker when you're done to protect your information.\n"
    ]
    
    for idx, item in enumerate(items, start=1):
        label = customtkinter.CTkLabel(Directions_Frame, text=f"{idx}.   {item}", font=("", 19))
        label.grid(row=idx+5, column=4, padx=20, pady=5)
        label.configure(wraplength=600)  # Set wrap length to 400 pixels so words don't run on

insert_numbered_list()

def import_csv_data():
    global v
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)
    #df = pd.read_csv(csv_file_path)


def openNewWindow():
    Enterpaywindow = Toplevel(app)
    Enterpaywindow.title("Enter Pay")
    Enterpaywindow.geometry("400x200")
    Enterpaywindow.lift()
    Enterpaywindow.attributes("-topmost", True)
    Enterpaywindow.attributes("-topmost", False) 


# Import CSV Button
customtkinter.CTkButton(Directions_Frame, text='Upload CSV', command=import_csv_data,
    border_width=1,
    border_color="black",
    fg_color="transparent").grid(row=13, column=4,pady=5)

# Import Enter Pay button
customtkinter.CTkButton(Directions_Frame, text='Enter Pay', corner_radius=30, command=openNewWindow,
    border_width=1,
    border_color="black",
    fg_color="transparent").grid(row=12, column=4, pady=5)

# Run app
app.mainloop()
