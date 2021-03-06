# Example: This is the GUI for the Program seen by the user
from handle_info import *
from tkinter import *
from API import *
import csv


# Homescreen, hier is de keus tussen aanbieder of gebruiker
def toonhomescreen():
    # alle schermen die niet gezien moeten worden
    # gebruiker
    keuzescherm.pack_forget()
    signup_frame.pack_forget()
    login_frame.pack_forget()
    overzicht_films.pack_forget()
    ticket.pack_forget()
    # aanbieder
    provider_choice_screen.pack_forget()
    login_provider.pack_forget()
    signup_provider.pack_forget()
    p_menu.pack_forget()
    p_overzicht_films.pack_forget()

    home_screen.pack()
    print('home aanbieder / user')


# Keuze scherm van inloggen of inschrijven
def toonKeuzeScherm():
    home_screen.pack_forget()
    signup_frame.pack_forget()
    login_frame.pack_forget()

    keuzescherm.pack()
    print('keuze scherm user')


def toonProviderChoiceScreen():
    home_screen.pack_forget()
    login_provider.pack_forget()
    signup_provider.pack_forget()
    p_menu.pack_forget()

    provider_choice_screen.pack()
    print('provider home')


def toonLoginFrame():
    keuzescherm.pack_forget()
    login_frame.pack()
    print('login scherm user')


def toonproviderlogin():
    provider_choice_screen.pack_forget()
    login_provider.pack()


def toonSignUpframe():
    keuzescherm.pack_forget()
    signup_frame.pack()
    print('sign up scherm user')


def toonprovidersignup():
    provider_choice_screen.pack_forget()
    signup_provider.pack()
    print("sign up provider")


def toonoverzichtfilms():
    login_frame.pack_forget()
    overzicht_films.pack()
    print('film overzicht user')


def toonticket():
    overzicht_films.pack_forget()
    ticket.pack()
    print('ticket')


def toon_p_overzicht():
    provider_choice_screen.pack_forget()
    login_provider.pack_forget()
    signup_provider.pack_forget()
    p_menu.pack_forget()

    p_overzicht_films.pack()
    print('provider overzicht')


def toon_p_menu():
    login_provider.pack_forget()
    signup_provider.pack_forget()
    p_overzicht_films.pack_forget()

    p_menu.pack()


# Logic
def login_user():
    name_email = f'{login_field.get()}{login_field_email.get()}'
    curuser = f'{login_field.get()}'
    if username_infile(name_email):
        toonoverzichtfilms()
    else:
        print('Verkeerde gebruikersnaam!')

    name_of_user.config(text=str(curuser))
    return name_email


def provider_login():
    p_name_email = f'{p_login_entry_name.get()}{p_login_entry_email.get()}'
    if username_provider_infile(p_name_email):
        toon_p_menu()
    else:
        print('Verkeerde gebruikersnaam!')

    return p_name_email


def signup_user():
    if signup_field.get() != '' and signup_field_email != '':
        handle_user_signup(f'{signup_field.get()}{signup_field_email.get()}\n')
        toonKeuzeScherm()
    else:
        print('Kan geen lege waarde verwerken')


def provider_signup():
    if provider_name != '' and provider_email != '':
        handle_provider_signup(f'{provider_name.get()}{provider_email.get()}\n')
        toonProviderChoiceScreen()
    else:
        print('kan geen waardes doorvoeren')


def u_insert_title():
    with open(bestand, "r") as f:
        infile = csv.reader(f)
        for row in infile:
            text = row[0]
            title = text.split(";")[0]
            listbox_movies.insert(END, title)
    return title


def p_insert_title():
    titles = movies_in_file()
    for row in titles:
        listbox_movies.insert(END, row)


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

    p_movie_name.config(text=str(picked))
    p_movie_synops.config(text=str(synops))
    p_movie_start.config(text=str(starttime))

def reservefilm():
    curuser = login_user()
    picked_movie = movie_name.cget("text")

    # Creert unieke code
    invoerstring = f'{curuser}{picked_movie}'
    orderd = [ord(c) + 3 for c in invoerstring]
    karakter = [chr(d) for d in orderd]
    unique = ''.join(karakter)

    # kijkt of het bestand leeg is
    if file_is_empty(u_bestand_reserved_movies):
        f = open(u_bestand_reserved_movies, 'w')
        f.write(f'{curuser};{picked_movie};{unique}\n')
        f.close()
    else:
        ff = open(u_bestand_reserved_movies, 'a')
        ff.write(f'{curuser};{picked_movie};{unique}\n')
        ff.close()

    name_of_movie.config(text=str(movie_name.cget("text")))
    unique_code.config(text=str(unique))
    toonticket()


def zetopnaam():
    curuser = provider_login()
    picked_movie = movie_name.cget("text")

    if file_is_empty(p_bestand_reserved_opnaam):
        f = open(p_bestand_reserved_opnaam, 'w+')
        f.write(f'{curuser};{picked_movie}\n')
        f.close()

    else:
        ff = open(p_bestand_reserved_opnaam, 'a')
        ff.write(f'{curuser};{picked_movie}\n')
        ff.close()


# hierin komt alle opmaak van de tkinter te staan
root = Tk()
root.geometry("768x432")
root.resizable(0, 0)

# _________________________________________________________________________________________________________
# Homescreen met de keuze tussen aanbieder en gebruiker
home_screen = Frame(master=root)
home_screen.pack()

user_btn = Button(master=home_screen, text='Inloggen als Gebruiker', width=40, command=toonKeuzeScherm)
aanbieder_btn = Button(master=home_screen, text='Inloggen als Aanbieder', width=40, command=toonProviderChoiceScreen)

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

login_field_accept = Button(master=login_frame, text='login', command=login_user)
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
signup_field_accept = Button(master=signup_frame, text='sign up', command=signup_user)

# Layout
name_user.grid(row=0, column=0)
signup_field.grid(row=0, column=1)
email_user.grid(row=1, column=0)
signup_field_email.grid(row=1, column=1)
go_back_button.grid(row=1, column=2)
signup_field_accept.grid(row=0, column=2)

# _________________________________________________________________________________________________________
# Overzicht van alle films voor gebruiker
overzicht_films = Frame(master=root)
overzicht_films.pack_propagate(0)
overzicht_films.pack(fill="both", expand=True)

titel = Label(master=overzicht_films,
              text='Films die vandaag op TV zijn:',
              font=('Helvetica', 12, 'bold italic'),
              width=40
              )

listbox_movies = Listbox(master=overzicht_films, width=40)
u_insert_title()
listbox_movies.bind('<<ListboxSelect>>', CurSelect)

movie_name = Label(master=overzicht_films)
movie_synops = Label(master=overzicht_films, width=50, wraplengt=300, justify=LEFT)
movie_start = Label(master=overzicht_films)

reserve_btn = Button(master=overzicht_films, text='Reserveren', command=reservefilm)

# place
titel.grid(row=0, column=0, columnspan=2)
listbox_movies.grid(row=1, column=0, rowspan=3, columnspan=2)

movie_name.grid(row=0, column=2)
movie_start.grid(row=0, column=3)
movie_synops.grid(row=1, column=2, rowspan=3, columnspan=2)
reserve_btn.grid(row=4, column=2)

# _________________________________________________________________________________________________________
# Ticket
ticket = Frame(master=root)
ticket.pack(fill='both', expand=True)

name_of_user = Label(master=ticket)
name_of_movie = Label(master=ticket)
unique_code = Label(master=ticket)
name_of_provider = Label(master=ticket)

name_of_user.grid(row=0, column=0, columnspan=2)
name_of_movie.grid(row=0, column=2, columnspan=2)
unique_code.grid(row=1, column=2, columnspan=2)
name_of_provider.grid(row=1, column=0, columnspan=2)

# ___________________________________________Aanbieder GUI_________________________________________________
# Keuze scherm aanbieder
provider_choice_screen = Frame(master=root)
provider_choice_screen.pack(fill='both', expand=True)

btn_login = Button(master=provider_choice_screen, text='Login', command=toonproviderlogin)
btn_signup = Button(master=provider_choice_screen, text='Sign Up', command=toonprovidersignup)
btn_naarhome = Button(master=provider_choice_screen, text='Home', command=toonhomescreen)

btn_login.grid()
btn_signup.grid()
btn_naarhome.grid()

# _________________________________________________________________________________________________________
# Login voor aanbieder
login_provider = Frame(master=root)
login_provider.pack(fill="both", expand=True)

login_label_name = Label(master=login_provider, text='Naam')
p_login_entry_name = Entry(master=login_provider)
login_label_email = Label(master=login_provider, text='Email')
p_login_entry_email = Entry(master=login_provider)

login_accept = Button(master=login_provider, text='login', command=provider_login)
back_login_provider = Button(master=login_provider, text='<', command=toonProviderChoiceScreen)

# layout
login_label_name.grid(row=0, column=0)
p_login_entry_name.grid(row=0, column=1)
login_label_email.grid(row=1, column=0)
p_login_entry_email.grid(row=1, column=1)

back_login_provider.grid(row=1, column=2)
login_accept.grid(row=0, column=2)

# _________________________________________________________________________________________________________
# Signup voor aanbieder

signup_provider = Frame(master=root)
signup_provider.pack(fill='both', expand=True)

label_name = Label(master=signup_provider, text='Naam')
provider_name = Entry(master=signup_provider)
label_email = Label(master=signup_provider, text='Email')
provider_email = Entry(master=signup_provider)

back_button = Button(master=signup_provider, text='<', command=toonProviderChoiceScreen)
signup_accept = Button(master=signup_provider, text='sign up', command=provider_signup)

# Layout
label_name.grid(row=0, column=0)
provider_name.grid(row=0, column=1)
label_email.grid(row=1, column=0)
provider_email.grid(row=1, column=1)

back_button.grid(row=1, column=2)
signup_accept.grid(row=0, column=2)

# _________________________________________________________________________________________________________
# Menu, Toon gereserveerde films, toon overzicht films, terug naar homescreen
p_menu = Frame(master=root)
p_menu.pack(fill='both', expand=True)

btn_toonoverzicht = Button(master=p_menu, text='Toon overzicht films', command=toon_p_overzicht)
btn_terug = Button(master=p_menu, text='Terug', command=toonProviderChoiceScreen)

btn_toonoverzicht.grid()
btn_terug.grid()

# _________________________________________________________________________________________________________
# Overzicht Films, film reserveren
p_overzicht_films = Frame(master=root)
p_overzicht_films.pack(fill='both', expand=True)

titel = Label(master=p_overzicht_films,
              text='Films die nog niet op naam staan',
              font=('Helvetica', 12, 'bold italic'),
              width=40
              )

listbox_movies = Listbox(master=p_overzicht_films, width=40)
p_insert_title()
listbox_movies.bind('<<ListboxSelect>>', CurSelect)

p_movie_name = Label(master=p_overzicht_films)
p_movie_synops = Label(master=p_overzicht_films, width=50, wraplengt=300, justify=LEFT)
p_movie_start = Label(master=p_overzicht_films)

reserve_btn = Button(master=p_overzicht_films, text='Zet op naam', command=zetopnaam)
btn_back = Button(master=p_overzicht_films, text='<', command=toon_p_menu)

# place
titel.grid(row=0, column=0, columnspan=2)
listbox_movies.grid(row=1, column=0, rowspan=3, columnspan=2)

p_movie_name.grid(row=0, column=2)
p_movie_start.grid(row=0, column=3)
p_movie_synops.grid(row=1, column=2, rowspan=3, columnspan=2)
reserve_btn.grid(row=4, column=2)
btn_back.grid(row=4, column=3)

toonhomescreen()
root.mainloop()
