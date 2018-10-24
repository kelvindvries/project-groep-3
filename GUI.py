# Author:   Kelvin de Vries
# Example:  The GUI of the program, getting login value's and sign up value's, gets chosen movie and shows unique coed

from user_info import *
from tkinter import *
from classes import api

api = api.api()


# Keuze scherm van inloggen of inschrijven
def toonKeuzeScherm():
    signup_frame.pack_forget()
    login_frame.pack_forget()
    overzicht_films.pack_forget()
    keuzescherm.pack()
    print('keuze scherm')


# LoginFrame
def toonLoginFrame():
    keuzescherm.pack_forget()
    login_frame.pack()
    print('login scherm')


def toonSignUpframe():
    keuzescherm.pack_forget()
    signup_frame.pack()
    print('sign up scherm')


# overzicht van de films
def toonoverzichtfilms():
    login_frame.pack_forget()
    overzicht_films.pack()
    print('film overzicht')


# Login functie voor het controleren van de ingevoerde waarde in de entry
def login():
    if username_infile(f'{login_field_name}{login_field_email}') == True:
        toonoverzichtfilms()
    else:
        print('Verkeerde gebruikersnaam!')


def signup():
    if signup_field_name.get() != '' and signup_field_email != '':
        user_signup(f'{signup_field_name.get()};{signup_field_email.get()}\n')
        toonKeuzeScherm()
    else:
        print('Kan geen lege waarde ontvangen')


# hierin komt alle opmaak van de tkinter te staan
root = Tk()

# _____________________________________________________________________________________________ #
# keuze scherm voor inloggen of inschrijven
keuzescherm = Frame(master=root)
keuzescherm.pack(fill="both", expand=True)

keuzescherm_label = Label(master=keuzescherm, text='Maak een keuze')
keuzescherm_label.pack(side=TOP, padx=20, pady=20)

login_button = Button(master=keuzescherm, text='login', command=toonLoginFrame)
login_button.pack(side=RIGHT, padx=20, pady=20)

signup_button = Button(master=keuzescherm, text='signup', command=toonSignUpframe)
signup_button.pack(side=RIGHT, padx=20, pady=20)

# _____________________________________________________________________________________________ #
# Login frame
login_frame = Frame(master=root)
login_frame.pack(fill="both", expand=True)

# Entrys, dus alle input
login_field_name = Entry(master=login_frame)
login_field_name.grid(row=0, column=0, padx=20, pady=10)

login_field_email = Entry(master=login_frame)
login_field_email.grid(row=1, column=0, padx=20, pady=10)

# Buttons
back_login = Button(master=login_frame, text='<', height=1, width=5, command=toonKeuzeScherm)
back_login.grid(row=1, column=1, padx=5, pady=5)

login_field_accept = Button(master=login_frame, text='login', height=1, width=5, command=login)
login_field_accept.grid(row=0, column=1)

# _____________________________________________________________________________________________ #
# signup frame
signup_frame = Frame(master=root)
signup_frame.pack(fill="both", expand=True)

# Naam
signup_field_name = Entry(master=signup_frame, text='Naam')
signup_field_name.grid(row=0, column=0, padx=20, pady=10)

# Email
signup_field_email = Entry(master=signup_frame, text='Email')
signup_field_email.grid(row=1, column=0, padx=20, pady=10)

# Buttons
go_back_button = Button(master=signup_frame, text='<', height=1, width=6, command=toonKeuzeScherm)
go_back_button.grid(row=1, column=1, padx=5, pady=5)

signup_field_accept = Button(master=signup_frame, text='sign up', height=1, width=6, command=signup)
signup_field_accept.grid(row=0, column=1)

# _____________________________________________________________________________________________ #
# Overzicht van alle films
overzicht_films = Frame(master=root)
overzicht_films.pack(fill="both", expand=True)

titel = Label(master=overzicht_films,
              text='Overzicht van de films',
              font=('Helvetica', 25, 'bold italic'),
              width=30,
              height=1,
              justify=LEFT
              )
titel.pack()
"""
titels = Label(master=overzicht_films,
               text=api.get_movies(),
               font=('Helvetica', 16, 'bold italic'),
               width=50,
               height=20,
               justify=LEFT
               )
titels.pack()
"""
# _____________________________________________________________________________________________ #

toonKeuzeScherm()
root.mainloop()
