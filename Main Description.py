import tkinter
import customtkinter 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import pandas as pd

#Our app Frame
app = customtkinter.CTk()
app.title("Financial Tracker")
app.configure(bg='green')
app.minsize(1920, 1080)  # Set a minimum size larger than the enforced minimum
app.attributes("-fullscreen", True)


#creating a frame for my widgets
Directions_Frame = customtkinter.CTkFrame(app,corner_radius=25)
Directions_Frame.grid(row= 0, column= 0, pady=15, padx=20, ipady=4)

#Adding UI elements, Text Frame
title = ttk.Label(Directions_Frame, text="Directions:", font=("", 24))
title.grid(row=3, column=4)

# Run app
app.mainloop()