import os

bestand = 'user_information.txt'


def file_is_empty():
    with open(bestand, 'r') as file:
        file.seek(0, os.SEEK_END)  # gaat naar einde van file
        if file.tell():
            file.seek(0)  # zet de cursor weer op de 0 positie
            return False
        else:
            return True


def user_signup(user_input):
    file = open(bestand, 'r+')
    if file_is_empty():
        file.write(user_input)
        file.close()
    else:
        append_file = open(bestand, 'a')
        append_file.write(user_input)
        append_file.close()


def username_infile(user_input):
    with open(bestand, 'r')as file:
        readlines = file.readlines()
        print(readlines)

    for elem in readlines:
        elem_mod = elem.strip()

        if elem_mod == user_input:
            print('overeenkomende username gevonden')
            return True
        else:
            print('geen overeenkomende username gevonden')



username_infile('kelvin')
