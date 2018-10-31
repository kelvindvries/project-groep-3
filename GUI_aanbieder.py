from tkinter import *

root = Tk()
root.geometry("500x500")
root.resizable(0,0)

# Define Screens
# Homescreen
home_screen = Frame(master=root)

overzicht = Frame(master=root)
"""
Overzicht films
    Film op naam zetten
        Film verwijderen voor andere aanbieder
    

"""

# Layout Screens
home_screen.pack(fill='both', expand=True)
overzicht.pack(fill='both', expand=True)

# Mainloop
root.mainloop()
