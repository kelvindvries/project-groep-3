# Example: This processes the value's given in the GUI in to a text file and checks entered value's from GUI


import os

bestand_gebruiker = 'user_information.txt'
bestand_aanbieder = 'aanbieder_information.txt'


def file_is_empty(bestand):
    with open(bestand, 'r') as file:
        file.seek(0, os.SEEK_END)  # gaat naar einde van file
        if file.tell():
            file.seek(0)  # zet de cursor weer op de 0 positie
            return False
        else:
            return True


def handle_user_signup(user_input):
    file = open(bestand_gebruiker, 'r+')
    if file_is_empty(bestand_gebruiker):
        file.write(user_input)
        file.close()
    else:
        append_file = open(bestand_gebruiker, 'a')
        append_file.write(user_input)
        append_file.close()


def handle_provider_signup(user_input):
    file = open(bestand_aanbieder, 'r+')
    if file_is_empty(bestand_aanbieder):
        file.write(user_input)
        file.close()
    else:
        appen_file = open(bestand_aanbieder, 'a')
        appen_file.write(user_input)
        appen_file.close()


def username_infile(user_input):
    with open(bestand_gebruiker, 'r')as file:
        readlines = file.readlines()

    for elem in readlines:
        elem_mod = elem.strip()

        if elem_mod == user_input:
            print(f'overeenkomende username gevonden {elem_mod} -- {user_input}')
            return True

        else:
            print('geen overeenkomende username gevonden in gebruiker')


def username_provider_infile(user_input):
    with open(bestand_aanbieder, 'r')as file:
        p_readlines = file.readlines()

    for p_elem in p_readlines:
        p_elem_mod = p_elem.strip()

        if p_elem_mod == user_input:
            print(p_elem_mod, user_input)
            print('overeenkomende username gevonden')
            return True

        else:
            print('geen overeenkomende username gevonden in aanbieder')
