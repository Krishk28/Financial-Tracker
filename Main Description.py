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
