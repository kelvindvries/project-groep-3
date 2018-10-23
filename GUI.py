from user_login import *
from tkinter import *
from classes import get_api




root = Tk()

titel = Label(master=root,
              text='Welkom!',
              background='yellow',
              foreground='blue',
              font=('Helvetica', 8, 'bold italic'),
              width=100,
              height=5)

titels = Label(master=root,
              text=get_api.tkinter_data.read(),
              background='yellow',
              foreground='blue',
              font=('Helvetica', 8, 'bold italic'),
              width=100,
              height=50)


titel.pack()
titels.pack()

get_api.tkinter_data.close()






root.mainloop()