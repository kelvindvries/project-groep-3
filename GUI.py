from user_login import *
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
    if login_field.get() == 'admin':
        toonoverzichtfilms()
    else:
        print('Verkeerde gebruikersnaam!')


def signup():
    if signup_field.get() == 'sign':
        toonKeuzeScherm()
    else:
        print('Kan geen lege waarde ontvangen')


# hierin komt alle opmaak van de tkinter te staan
root = Tk()

# keuze scherm voor inloggen of inschrijven
keuzescherm = Frame(master=root)
keuzescherm.pack(fill="both", expand=True)

keuzescherm_label = Label(master=keuzescherm, text='Maak een keuze')
keuzescherm_label.pack(side=TOP, padx=20, pady=20)

login_button = Button(master=keuzescherm, text='login', command=toonLoginFrame)
login_button.pack(side=RIGHT, padx=20, pady=20)

signup_button = Button(master=keuzescherm, text='signup', command=toonSignUpframe)
signup_button.pack(side=RIGHT, padx=20, pady=20)


# Login frame
login_frame = Frame(master=root)
login_frame.pack(fill="both", expand=True)

login_field = Entry(master=login_frame)
login_field.pack(side=LEFT, padx=10, pady=20)

login_field_accept = Button(master=login_frame, text='login', command=login)
login_field_accept.pack(side=RIGHT, padx=10, pady=20)

#signup frame
signup_frame =Frame(master=root)
signup_frame.pack(fill="both", expand=True)

signup_field = Entry(master=signup_frame)
signup_field.pack(side=LEFT, padx=10, pady=20)

signup_field_accept = Button(master=signup_frame, text='sign up', command=signup)
signup_field_accept.pack(side=RIGHT, padx=10, pady=20)

# Overzicht van alle films
overzicht_films = Frame(master=root)
overzicht_films.pack(fill="both", expand=True)

titel = Label(master=overzicht_films,
              text='Welkom!',
              foreground='blue',
              font=('Helvetica', 8, 'bold italic'),
              width=40,
              height=5
              )
titel.pack()

titels = Label(master=overzicht_films,
               text=api.get_movies(),
               foreground='blue',
               font=('Helvetica', 8, 'bold italic'),
               width=40,
               height=10
               )
titels.pack()

toonKeuzeScherm()
root.mainloop()
