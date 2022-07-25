from fpdf import FPDF
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3
from tkinter import font
import webbrowser


class PDF(FPDF):
    def header(self):
        # logo
        self.image('w.jpg', 20, 8, 25)
        # font
        self.set_font("helvetica", "B", 10)
        # title
        self.cell(0, 10, 'Republic of the Philippines', border=False, ln=1, align='C')
        self.cell(0, 10, 'MUNICIPALITY OF LUISIANA', border=False, ln=1, align='C')
        self.cell(0, 10, 'Province of Laguna', border=False, ln=1, align='C')
        # line break
        self.ln(6)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 10)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='R')


class Printer():

    def __init__(self, root):
        global ID, cs_entry, Lname, Fname, Mname, ID_entry, Lname_entry, Fname_entry, Mname_entry, Bday_entry, Bplace_entry, genderdr, CivilStat_entry, Addr_entry, EmailAddr_entry, EmpStatsf, Appointment_entry, Promotion_entry, Responsibilities_entry, ID_Oentry, ID_PentryCBlname, CBfname, CBmname, CBgender, CBbday, CBbplace, CBcivils, CBaddr, CBemail, CBemstat, CBapp, CBpromo, CBcs
        self.root = root
        titlespace = " "
        self.root.title(170 * titlespace + "HRM Luisiana Database")
        self.root.geometry("1500x800")
        self.root.configure(bg='#a0c0e5')
        self.root.state('zoomed')

        Mainlabel = Label(root, bg='#f0f0f0', relief='solid')
        Mainlabel.configure(bg='#a0c0e5')
        Mainlabel.place(relx=0.01, rely=0.01, relheight=0.98, relwidth=0.98)

        Titlelabel = Label(Mainlabel, bg='#4472c4',
                           text="Republic of the Philippines \n Province of Laguna \n MUNICIPALITY OF LUISIANA",
                           width=20, padx=325, pady=10, borderwidth=2, relief='solid',
                           font=('Amasis MT Pro Medium', 10, 'bold'), fg='Black')
        Titlelabel.place(relx=0, rely=0, relheight=0.10, relwidth=1)

        # ID
        P_ID = StringVar()
        O_ID = StringVar()

        # ==========PERSONAL INFORMATION=======
        Lname = StringVar()
        Fname = StringVar()
        Mname = StringVar()
        Bday = StringVar()
        Bplace = StringVar()
        Gender = StringVar()
        CivilStat = StringVar()
        Addr = StringVar()
        EmailAddr = StringVar()

        # ========EMPLOYMENT INFORMATIONS

        EmpStatus = StringVar()
        Appointment = StringVar()
        Promotion = StringVar()
        Responsibilities = StringVar()
        CS = StringVar()

        # =====================cb/check button
        CBlname = IntVar()
        CBfname = IntVar()
        CBmname = IntVar()
        CBgender = IntVar()
        CBbday = IntVar()
        CBbplace = IntVar()
        CBcivils = IntVar()
        CBaddr = IntVar()
        CBemail = IntVar()
        CBemstat = IntVar()
        CBapp = IntVar()
        CBpromo = IntVar()
        CBrespo = IntVar()
        CBcs = IntVar()
        CBpaper = IntVar()

        # =====================ENTRIES

        my_tree = ttk.Treeview(root)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 15), printllheight=35)
        style.configure("Treeview", font=(None, 15), printllheight=30)

        my_tree['columns'] = ("Office ID", "Personal ID", "Last Name", "First Name", "Middle Name")

        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Office ID", anchor=W, width=90, minwidth=90)
        my_tree.column("Personal ID", anchor=W, width=90, minwidth=90)
        my_tree.column("Last Name", anchor=W, width=90, minwidth=90)
        my_tree.column("First Name", anchor=W, width=90, minwidth=135)
        my_tree.column("Middle Name", anchor=W, width=90, minwidth=90)

        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Office ID", text="Office ID", anchor=W)
        my_tree.heading("Personal ID", text="Personal ID", anchor=W)
        my_tree.heading("Last Name", text="Last Name", anchor=W)
        my_tree.heading("First Name", text="First Name", anchor=W)
        my_tree.heading("Middle Name", text="Middle Name", anchor=W)

        my_tree.place(relx=0.02, rely=0.16, relheight=0.7, relwidth=0.485)

        Table_label = Label(root, bg='#a0c0e5', fg='Black', text='Database', font='Helvetica 15 bold')
        Table_label.place(relx=0.02, rely=0.11, relheight=0.05, relwidth=0.485)

        # ======================= search
        Search_frame = Frame(Mainlabel, bg="blue", bd=1)
        Search_frame.place(relx=.51, rely=0.11, relwidth=.48, relheight=0.75)
        Search1 = Label(Search_frame, bg='#a0c0e5')
        Search1.place(relx=0, rely=0, relwidth=1, relheight=1)

        # ================1st Collumn
        Name_label = Label(root, bg='#a0c0e5', fg='Black', text="Name: ", anchor='nw',
                           font=('Amasis MT Pro Medium', 12, 'bold'))
        Name_label.place(relx=0.52, rely=0.14, relheight=0.05, relwidth=0.04)

        CB_lname = Checkbutton(root, text="Last",
                               variable=CBlname,
                               onvalue=1,
                               offvalue=0,
                               )
        CB_lname.place(relx=0.57, rely=0.135, relheight=0.05, relwidth=0.05)
        LName_entry = Entry(root, textvariable=Lname, font='Helvetica 10 ')
        LName_entry.place(relx=0.625, rely=0.135, relheight=0.05, relwidth=0.125)

        CB_fname = Checkbutton(root, text="First",
                               variable=CBfname,
                               onvalue=1,
                               offvalue=0,
                               )
        CB_fname.place(relx=0.57, rely=0.2, relheight=0.05, relwidth=0.05)
        FName_entry = Entry(root, textvariable=Fname, font='Helvetica 10 ')
        FName_entry.place(relx=0.625, rely=0.2, relheight=0.05, relwidth=0.125)

        CB_mname = Checkbutton(root, text="Middle",
                               variable=CBmname,
                               onvalue=1,
                               offvalue=0,
                               )
        CB_mname.place(relx=0.57, rely=0.265, relheight=0.05, relwidth=0.05)
        MName_entry = Entry(root, textvariable=Mname, font='Helvetica 10 ')
        MName_entry.place(relx=0.625, rely=0.265, relheight=0.05, relwidth=0.125)

        Gender_label = Label(root, bg='#a0c0e5', fg='Black', text="Gender: ", anchor='nw',
                             font=('Amasis MT Pro Medium', 12, 'bold'))
        Gender_label.place(relx=0.52, rely=0.34, relheight=0.05, relwidth=0.15)

        CB_gender = Checkbutton(root,
                                variable=CBgender,
                                onvalue=1,
                                offvalue=0,
                                )
        CB_gender.place(relx=0.57, rely=0.33, relheight=0.05, relwidth=0.03)
        ff = font.Font(family='helvetica', size=12)
        genderdr = ttk.Combobox(root,
                                values=["Female", "Male"],
                                textvariable=Gender)
        genderdr.place(relx=0.605, rely=0.33, relheight=0.05, relwidth=0.145)
        genderdr.config(font=ff)

        Bday_label = Label(root, bg='#a0c0e5', fg='Black', text="Birthday: ", anchor='nw',
                           font=('Amasis MT Pro Medium', 12, 'bold'))
        Bday_label.place(relx=0.52, rely=.405, relheight=0.05, relwidth=0.15)
        CB_bday = Checkbutton(root,
                              variable=CBbday,
                              onvalue=1,
                              offvalue=0,
                              )
        CB_bday.place(relx=0.57, rely=0.395, relheight=0.05, relwidth=0.03)
        Bday_entry = Entry(root, textvariable=Bday, font='Helvetica 10 ')
        Bday_entry.place(relx=0.605, rely=0.395, relheight=0.05, relwidth=0.145)
        #
        Bplace_label = Label(root, bg='#a0c0e5', fg='Black', text="Birthplace: ", anchor='nw',
                             font=('Amasis MT Pro Medium', 10, 'bold'))
        Bplace_label.place(relx=0.52, rely=0.47, relheight=0.05, relwidth=0.15)
        CB_bplace = Checkbutton(root,
                                variable=CBbplace,
                                onvalue=1,
                                offvalue=0,
                                )
        CB_bplace.place(relx=0.57, rely=0.46, relheight=0.05, relwidth=0.03)
        Bplace_entry = Entry(root, textvariable=Bplace, font='Helvetica 10 ')
        Bplace_entry.place(relx=0.605, rely=0.46, relheight=0.05, relwidth=0.145)
        #
        CivilStat_label = Label(root, bg='#a0c0e5', fg='Black', text="Civil Status ", anchor='nw',
                                font=('Amasis MT Pro Medium', 10, 'bold'))
        CivilStat_label.place(relx=0.52, rely=0.535, relheight=0.05, relwidth=0.15)
        CB_civils = Checkbutton(root,
                                variable=CBcivils,
                                onvalue=1,
                                offvalue=0,
                                )
        CB_civils.place(relx=0.57, rely=0.525, relheight=0.05, relwidth=0.03)
        CivilStat_entry = Entry(root, textvariable=CivilStat, font='Helvetica 10 ')
        CivilStat_entry.place(relx=0.605, rely=0.525, relheight=0.05, relwidth=0.145)
        #
        Addr_label = Label(root, bg='#a0c0e5', fg='Black', text="Address: ", anchor='nw',
                           font=('Amasis MT Pro Medium', 10, 'bold'))
        Addr_label.place(relx=0.52, rely=0.6, relheight=0.05, relwidth=0.15)
        CB_addr = Checkbutton(root,
                              variable=CBaddr,
                              onvalue=1,
                              offvalue=0,
                              )
        CB_addr.place(relx=0.57, rely=0.59, relheight=0.05, relwidth=0.03)
        Addr_entry = Entry(root, textvariable=Addr, font='Helvetica 10 ')
        Addr_entry.place(relx=0.605, rely=0.59, relheight=0.05, relwidth=0.145)
        #
        EmailAddr_label = Label(root, bg='#a0c0e5', fg='Black', text="Email Add: ", anchor='nw',
                                font=('Amasis MT Pro Medium', 10, 'bold'))
        EmailAddr_label.place(relx=0.52, rely=0.665, relheight=0.05, relwidth=0.15)
        CB_email = Checkbutton(root,
                               variable=CBemail,
                               onvalue=1,
                               offvalue=0,
                               )
        CB_email.place(relx=0.57, rely=0.655, relheight=0.05, relwidth=0.03)
        EmailAddr_entry = Entry(root, textvariable=EmailAddr, font='Helvetica 10 ')
        EmailAddr_entry.place(relx=0.605, rely=0.655, relheight=0.05, relwidth=0.145)

        # =========================2nd Collumn
        ID_Olabel = Label(root, bg='#a0c0e5', fg='Black', text="ID ", anchor='nw',
                          font=('Amasis MT Pro Medium', 12, 'bold'))
        ID_Olabel.place(relx=0.76, rely=0.14, relheight=0.06, relwidth=0.04)
        ID_Oentry = Entry(root, textvariable=O_ID, font='Helvetica 10 ')
        ID_Oentry.place(relx=0.8, rely=0.135, relheight=0.05, relwidth=0.087)

        ID_Plabel = Label(root, bg='#a0c0e5', fg='Black', text="--", anchor='nw',
                          font=('Amasis MT Pro Medium', 12, 'bold'))
        ID_Plabel.place(relx=0.894, rely=0.14, relheight=0.06, relwidth=0.04)
        ID_Pentry = Entry(root, textvariable=P_ID, font='Helvetica 10 ')
        ID_Pentry.place(relx=0.91, rely=0.135, relheight=0.05, relwidth=0.05)
        ######
        EmpStatus_label = Label(root, bg='#a0c0e5', fg='Black', text="Emploment Status ", anchor='nw',
                                font=('Amasis MT Pro Medium', 12, 'bold'))
        EmpStatus_label.place(relx=0.76, rely=0.205, relheight=0.06, relwidth=0.18)
        CB_emstat = Checkbutton(root,
                                variable=CBemstat,
                                onvalue=1,
                                offvalue=0,
                                )
        CB_emstat.place(relx=0.93, rely=0.195, relheight=0.05, relwidth=0.03)
        EmpStatsf = ttk.Combobox(root,
                                 values=["Permanent", "Job Order", "OJT", "Cadsual"],
                                 textvariable=EmpStatus)
        EmpStatsf.place(relx=0.76, rely=0.25, relheight=0.05, relwidth=0.2)
        EmpStatsf.config(font=ff)
        #
        Appointment_label = Label(root, bg='#a0c0e5', fg='Black', text="Date of Appointment ", anchor='nw',
                                  font=('Amasis MT Pro Medium', 12, 'bold'))
        Appointment_label.place(relx=0.76, rely=0.315, relheight=0.05, relwidth=0.15)
        CB_app = Checkbutton(root,
                             variable=CBapp,
                             onvalue=1,
                             offvalue=0,
                             )
        CB_app.place(relx=0.93, rely=0.305, relheight=0.05, relwidth=0.03)
        Appointment_entry = Entry(root, textvariable=Appointment, font='Helvetica 10 ')
        Appointment_entry.place(relx=0.76, rely=0.36, relheight=0.05, relwidth=0.2)
        #
        Promotion_label = Label(root, bg='#a0c0e5', fg='Black', text="Date of Last Promotion ", anchor='nw',
                                font=('Amasis MT Pro Medium', 12, 'bold'))
        Promotion_label.place(relx=0.76, rely=0.425, relheight=0.05, relwidth=0.15)
        CB_promo = Checkbutton(root,
                               variable=CBpromo,
                               onvalue=1,
                               offvalue=0,
                               )
        CB_promo.place(relx=0.93, rely=0.415, relheight=0.05, relwidth=0.03)
        Promotion_entry = Entry(root, textvariable=Promotion, font='Helvetica 10 ')
        Promotion_entry.place(relx=0.76, rely=0.47, relheight=0.05, relwidth=0.2)
        #
        Responsibilities_label = Label(root, bg='#a0c0e5', fg='Black', text="Responsibilities ", anchor='nw',
                                       font=('Amasis MT Pro Medium', 12, 'bold'))
        Responsibilities_label.place(relx=0.76, rely=0.535, relheight=0.05, relwidth=0.15)
        CB_respo = Checkbutton(root,
                               variable=CBrespo,
                               onvalue=1,
                               offvalue=0,
                               )
        CB_respo.place(relx=0.93, rely=0.525, relheight=0.05, relwidth=0.03)
        Responsibilities_entry = Entry(root, textvariable=Responsibilities, font='Helvetica 10 ')
        Responsibilities_entry.place(relx=0.76, rely=0.585, relheight=0.05, relwidth=0.2)
        #
        cs_label = Label(root, bg='#a0c0e5', fg='Black', text="Educational Backround", anchor='nw',
                         font=('Amasis MT Pro Medium', 12, 'bold'))
        cs_label.place(relx=0.76, rely=0.65, relheight=0.05, relwidth=0.15)
        CB_cs = Checkbutton(root,
                            variable=CBcs,
                            onvalue=1,
                            offvalue=0,
                            )
        CB_cs.place(relx=0.93, rely=0.64, relheight=0.05, relwidth=0.03)
        cs_entry = ttk.Combobox(root,
                                values=["Civil Service", "RA 1080", "Sub Professional", "Professional", "Others"],
                                textvariable=CS)
        cs_entry.place(relx=0.76, rely=0.7, relheight=0.05, relwidth=0.2)
        cs_entry.config(font=ff)

        CB_paper = Checkbutton(root,
                               variable=CBpaper,
                               onvalue=1,
                               offvalue=0,
                               )
        CB_paper.place(relx=0.93, rely=0.78, relheight=0.05, relwidth=0.03)

        cs_land = Label(root, bg='#a0c0e5', fg='Black', text="Landscape", anchor='nw',
                        font=('Amasis MT Pro Medium', 12, 'bold'))
        cs_land.place(relx=0.85, rely=0.79, relheight=0.05, relwidth=0.07)

        # ==========
        def selectRecord(a):

            ID_Oentry.delete(0, END)
            ID_Pentry.delete(0, END)
            LName_entry.delete(0, END)
            FName_entry.delete(0, END)
            MName_entry.delete(0, END)
            Bday_entry.delete(0, END)
            Bplace_entry.delete(0, END)
            genderdr.delete(0, END)
            CivilStat_entry.delete(0, END)
            Addr_entry.delete(0, END)
            EmailAddr_entry.delete(0, END)

            EmpStatsf.delete(0, END)
            Appointment_entry.delete(0, END)
            Promotion_entry.delete(0, END)
            Responsibilities_entry.delete(0, END)
            cs_entry.delete(0, END)

            selected = my_tree.focus()
            values = my_tree.item(selected, 'values')

            conn = sqlite3.connect('Employee1.db')
            with conn:
                cursor = conn.cursor()
            for e in cursor.execute(
                    "SELECT * FROM employee_id WHERE Personal_id= " + values[1] + " AND Office_id= " + values[0] + ";"):
                ID_Oentry.insert(0, e[1])
                ID_Pentry.insert(0, e[0])
                LName_entry.insert(0, e[2])
                FName_entry.insert(0, e[3])
                MName_entry.insert(0, e[4])
                Bday_entry.insert(0, e[5])
                Bplace_entry.insert(0, e[6])
                genderdr.insert(0, e[7])
                CivilStat_entry.insert(0, e[8])
                Addr_entry.insert(0, e[9])
                EmailAddr_entry.insert(0, e[10])
                cs_entry.insert(0, e[11])
                Responsibilities_entry.insert(0, e[12])
                Promotion_entry.insert(0, e[13])
                Appointment_entry.insert(0, e[14])
                EmpStatsf.insert(0, e[15])

        # =========

        # =========================================================

        def save():
            minfo = P_ID.get()
            minfo1 = O_ID.get()
            pinfo1 = Lname.get()
            pinfo2 = Fname.get()
            pinfo3 = Mname.get()
            pinfo4 = Bday.get()
            pinfo5 = Bplace.get()
            pinfo6 = Gender.get()
            pinfo7 = CivilStat.get()
            pinfo8 = Addr.get()
            pinfo9 = EmailAddr.get()

            einfo5 = EmpStatus.get()
            einfo4 = Appointment.get()
            einfo3 = Promotion.get()
            einfo2 = Responsibilities.get()
            einfo1 = CS.get()

            conn = sqlite3.connect('Employee1.db')
            with conn:
                cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO PERSONAL_INFO (Personal_id, Office_id , lastname , firstname , middlename, bday, bplace, gender, civilstatus, address, email, cs_eligibility , majorresponsibilities, datelastpromoted, dateofappointment, employmentstatus ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                (minfo, minfo1, pinfo1, pinfo2, pinfo3, pinfo4, pinfo5, pinfo6, pinfo7, pinfo8, pinfo9, einfo1, einfo2,
                 einfo3, einfo4, einfo5))
            conn.commit()

        def check():
            g_id = P_ID.get()
            g_id2 = O_ID.get()
            g_lastname = Lname.get()
            g_firstname = Fname.get()
            g_middlename = Mname.get()
            g_bday = Bday.get()
            g_bplace = Bplace.get()
            g_gender = Gender.get()
            g_civilstatus = CivilStat.get()
            g_address = Addr.get()
            g_email = EmailAddr.get()

            g_employymentstatus = EmpStatus.get()
            g_dateofappointment = Appointment.get()
            g_datelastpromoted = Promotion.get()
            g_majorresponsibilities = Responsibilities.get()
            g_cs_eligibility = CS.get()

            if g_id2 == '':
                error = Label(root, text='Please Fill Up Personal Identification \n thanks', bg='#a0c0e5', fg='black',
                              bd=2,
                              activebackground="white", font=("Arial", 20))
                error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)

            elif g_id == '':
                error = Label(root, text='Please Fill Up Office ID \n thanks', bg='#a0c0e5', fg='black', bd=2,
                              activebackground="white", font=("Arial", 20))
                error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)

            elif g_lastname == '':
                error = Label(root, text='Please Fill Up Last Name \n thanks', bg='#a0c0e5', fg='black', bd=2,
                              activebackground="white", font=("Arial", 20))
                error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)

            elif g_firstname == '':
                error = Label(root, text='Please Fill Up First Name \n thanks', bg='#a0c0e5', fg='black', bd=2,
                              activebackground="white", font=("Arial", 20))
                error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)

            elif g_middlename == '':
                error = Label(root, text='Please Fill Up Middle Name \n thanks', bg='#a0c0e5', fg='black', bd=2,
                              activebackground="white", font=("Arial", 20))
                error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)


            elif g_bday == '':
                error = Label(root, text='Please Input Birthday \n thanks', bg='#a0c0e5', fg='black', bd=2,
                              activebackground="white", font=("Arial", 20))
                error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)


            elif g_bplace == '':
                error = Label(root, text='Please Fill Up Birth Place \n thanks', bg='#a0c0e5', fg='black', bd=2,
                              activebackground="white", font=("Arial", 20))
                error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)


            elif g_gender == '':
                error = Label(root, text='Please Fill Up Gender \n thanks', bg='#a0c0e5', fg='black', bd=2,
                              activebackground="white", font=("Arial", 20))
                error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)


            elif g_civilstatus == '':
                error = Label(root, text='Choose Civil Status \n thanks', bg='#a0c0e5', fg='black', bd=2,
                              activebackground="white", font=("Arial", 20))
                error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)


            elif g_address == '':
                error = Label(root, text='Please Fill Up The Address \n thanks', bg='#a0c0e5', fg='black', bd=2,
                              activebackground="white", font=("Arial", 20))
                error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)


            elif g_email == '':
                error = Label(root, text='Please Fill Up Email Address \n thanks', bg='#a0c0e5', fg='black', bd=2,
                              activebackground="white", font=("Arial", 20))
                error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)


            elif g_employymentstatus == '':
                error = Label(root, text='Choose Employment Status \n thanks', bg='#a0c0e5', fg='black', bd=2,
                              activebackground="white", font=("Arial", 20))
                error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)


            elif g_dateofappointment == '':
                error = Label(root, text='Please Fill Up Date of Appointment \n thanks', bg='#a0c0e5', fg='black', bd=2,
                              activebackground="white", font=("Arial", 20))
                error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)


            elif g_datelastpromoted == '':
                error = Label(root, text='Please Fill Up Date of Last Promotion \n thanks', bg='#a0c0e5', fg='black',
                              bd=2,
                              activebackground="white", font=("Arial", 20))
                error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)


            elif g_majorresponsibilities == '':
                error = Label(root, text='Select Major Responsibilities \n thanks', bg='#a0c0e5', fg='black', bd=2,
                              activebackground="white", font=("Arial", 20))
                error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)

            elif g_cs_eligibility == '':
                error = Label(root, text='Select Civil Service Eligibility \n thanks', bg='#a0c0e5', fg='black', bd=2,
                              activebackground="white", font=("Arial", 20))
                error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)
            else:

                error = Label(root, text='DONE!!! \n Updating!', bg='#a0c0e5', fg='black', bd=2,
                              activebackground="white", font=("Arial", 30))
                error.place(relx=.3, rely=0.3, relwidth=.4, relheight=0.4)
                update()
            root.update()
            error.after(4000, error.destroy())

        # UPDATE
        def update():

            minfo = P_ID.get()
            minfo1 = O_ID.get()

            pinfo1 = Lname.get()
            pinfo2 = Fname.get()
            pinfo3 = Mname.get()
            pinfo4 = Bday.get()
            pinfo5 = Bplace.get()
            pinfo6 = Gender.get()
            pinfo7 = CivilStat.get()
            pinfo8 = Addr.get()
            pinfo9 = EmailAddr.get()

            einfo5 = EmpStatus.get()
            einfo4 = Appointment.get()
            einfo3 = Promotion.get()
            einfo2 = Responsibilities.get()
            einfo1 = CS.get()

            conn = sqlite3.connect('Employee1.db')
            with conn:
                cursor = conn.cursor()
            cursor.execute("""UPDATE employee_id SET 
                                lastname=:lname , 
                                firstname=:fname , 
                                middlename=:mname, 
                                bday=:bday, 
                                bplace=:bplace,
                                gender=:gen, 
                                civilstatus=:civstat, 
                                address=:add, 
                                email=:em,
                                cs_eligibility=:cs,
                                employmentstatus=:emstat, 
                                dateofappointment=:dateapp, 
                                datelastpromoted=:datepro, 
                                majorresponsibilities=:res

                                WHERE Personal_id =:PID AND Office_id = :OID""",
                           {
                               'PID': minfo,
                               'OID': minfo1,
                               'lname': pinfo1,
                               'fname': pinfo2,
                               'mname': pinfo3,
                               'bday': pinfo4,
                               'bplace': pinfo5,
                               'gen': pinfo6,
                               'civstat': pinfo7,
                               'add': pinfo8,
                               'em': pinfo9,
                               'cs': einfo1,
                               'res': einfo2,
                               'datepro': einfo3,
                               'dateapp': einfo4,
                               'emstat': einfo5,
                           })
            conn.commit()
            reload()
            root.update()

        def reload():
            for e in my_tree.get_children():
                my_tree.delete(e)
            conn = sqlite3.connect('Employee1.db')
            with conn:
                cursor1 = conn.cursor()
                cursor1.execute(
                    """ CREATE TABLE IF NOT EXISTS employee_id(Personal_id integer PRIMARY KEY AUTOINCREMENT, Office_id ,lastname , firstname , middlename , bday , bplace , gender , civilstatus , address , email , cs_eligibility , majorresponsibilities , datelastpromoted , dateofappointment ,employmentstatus  ); """)

            cursor1.execute("SELECT * FROM employee_id ")
            conn.commit()

            for e in cursor1:
                my_tree.insert(parent='', index='end', iid=e[1], text="Parent", values=(e[0], e[1], e[2], e[3], e[4]))
            my_tree.bind("<ButtonRelease-1>", selectRecord)
            root.update()

        def clear():
            ID_Oentry.delete(0, END)
            ID_Pentry.delete(0, END)
            LName_entry.delete(0, END)
            FName_entry.delete(0, END)
            MName_entry.delete(0, END)
            Bday_entry.delete(0, END)
            Bplace_entry.delete(0, END)
            genderdr.delete(0, END)
            CivilStat_entry.delete(0, END)
            Addr_entry.delete(0, END)
            EmailAddr_entry.delete(0, END)

            EmpStatsf.delete(0, END)
            Appointment_entry.delete(0, END)
            Promotion_entry.delete(0, END)
            Responsibilities_entry.delete(0, END)
            cs_entry.delete(0, END)
            root.update()


        def search():
            for e in my_tree.get_children():
                my_tree.delete(e)

            con = sqlite3.connect('Employee1.db')
            cur = con.cursor()
            minfo = P_ID.get()
            minfo1 = O_ID.get()

            pinfo1 = Lname.get()
            pinfo2 = Fname.get()
            pinfo3 = Mname.get()
            pinfo4 = Bday.get()
            pinfo5 = Bplace.get()
            pinfo6 = Gender.get()
            pinfo7 = CivilStat.get()
            pinfo8 = Addr.get()
            pinfo9 = EmailAddr.get()

            einfo5 = EmpStatus.get()
            einfo4 = Appointment.get()
            einfo3 = Promotion.get()
            einfo2 = Responsibilities.get()
            einfo1 = CS.get()

            toprint = ""
            pap = "p"
            if CBlname.get() == 1:
                if len(toprint) > 0:
                    toprint = toprint + " AND "
                toprint = toprint + "lastname = '" + pinfo1 + "'"
            if CBfname.get() == 1:
                if len(toprint) > 0:
                    toprint = toprint + " AND "
                toprint = toprint + "firstname = '" + pinfo2 + "'"
            if CBmname.get() == 1:
                if len(toprint) > 0:
                    toprint = toprint + " AND "
                toprint = toprint + "middlename = '" + pinfo3 + "'"
            if CBbday.get() == 1:
                if len(toprint) > 0:
                    toprint = toprint + " AND "
                toprint = toprint + "bday = '" + pinfo4 + "'"
            if CBbplace.get() == 1:
                if len(toprint) > 0:
                    toprint = toprint + " AND "
                toprint = toprint + "bplace = '" + pinfo5 + "' "
            if CBgender.get() == 1:
                if len(toprint) > 0:
                    toprint = toprint + " AND "
                toprint = toprint + "gender = '" + pinfo6 + "' "
            if CBcivils.get() == 1:
                if len(toprint) > 0:
                    toprint = toprint + " AND "
                toprint = toprint + "civilstatus = '" + pinfo7 + "' "
            if CBaddr.get() == 1:
                if len(toprint) > 0:
                    toprint = toprint + " AND "
                toprint = toprint + "address = '" + pinfo8 + "' "
            if CBemail.get() == 1:
                if len(toprint) > 0:
                    toprint = toprint + " AND "
                toprint = toprint + "email = '" + pinfo9 + "' "
            if CBcs.get() == 1:
                if len(toprint) > 0:
                    toprint = toprint + " AND "
                toprint = toprint + "cs_eligibility = '" + einfo1 + "' "
            if CBrespo.get() == 1:
                if len(toprint) > 0:
                    toprint = toprint + " AND "
                toprint = toprint + "majorresponsibilities = '" + einfo2 + "' "
            if CBpromo.get() == 1:
                if len(toprint) > 0:
                    toprint = toprint + " AND "
                toprint = toprint + "datelastpromoted = '" + einfo3 + "' "
            if CBapp.get() == 1:
                if len(toprint) > 0:
                    toprint = toprint + " AND "
                toprint = toprint + "dateofappointment = '" + einfo4 + "' "
            if CBemstat.get() == 1:
                if len(toprint) > 0:
                    toprint = toprint + " AND "
                toprint = toprint + "employmentstatus = '" + einfo5 + "' "
            else:
                cur.execute("SELECT * FROM employee_id ")
                con.commit()
            print(toprint)
            cur.execute("SELECT * FROM employee_id WHERE " + toprint + " ;")
            print(cur.execute)

            for e in cur:
                my_tree.insert(parent='', index='end', iid=e[1], text="Parent", values=(e[0], e[1], e[2], e[3], e[4]))
            my_tree.bind("<ButtonRelease-1>", selectRecord)
            root.update()

        def printtopdf():
            con = sqlite3.connect('Employee1.db')
            cur = con.cursor()

            toprint = "Personal_id, Office_id"
            printll = " Personal ID,  Office ID"
            pap = "p"
            if CBlname.get() == 1:
                toprint = toprint + ", lastname"
                printll = printll + ",  lastname"
            if CBfname.get() == 1:
                toprint = toprint + ", firstname"
                printll = printll + ",  firstname"
            if CBmname.get() == 1:
                toprint = toprint + ", middlename"
                printll = printll + ",  Middlename"
            if CBbday.get() == 1:
                toprint = toprint + ", bday"
                printll = printll + ",  Birthday"
            if CBbplace.get() == 1:
                toprint = toprint + ", bplace"
                printll = printll + ",  Birth Place"
            if CBgender.get() == 1:
                toprint = toprint + ", gender"
                printll = printll + ",  Gender"
            if CBcivils.get() == 1:
                toprint = toprint + ", civilstatus"
                printll = printll + ",  Civil Status"
            if CBaddr.get() == 1:
                toprint = toprint + ", address"
                printll = printll + ",  Address"
            if CBemail.get() == 1:
                toprint = toprint + ", email"
                printll = printll + ",  Email"
            if CBcs.get() == 1:
                toprint = toprint + ", cs_eligibility"
                printll = printll + ", Educational"
            if CBrespo.get() == 1:
                toprint = toprint + ", majorresponsibilities"
                printll = printll + ",Responsibility"
            if CBpromo.get() == 1:
                toprint = toprint + ", datelastpromoted"
                printll = printll + ",last Promoted"
            if CBapp.get() == 1:
                toprint = toprint + ", dateofappointment"
                printll = printll + ",Appointment"
            if CBemstat.get() == 1:
                toprint = toprint + ",employmentstatus"
                printll = printll + ", Employment"
            if CBpaper.get() == 1:
                pap = "L"
            else:
                pap = "P"

            pdf = PDF(orientation=pap, unit="mm", format="A4")
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("helvetica", "B", 11)

            top = []
            printll = str(printll)
            printll = printll.replace("'", "")
            printll = printll.replace(")", "")
            printll = printll.replace("(", "")
            top = printll.split(",")

            for hhs in top:
                pdf.cell(30, 18, hhs, border=1)

            pdf.ln(18)
            pdf.set_font("helvetica", "", 7)

            hold = []
            for e in my_tree.get_children():
                empinfo1 = my_tree.item(e, 'values')[0]
                perinfo2 = my_tree.item(e, 'values')[1]
                for row in cur.execute(
                        "SELECT " + toprint + " FROM employee_id WHERE Personal_id= '" + perinfo2 + "' AND Office_id= '" + empinfo1 + "'"):
                    print(empinfo1, perinfo2)
                    row = str(row)
                    row = row.replace("'", "")
                    row = row.replace(")", "")
                    row = row.replace("(", "")
                    hold = row.split(",")

                    for element in hold:
                        pdf.cell(30, 6, element, border=1)
                    pdf.ln(6)

            pdf.output("Print.pdf", 'F')
            webbrowser.open_new('Print.pdf')

        button1a = Button(root, text="Print", highlightthickness=0, bg="#4472c4", font=("Arial", 10),
                          command=printtopdf)
        button1a.place(relx=0.52, rely=0.78, relwidth=0.07, relheight=0.05)

        button2a = Button(root, text="Search", highlightthickness=0, bg="#4472c4", font=("Arial", 10),
                          command=search)
        button2a.place(relx=0.595, rely=0.78, relwidth=0.07, relheight=0.05)

        button3a = Button(root, text="Quit", highlightthickness=0, bg="#4472c4", font=("Arial", 10),
                          command=root.destroy)
        button3a.place(relx=0.67, rely=0.78, relwidth=0.07, relheight=0.05)

        button4a = Button(root, text="Clear", highlightthickness=0, bg="#4472c4", font=("Arial", 10),
                          command=clear)
        button4a.place(relx=0.745, rely=0.78, relwidth=0.07, relheight=0.05)


        reload()

        root.mainloop()
        # ========================================

        # ======================================

        # ==========================================================


if __name__ == '__main__':
    root = Tk()
    application = Printer(root)
    root.mainloop()
