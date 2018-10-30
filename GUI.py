# Author: Kelvin de Vries
# Example: This is the GUI for the Program seen by the user


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
    if username_infile(login_field.get()) == True:
        toonoverzichtfilms()
    else:
        print('Verkeerde gebruikersnaam!')


def signup():
    if signup_field.get() != '':
        user_signup(f'{signup_field.get()}')
        toonKeuzeScherm()
    else:
        print('Kan geen lege waarde ontvangen')


def insert_item():
    for movie in api.get_title():
        print(movie)
        listbox_movies.insert(END, movie)


def CurSelect():



# hierin komt alle opmaak van de tkinter te staan
root = Tk()
root.geometry("400x400+30+30")


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

back_login = Button(master=login_frame, text='<', command=toonKeuzeScherm)
back_login.pack(side=RIGHT, padx=5, pady=20)

login_field_accept = Button(master=login_frame, text='login', command=login)
login_field_accept.pack(side=RIGHT, padx=10, pady=20)

# signup frame
signup_frame = Frame(master=root)
signup_frame.pack(fill="both", expand=True)

signup_field = Entry(master=signup_frame)
signup_field.pack(side=LEFT, padx=10, pady=20)

go_back_button = Button(master=signup_frame, text='<', command=toonKeuzeScherm)
go_back_button.pack(side=RIGHT, padx=5, pady=20)

signup_field_accept = Button(master=signup_frame, text='sign up', command=signup)
signup_field_accept.pack(side=RIGHT, padx=10, pady=20)

# Overzicht van alle films
overzicht_films = Frame(master=root)
overzicht_films.pack(fill="both", expand=True)

titel = Label(master=overzicht_films,
              text='Films die vandaag op TV zijn:',
              font=('Helvetica', 12, 'bold italic'),
              width=30,
              height=1,
              justify=LEFT
              )
titel.pack()

listbox_movies = Listbox(master=overzicht_films, width=40, height=15)
insert_item()
listbox_movies.pack()

toonKeuzeScherm()
root.mainloop()
