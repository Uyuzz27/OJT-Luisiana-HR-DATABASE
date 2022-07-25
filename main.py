import subprocess
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3
from subprocess import *
"""
GSIS
TIN
Philhealt
HDMF
"""

class ConnectorDB:

    def __init__(self,root):
        self.root = root
        titlespace = " "
        self.root.title(170 * titlespace + "HRM Luisiana Database")
        self.root.geometry("1500x800")
        self.root.configure(bg='#a0c0e5')
        self.root.state('zoomed')

        Mainlabel = Label(root, bg='#f0f0f0', relief='solid')
        Mainlabel.configure(bg='#a0c0e5')
        Mainlabel.place(relx=0.01, rely=0.01, relheight=0.98, relwidth=0.98)

        Titlelabel = Label(root, bg='#4472c4',
                           text="Republic of the Philippines \n Province of Laguna \n MUNICIPALITY OF LUISIANA",
                           width=20, padx=325, pady=10, borderwidth=2, relief='solid',
                           font=('Amasis MT Pro Medium', 10, 'bold'), fg='Black')
        Titlelabel.place(relx=0.01, rely=0.01, relheight=0.10, relwidth=0.98)

        def Register():
            subprocess.run(["E:\Programs\Python\python", "Registration.py"], shell=True)

        def Editing():
            subprocess.run(["E:\Programs\Python\python", "Edit.py"], shell=True)

        button1 = Frame(root, bg="#4472c4", bd=1)
        button1.place(relx=0.88, rely=0.12, relwidth=0.1, relheight=0.05)
        button1a = Button(button1, text="Register", highlightthickness=0, bg="#4472c4", font=("Arial", 10), command= Register)
        button1a.place(relx=0, rely=0, relwidth=1, relheight=1)

        button2 = Frame(root, bg="#4472c4", bd=1)
        button2.place(relx=0.88, rely=0.17, relwidth=0.1, relheight=0.05)
        button2a = Button(button2, text="Edit and Print", highlightthickness=0, bg="#4472c4", font=("Arial", 10), command= Editing)
        button2a.place(relx=0, rely=0, relwidth=1, relheight=1)








        root.mainloop()


    #======================================
    '''def admin_window():
        
        


        root.mainloop

    '''
    #==========================================================







if __name__ == '__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()