from user_login import *
from tkinter import *
from classes import api


# Keuze scherm van inloggen of inschrijven
def toonKeuzeScherm():
    loginFrame.pack_forget()
    overzichtfilms.pack_forget()
    keuzescherm.pack()


# LoginFrame
def toonLoginFrame():
    keuzescherm.pack_forget()
    loginFrame.pack()

# Login functie voor het controleren van de ingevoerde waarde in de entry
def login():
    if loginfield.get() == 'admin':
        toonoverzichtfilms()
    else:
        print('Verkeerde gebruikersnaam!')


# hierin komt alle opmaak van de tkinter te staan
root = Tk()

# keuze scherm voor inloggen of inschrijven
keuzescherm = Frame(master=root)
keuzescherm.pack(fill="both", expand=True)
keuzeschermlabel = Label(master=keuzescherm, text='Maak een keuze')
keuzeschermlabel.pack(side=TOP, padx=20, pady=20)
loginbutton = Button(master=keuzescherm, text='login', command=toonLoginFrame)
loginbutton.pack(side=RIGHT, padx=20, pady=20)
signupbutton = Button(master=keuzescherm, text='sign up')
signupbutton.pack(side=LEFT, padx=20, pady=20)

# Login frame
loginFrame = Frame(master=root)
loginFrame.pack(fill="both", expand=True)
loginfield = Entry(master=loginFrame)
loginfield.pack(padx=20, pady=20)
loginfieldaccept = Button(master=loginFrame, text='login', command=login)
loginfieldaccept.pack(padx=20, pady=20)

# Overzicht van alle films
overzichtfilms = Frame(master=root)
overzichtfilms.pack(fill="both", expand=True)

titel = Label(master=overzichtfilms,
              text='Welkom!',
              foreground='blue',
              font=('Helvetica', 8, 'bold italic'),
              width=40,
              height=5
              )
titel.pack()

titels = Label(master=overzichtfilms,
               text=get_api.tkinter_data.read(),
               foreground='blue',
               font=('Helvetica', 8, 'bold italic'),
               width=40,
               height=10
               )
titels.pack()

get_api.tkinter_data.close()

toonKeuzeScherm()
root.mainloop()
