# Example: This is the GUI for the Program seen by the user
from handle_info import *
from tkinter import *
from API import *
import csv


# Homescreen
def toonhomescreen():
    signup_frame.pack_forget()
    login_frame.pack_forget()
    keuzescherm.pack_forget()
    overzicht_films.pack_forget()

    home_screen.pack()


# Keuze scherm van inloggen of inschrijven
def toonKeuzeScherm():
    home_screen.pack_forget()
    signup_frame.pack_forget()
    login_frame.pack_forget()

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
    name_email = f'{login_field.get()}{login_field_email.get()}'
    if username_infile(name_email):
        currentuser = username_infile(login_field.get())
        print(currentuser)
        toonoverzichtfilms()
    else:
        print('Verkeerde gebruikersnaam!')


def signup():
    if signup_field.get() != '':
        user_signup(f'{signup_field.get()}{signup_field_email.get()}\n')
        toonKeuzeScherm()
    else:
        print('Kan geen lege waarde ontvangen')


def insert_title():
    with open(bestand, "r") as f:
        infile = csv.reader(f)
        for row in infile:
            text = row[0]
            title = text.split(";")[0]
            listbox_movies.insert(END, title)


def CurSelect(event):
    widget = event.widget
    selection = widget.curselection()
    picked = widget.get(selection[0])

    with open(bestand, "r") as f:
        infile = csv.reader(f, delimiter=";")
        for elem in infile:
            '+'.join(elem)
            text = elem
            if picked in elem:
                synops = text[1]
                starttime = text[2]

    movie_name.config(text=str(picked))
    movie_synops.config(text=str(synops))
    movie_start.config(text=str(starttime))


# hierin komt alle opmaak van de tkinter te staan
root = Tk()
root.geometry("768x432")
root.resizable(0, 0)

# _________________________________________________________________________________________________________
# Homescreen met de keuze tussen aanbieder en gebruiker
home_screen = Frame(master=root)
home_screen.pack()

user_btn = Button(master=home_screen, text='Inloggen als Gebruiker', width=40, command=toonKeuzeScherm)
aanbieder_btn = Button(master=home_screen, text='Inloggen als Aanbieder', width=40)

user_btn.pack()
aanbieder_btn.pack()

# _______________________________Gebruiker_________________________________________________________________
# keuze scherm voor inloggen of inschrijven
keuzescherm = Frame(master=root)
keuzescherm.pack(fill="both", expand=True)

keuzescherm_label = Label(master=keuzescherm, text='Maak een keuze')
keuzescherm_label.pack(side=TOP, padx=20, pady=20)

login_button = Button(master=keuzescherm, text='login', command=toonLoginFrame)
login_button.pack(side=RIGHT, padx=20, pady=20)

signup_button = Button(master=keuzescherm, text='signup', command=toonSignUpframe)
signup_button.pack(side=RIGHT, padx=20, pady=20)

go_home_screen = Button(master=keuzescherm, text='<', command=toonhomescreen)
go_home_screen.pack(side=BOTTOM)

# _________________________________________________________________________________________________________
# Login frame
login_frame = Frame(master=root)
login_frame.pack(fill="both", expand=True)

login_name = Label(master=login_frame, text='Naam')
login_field = Entry(master=login_frame)
login_email = Label(master=login_frame, text='Email')
login_field_email = Entry(master=login_frame)

login_field_accept = Button(master=login_frame, text='login', command=login)
back_login = Button(master=login_frame, text='<', command=toonKeuzeScherm)

# layout
login_name.grid(row=0, column=0)
login_field.grid(row=0, column=1)
login_email.grid(row=1, column=0)
login_field_email.grid(row=1, column=1)

back_login.grid(row=1, column=2)
login_field_accept.grid(row=0, column=2)

# _________________________________________________________________________________________________________
# signup frame
signup_frame = Frame(master=root)
signup_frame.pack(fill="both", expand=True)

name_user = Label(master=signup_frame, text='Naam')
signup_field = Entry(master=signup_frame)
email_user = Label(master=signup_frame, text='Email')
signup_field_email = Entry(master=signup_frame)

go_back_button = Button(master=signup_frame, text='<', command=toonKeuzeScherm)
signup_field_accept = Button(master=signup_frame, text='sign up', command=signup)

# Layout
name_user.grid(row=0, column=0)
signup_field.grid(row=0, column=1)
email_user.grid(row=1, column=0)
signup_field_email.grid(row=1, column=1)
go_back_button.grid(row=1, column=2)
signup_field_accept.grid(row=0, column=2)

# _________________________________________________________________________________________________________
# Overzicht van alle films
overzicht_films = Frame(master=root)
overzicht_films.pack_propagate(0)
overzicht_films.pack(fill="both", expand=True)

titel = Label(master=overzicht_films,
              text='Films die vandaag op TV zijn:',
              font=('Helvetica', 12, 'bold italic'),
              width=40
              )

listbox_movies = Listbox(master=overzicht_films, width=40)
insert_title()
listbox_movies.bind('<<ListboxSelect>>', CurSelect)

movie_name = Label(master=overzicht_films)
movie_synops = Label(master=overzicht_films, width=50, wraplengt=300, justify=LEFT)
movie_start = Label(master=overzicht_films)

reserve_btn = Button(master=overzicht_films, text='Reserveren')

# place
titel.grid(row=0, column=0, columnspan=2)
listbox_movies.grid(row=1, column=0, rowspan=3, columnspan=2)

movie_name.grid(row=0, column=2)
movie_start.grid(row=0, column=3)
movie_synops.grid(row=1, column=2, rowspan=3, columnspan=2)
reserve_btn.grid(row=4, column=2)

# ___________________________________________Aanbieder GUI_________________________________________________
# Login , signup voor aanbieder

# Menu, Toon gereserveerde films, toon overzicht films, terug naar homescreen

# Overzicht Films, film reserveren


toonhomescreen()
root.mainloop()
