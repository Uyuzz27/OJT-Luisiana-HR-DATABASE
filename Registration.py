from os import getcwd, getcwdb
from tkinter import *
from tkinter import ttk
import tkinter as tk
import time
from tkinter import font
import sqlite3

with sqlite3.connect("Employee1.db") as db:
    cursor = db.cursor()
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS employee_id(Personal_id integer PRIMARY KEY AUTOINCREMENT, Office_id ,lastname , firstname , middlename , bday , bplace , gender , civilstatus , address , email , cs_eligibility , majorresponsibilities , datelastpromoted , dateofappointment ,employmentstatus  ); """)


# thinker
class ConnectorDB:

    def __init__(self, root):
        global idfp, idfp2, Lnamep, Fnamep, Mnamep, bday, bpfp, genderdr, civilsdr, Addressfp, emailfp, EmpStatsf, doAppointmentfp, dolPromotionfp, majorresfp, EInfo1, IP_simp, educations, cs_eligibility
        self.root = root
        titlespace = " "
        self.root.title(170 * titlespace + "HRM Luisiana Database")
        self.root.geometry("1500x800")
        self.root.configure(bg='#a0c0e5')
        self.root.state('zoomed')
        # self.root.resizable(0,0)

        # ID
        idfp = StringVar()

        # ==========PERSONAL INFORMATION=======
        Lnamep = StringVar()
        Fnamep = StringVar()
        Mnamep = StringVar()
        bday = StringVar()
        bpfp = StringVar()
        genderdr = StringVar()
        civilsdr = StringVar()
        Addressfp = StringVar()
        emailfp = StringVar()

        # ========EMPLOYMENT INFORMATIONS

        EmpStatus = StringVar()
        Appointment = StringVar()
        Promotion = StringVar()
        Responsibilities = StringVar()

        # the windows main
        headingFrame1 = Frame(root, bg="#4472c4", bd=5)
        headingFrame1.place(relx=0, rely=0, relwidth=1, relheight=0.13)
        headingLabel = Label(headingFrame1,
                             text="                         Republic of the Philippines \n                          Province of Laguna \n                         Municipality of the Philippines",
                             bg='#4472c4', fg='white', font=('Amasis MT Std Medium', 15))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Frame
        idff = Frame(root, bg="blue", bd=1)
        idff.place(relx=.009, rely=0.14, relwidth=.25, relheight=0.08)
        idffa = Label(idff, bg='#a0c0e5')
        idffa.place(relx=0, rely=0, relwidth=1, relheight=1)

        PInfo = Frame(root, bg="blue", bd=1)
        PInfo.place(relx=.01, rely=0.23, relwidth=.98, relheight=0.27)
        PInfo1 = Label(PInfo, bg='#a0c0e5')
        PInfo1.place(relx=0, rely=0, relwidth=1, relheight=1)

        EInfo = Frame(root, bg="blue", bd=1)
        EInfo.place(relx=.01, rely=0.52, relwidth=.98, relheight=0.3)
        EInfo1 = Label(EInfo, bg='#a0c0e5')
        EInfo1.place(relx=0, rely=0, relwidth=1, relheight=1)

        # ID

        idl1 = Label(root, text='ID', bg='#a0c0e5', fg='Black', activebackground="white", font=("Arial", 25))
        idl1.place(relx=.01, rely=0.15, relwidth=.05, relheight=0.05)

        idfp = Entry(root, width=50, font=("Arial", 25))
        idfp.insert(0, "")
        idfp.place(relx=.06, rely=0.15, relwidth=.1, relheight=0.05)

        idl1 = Label(root, text='-', bg='#a0c0e5', fg='Black', activebackground="white", font=("Arial", 25))
        idl1.place(relx=.16, rely=0.15, relwidth=.03, relheight=0.05)

        idfp2 = Entry(root, width=50, font=("Arial", 25))
        idfp2.insert(0, "")
        idfp2.place(relx=.19, rely=0.15, relwidth=.06, relheight=0.05)

        # ================ PERSONAL INFORMATION

        # name
        namel1 = Label(root, text='Name', bg='#a0c0e5', fg='Black', activebackground="white", font=("Arial", 25))
        namel1.place(relx=.02, rely=0.24, relwidth=.1, relheight=0.05)
        n1 = Label(root, text='"Last Name"', bg='#a0c0e5', fg='red', font=("Arial", 10, "italic"))
        n1.place(relx=.02, rely=0.28, relwidth=.07, relheight=0.02)
        Lnamep = Entry(root, width=50, font=("Arial", 20), bd=2)
        Lnamep.insert(0, "")
        Lnamep.place(relx=.02, rely=0.3, relwidth=.15, relheight=0.05)
        n2 = Label(root, text='"First Name"', bg='#a0c0e5', fg='red', font=("Arial", 10, "italic"))
        n2.place(relx=.18, rely=0.28, relwidth=.07, relheight=0.02)
        Fnamep = Entry(root, width=50, font=("Arial", 20), bd=2)
        Fnamep.insert(0, "")
        Fnamep.place(relx=.18, rely=0.3, relwidth=.15, relheight=0.05)
        n3 = Label(root, text='"Middle Name"', bg='#a0c0e5', fg='red', font=("Arial", 10, "italic"))
        n3.place(relx=.34, rely=0.28, relwidth=.07, relheight=0.02)
        Mnamep = Entry(root, width=50, font=("Arial", 20), bd=2)
        Mnamep.insert(0, "")
        Mnamep.place(relx=.34, rely=0.3, relwidth=.15, relheight=0.05)

        # Gendertttttttttt

        genderl1 = Label(root, text='Gender', bg='#a0c0e5', fg='Black', activebackground="white", font=("Arial", 25))
        genderl1.place(relx=.51, rely=0.24, relwidth=.1, relheight=0.05)

        ff = font.Font(family='helvetica', size=12)
        genderdr = ttk.Combobox(root,
                                values=["Female", "Male"],
                                )
        genderdr.place(relx=.51, rely=.3, relwidth=.15, relheight=0.05)
        genderdr.config(font=ff)

        # Birthday

        bdayl1 = Label(root, text='Birthday', bg='#a0c0e5', fg='Black', activebackground="white", font=("Arial", 25))
        bdayl1.place(relx=.67, rely=0.24, relwidth=.1, relheight=0.05)

        Date = Label(root, text='"MM/DD/YYYY"', bg='#a0c0e5', fg='red', font=("Arial", 10, "italic"))
        Date.place(relx=.67, rely=0.28, relwidth=.07, relheight=0.02)

        bday = Entry(root, width=50, font=("Arial", 20), bd=2)
        bday.insert(0, "")
        bday.place(relx=.67, rely=0.3, relwidth=.15, relheight=0.05)

        # civil Status

        civilsl1 = Label(root, text='Civil Status', bg='#a0c0e5', fg='Black', activebackground="white",
                         font=("Arial", 25))
        civilsl1.place(relx=.83, rely=0.24, relwidth=.12, relheight=0.05)

        civilsdr = ttk.Combobox(root,
                                values=["Single", "Married", "Divorced", "Separated", "Widowed"],
                                )
        civilsdr.place(relx=.83, rely=.3, relwidth=.15, relheight=0.05)
        civilsdr.config(font=ff)

        # Birth Place

        bpl1 = Label(root, text='Birth Place', bg='#a0c0e5', fg='Black', activebackground="white", font=("Arial", 25))
        bpl1.place(relx=.02, rely=0.36, relwidth=.1, relheight=0.05)

        bpfp = Entry(root, width=50, font=("Arial", 20), bd=2)
        bpfp.insert(0, "")
        bpfp.place(relx=.02, rely=0.42, relwidth=.26, relheight=0.05)

        # Address

        Addressl1 = Label(root, text='Address', bg='#a0c0e5', fg='Black', activebackground="white", font=("Arial", 25))
        Addressl1.place(relx=.3, rely=0.36, relwidth=.1, relheight=0.05)

        Addressfp = Entry(root, width=50, font=("Arial", 20), bd=2)
        Addressfp.insert(0, "")
        Addressfp.place(relx=.3, rely=0.42, relwidth=.30, relheight=0.05)

        # Email

        emaill1 = Label(root, text='Email   ', bg='#a0c0e5', fg='Black', activebackground="white", font=("Arial", 25))
        emaill1.place(relx=.62, rely=0.36, relwidth=.1, relheight=0.05)

        emailfp = Entry(root, width=50, font=("Arial", 20), bd=2)
        emailfp.insert(0, "")
        emailfp.place(relx=.62, rely=0.42, relwidth=.2, relheight=0.05)

        # =============Employment INFORMATION

        EmpStatsl1 = Label(root, text='Employment Status', bg='#a0c0e5', fg='Black', activebackground="white",
                           font=("Arial", 25))
        EmpStatsl1.place(relx=.02, rely=0.54, relwidth=.2, relheight=0.05)

        EmpStatsf = ttk.Combobox(root,
                                 values=["Permanent", "Job Order", "OJT", "Casual"],
                                 )
        EmpStatsf.place(relx=.04, rely=.6, relwidth=.3, relheight=0.05)
        EmpStatsf.config(font=ff)

        # Date of Original Appointment
        doAppointmentl1 = Label(root, text='Date of Original Appointment', bg='#a0c0e5', fg='Black',
                                activebackground="white", font=("Arial", 25))
        doAppointmentl1.place(relx=.34, rely=0.54, relwidth=.3, relheight=0.05)

        doAppointmentfp = Entry(root, width=50, font=("Arial", 25), bd=2)
        doAppointmentfp.insert(0, "")
        doAppointmentfp.place(relx=.37, rely=.6, relwidth=.25, relheight=0.05)
        Date2 = Label(root, text='"MM/DD/YYYY"', bg='#a0c0e5', fg='red', font=("Arial", 10, "italic"))
        Date2.place(relx=.36, rely=0.58, relwidth=.07, relheight=0.02)

        # cs/educational background
        education = Label(root, text='CS Eigibility', bg='#a0c0e5', fg='Black', activebackground="white",
                          font=("Arial", 25))
        education.place(relx=.64, rely=0.54, relwidth=.15, relheight=0.05)

        cs_eligibility = ttk.Combobox(root,
                                      values=["Civil Service", "RA 1080", "Sub Professional", "Professional", "Others"],
                                      )
        cs_eligibility.place(relx=.66, rely=.6, relwidth=.2, relheight=0.05)
        cs_eligibility.config(font=ff)

        # Date of Last Promotion
        dolPromotionl1 = Label(root, text='Date of Last Promotion', bg='#a0c0e5', fg='Black', activebackground="white",
                               font=("Arial", 25))
        dolPromotionl1.place(relx=.32, rely=0.67, relwidth=.28, relheight=0.05)

        dolPromotionfp = Entry(root, width=50, font=("Arial", 25), bd=2)
        dolPromotionfp.insert(0, "")
        dolPromotionfp.place(relx=.36, rely=0.74, relwidth=.25, relheight=0.05)
        Date1 = Label(root, text='"MM/DD/YYYY"', bg='#a0c0e5', fg='red', font=("Arial", 10, "italic"))
        Date1.place(relx=.36, rely=0.72, relwidth=.07, relheight=0.02)
        # Major Responsibility

        majorresl1 = Label(root, text='Major Responsibility', bg='#a0c0e5', fg='Black', activebackground="white",
                           font=("Arial", 25))
        majorresl1.place(relx=.02, rely=0.67, relwidth=.21, relheight=0.05)

        majorresfp = Entry(root, width=50, font=("Arial", 25), bd=2)
        majorresfp.insert(0, "")
        majorresfp.place(relx=.04, rely=0.74, relwidth=.28, relheight=0.05)

        ##buttons
        # register
        button1 = Frame(self.root, bg="#4472c4", bd=1)
        button1.place(relx=.01, rely=0.86, relwidth=.15, relheight=0.1)
        button = Button(button1, text="Register", highlightthickness=0, bg="#4472c4", font=("Arial", 25), bd=5,
                        command=register)
        button.place(relx=0, rely=0, relwidth=1, relheight=1)
        # done close?
        buttond1 = Frame(self.root, bg="#4472c4", bd=1)
        buttond1.place(relx=.17, rely=0.86, relwidth=.15, relheight=0.1)
        buttond = Button(buttond1, text="Close", highlightthickness=0, bg="#4472c4", font=("Arial", 25), bd=5, command= root.destroy)
        buttond.place(relx=0, rely=0, relwidth=1, relheight=1)

        #conn = sqlite3.connect('Employee1.db')
        #c = conn.cursor()
        #c.execute(
        #    """ CREATE TABLE IF NOT EXISTS employee_id(Personal_id integer PRIMARY KEY AUTOINCREMENT, Office_id ,lastname , firstname , middlename , bday , bplace , gender , civilstatus , address , email , cs_eligibility , majorresponsibilities , datelastpromoted , dateofappointment ,employmentstatus  ); """)

        #c.execute("SELECT *  FROM employee_id")
        #IP_records = c.fetchall()
        #IP_simp = []
        #for item in IP_records:
         #   IP_simp.append(item[1])

        root.mainloop()


def register():
    global g_id,g_id2,g_lastname,g_firstname,g_middlename,g_bday,g_bplace,g_gender,g_civilstatus,g_address,g_email,g_employymentstatus,g_dateofappointment,g_datelastpromoted,g_majorresponsibilities,g_cs_eligibility
    g_id = idfp.get()
    g_id2 = idfp2.get()
    g_lastname = Lnamep.get()
    g_firstname = Fnamep.get()
    g_middlename = Mnamep.get()
    g_bday = bday.get()
    g_bplace = bpfp.get()
    g_gender = genderdr.get()
    g_civilstatus = civilsdr.get()
    g_address = Addressfp.get()
    g_email = emailfp.get()

    g_employymentstatus = EmpStatsf.get()
    g_dateofappointment = doAppointmentfp.get()
    g_datelastpromoted = dolPromotionfp.get()
    g_majorresponsibilities = majorresfp.get()
    g_cs_eligibility = cs_eligibility.get()
    """
    g = len(g_id)
    g = 10-g
    if g <1:
        g=1
    g_id= g_id+g("")
    """

    conn = sqlite3.connect('Employee1.db')
    c = conn.cursor()
    c.execute(
        """ CREATE TABLE IF NOT EXISTS employee_id(Personal_id integer PRIMARY KEY AUTOINCREMENT, Office_id ,lastname , firstname , middlename , bday , bplace , gender , civilstatus , address , email , cs_eligibility , majorresponsibilities , datelastpromoted , dateofappointment ,employmentstatus  ); """)

    c.execute("SELECT *  FROM employee_id")
    IP_records = c.fetchall()
    IP_simp2 = []
    #for item in IP_records:
    #    IP_simp2.append(item[1])



    for item in IP_records:
        print(item[1])
        ID=str(item[1])
        print(type(g_id2))
        print(type(ID))
        if g_id2 == ID:
            print("tama")
            error = Label(root, text=' Personal ID \n already taken \n Please change it ', bg='#a0c0e5', fg='black', bd=2,
                          activebackground="white", font=("Arial", 30))
            error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)

            root.update()
            error.after(5000, error.destroy())
            clear()
            root.mainloop()


        else:
            print("May male")
    check()

def clear():
    idfp.delete(0, END)
    idfp2.delete(0, END)
    Lnamep.delete(0, END)
    Fnamep.delete(0, END)
    Mnamep.delete(0, END)
    bday.delete(0, END)
    bpfp.delete(0, END)
    genderdr.delete(0, END)
    civilsdr.delete(0, END)
    Addressfp.delete(0, END)
    emailfp.delete(0, END)
    EmpStatsf.delete(0, END)
    doAppointmentfp.delete(0, END)
    dolPromotionfp.delete(0, END)
    majorresfp.delete(0, END)
    cs_eligibility.delete(0, END)

    root.update()

def check():

    if g_id == '':
        print(g_id)
        error = Label(root, text='please fill up Office ID information \n thanks', bg='#a0c0e5', fg='black', bd=2,
                      activebackground="white", font=("Arial", 30))
        error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)
    elif g_id2 == '':
        print(g_id2)
        error = Label(root, text='please fill up every information \n thanks', bg='#a0c0e5', fg='black', bd=2,
                      activebackground="white", font=("Arial", 30))
        error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)

    elif g_lastname == '':
        error = Label(root, text='please fill up every information \n thanks', bg='#a0c0e5', fg='black', bd=2,
                      activebackground="white", font=("Arial", 30))
        error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)

    elif g_firstname == '':
        error = Label(root, text='please fill up every information \n thanks', bg='#a0c0e5', fg='black', bd=2,
                      activebackground="white", font=("Arial", 30))
        error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)

    elif g_middlename == '':
        error = Label(root, text='please fill up every information \n thanks', bg='#a0c0e5', fg='black', bd=2,
                      activebackground="white", font=("Arial", 30))
        error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)


    elif g_bday == '':
        error = Label(root, text='please fill up every information \n thanks', bg='#a0c0e5', fg='black', bd=2,
                      activebackground="white", font=("Arial", 30))
        error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)


    elif g_bplace == '':
        error = Label(root, text='please fill up every information \n thanks', bg='#a0c0e5', fg='black', bd=2,
                      activebackground="white", font=("Arial", 30))
        error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)


    elif g_gender == '':
        error = Label(root, text='please fill up every information \n thanks', bg='#a0c0e5', fg='black', bd=2,
                      activebackground="white", font=("Arial", 30))
        error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)


    elif g_civilstatus == '':
        error = Label(root, text='please fill up every information \n thanks', bg='#a0c0e5', fg='black', bd=2,
                      activebackground="white", font=("Arial", 30))
        error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)


    elif g_address == '':
        error = Label(root, text='please fill up every information \n thanks', bg='#a0c0e5', fg='black', bd=2,
                      activebackground="white", font=("Arial", 30))
        error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)


    elif g_email == '':
        error = Label(root, text='please fill up every information \n thanks', bg='#a0c0e5', fg='black', bd=2,
                      activebackground="white", font=("Arial", 30))
        error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)


    elif g_employymentstatus == '':
        error = Label(root, text='please fill up every information \n thanks', bg='#a0c0e5', fg='black', bd=2,
                      activebackground="white", font=("Arial", 30))
        error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)


    elif g_dateofappointment == '':
        error = Label(root, text='please fill up every information \n thanks', bg='#a0c0e5', fg='black', bd=2,
                      activebackground="white", font=("Arial", 30))
        error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)


    elif g_datelastpromoted == '':
        error = Label(root, text='please fill up every information \n thanks', bg='#a0c0e5', fg='black', bd=2,
                      activebackground="white", font=("Arial", 30))
        error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)


    elif g_majorresponsibilities == '':
        error = Label(root, text='please fill up every information \n thanks', bg='#a0c0e5', fg='black', bd=2,
                      activebackground="white", font=("Arial", 30))
        error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)

    elif g_cs_eligibility == '':
        error = Label(root, text='please fill up every information \n thanks', bg='#a0c0e5', fg='black', bd=2,
                      activebackground="white", font=("Arial", 30))
        error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)
    else:

        error = Label(root, text='DONE!!! \n Register \n Another One!', bg='#a0c0e5', fg='black', bd=2,
                      activebackground="white", font=("Arial", 50))
        error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)
        done1()

    root.update()
    error.after(5000, error.destroy())


def done1():
    g_id = idfp.get()
    if g_id == '':
        g_id = 0
    g_id2 = idfp2.get()
    if g_id2 == '':
        g_id2 = 0
    g_lastname = Lnamep.get()
    g_firstname = Fnamep.get()
    g_middlename = Mnamep.get()
    g_bday = bday.get()
    g_bplace = bpfp.get()
    g_gender = genderdr.get()
    g_civilstatus = civilsdr.get()
    g_address = Addressfp.get()
    g_email = emailfp.get()

    g_employymentstatus = EmpStatsf.get()
    g_dateofappointment = doAppointmentfp.get()
    g_datelastpromoted = dolPromotionfp.get()
    g_majorresponsibilities = majorresfp.get()
    g_cs_eligibility = cs_eligibility.get()

    cursor.execute("SELECT COUNT(*) from employee_id WHERE Personal_id = '" + g_id + "' ")
    res_id = cursor.fetchone()

    if int(res_id[0]) > 0:
        pass
    else:
        cursor.execute(
            "INSERT INTO employee_id(Personal_id, Office_id, lastname, firstname, middlename, bday, bplace, gender, civilstatus, address, email,employmentstatus,dateofappointment,datelastpromoted,majorresponsibilities,cs_eligibility)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (g_id2 , g_id, g_lastname, g_firstname, g_middlename, g_bday, g_bplace, g_gender, g_civilstatus, g_address,
             g_email, g_employymentstatus, g_dateofappointment, g_datelastpromoted, g_majorresponsibilities,
             g_cs_eligibility))

        db.commit()

    idfp.delete(0, END)
    idfp2.delete(0, END)
    Lnamep.delete(0, END)
    Fnamep.delete(0, END)
    Mnamep.delete(0, END)
    bday.delete(0, END)
    bpfp.delete(0, END)
    genderdr.delete(0, END)
    civilsdr.delete(0, END)
    Addressfp.delete(0, END)
    emailfp.delete(0, END)
    EmpStatsf.delete(0, END)
    doAppointmentfp.delete(0, END)
    dolPromotionfp.delete(0, END)
    majorresfp.delete(0, END)
    cs_eligibility.delete(0, END)



if __name__ == '__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()
