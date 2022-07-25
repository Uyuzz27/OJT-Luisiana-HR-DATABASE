import subprocess
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3
from tkinter import font
from Print import *
from subprocess import *

class ConnectorDB:

    def __init__(self, root):
        global ID,cs_entry, Lname, Fname, Mname, ID_entry, Lname_entry, Fname_entry, Mname_entry, Bday_entry, Bplace_entry, genderdr, CivilStat_entry, Addr_entry, EmailAddr_entry, EmpStatsf, Appointment_entry, Promotion_entry, Responsibilities_entry, ID_Oentry, ID_Pentry

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

        # =====================ENTRIES

        my_tree = ttk.Treeview(root)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 15), rowheight=35)
        style.configure("Treeview", font=(None, 15), rowheight=30)

        my_tree['columns'] = ("Office ID","Personal ID", "Last Name", "First Name", "Middle Name")

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
        LName_entry = Entry(root, textvariable=Lname, font='Helvetica 10 ')
        LName_entry.place(relx=0.57, rely=0.135, relheight=0.05, relwidth=0.18)

        FName_entry = Entry(root, textvariable=Fname, font='Helvetica 10 ')
        FName_entry.place(relx=0.57, rely=0.2, relheight=0.05, relwidth=0.18)

        MName_entry = Entry(root, textvariable=Mname, font='Helvetica 10 ')
        MName_entry.place(relx=0.57, rely=0.265, relheight=0.05, relwidth=0.18)

        Gender_label = Label(root, bg='#a0c0e5', fg='Black', text="Gender: ", anchor='nw',
                             font=('Amasis MT Pro Medium', 12, 'bold'))
        Gender_label.place(relx=0.52, rely=0.34, relheight=0.05, relwidth=0.15)

        ff = font.Font(family='helvetica', size=12)
        genderdr = ttk.Combobox(root,
                                values=["Female", "Male"],
                                textvariable=Gender)
        genderdr.place(relx=0.57, rely=0.33, relheight=0.05, relwidth=0.18)
        genderdr.config(font=ff)

        Bday_label = Label(root, bg='#a0c0e5', fg='Black', text="Birthday: ", anchor='nw',
                           font=('Amasis MT Pro Medium', 12, 'bold'))
        Bday_label.place(relx=0.52, rely=.405, relheight=0.05, relwidth=0.15)
        Bday_entry = Entry(root, textvariable=Bday, font='Helvetica 10 ')
        Bday_entry.place(relx=0.57, rely=0.395, relheight=0.05, relwidth=0.18)

        Bplace_label = Label(root, bg='#a0c0e5', fg='Black', text="Birthplace: ", anchor='nw',
                             font=('Amasis MT Pro Medium', 10, 'bold'))
        Bplace_label.place(relx=0.52, rely=0.47, relheight=0.05, relwidth=0.15)
        Bplace_entry = Entry(root, textvariable=Bplace, font='Helvetica 10 ')
        Bplace_entry.place(relx=0.57, rely=0.46, relheight=0.05, relwidth=0.18)

        CivilStat_label = Label(root, bg='#a0c0e5', fg='Black', text="Civil Status ", anchor='nw',
                                font=('Amasis MT Pro Medium', 10, 'bold'))
        CivilStat_label.place(relx=0.52, rely=0.535, relheight=0.05, relwidth=0.15)
        CivilStat_entry = Entry(root, textvariable=CivilStat, font='Helvetica 10 ')
        CivilStat_entry.place(relx=0.57, rely=0.525, relheight=0.05, relwidth=0.18)

        Addr_label = Label(root, bg='#a0c0e5', fg='Black', text="Address: ", anchor='nw',
                           font=('Amasis MT Pro Medium', 10, 'bold'))
        Addr_label.place(relx=0.52, rely=0.6, relheight=0.05, relwidth=0.15)
        Addr_entry = Entry(root, textvariable=Addr, font='Helvetica 10 ')
        Addr_entry.place(relx=0.57, rely=0.59, relheight=0.05, relwidth=0.18)

        EmailAddr_label = Label(root, bg='#a0c0e5', fg='Black', text="Email Add: ", anchor='nw',
                                font=('Amasis MT Pro Medium', 10, 'bold'))
        EmailAddr_label.place(relx=0.52, rely=0.665, relheight=0.05, relwidth=0.15)
        EmailAddr_entry = Entry(root, textvariable=EmailAddr, font='Helvetica 10 ')
        EmailAddr_entry.place(relx=0.57, rely=0.655, relheight=0.05, relwidth=0.18)

        # =========================2nd Collumn
        ID_Plabel = Label(root, bg='#a0c0e5', fg='Black', text="ID ", anchor='nw',
                         font=('Amasis MT Pro Medium', 12, 'bold'))
        ID_Plabel.place(relx=0.76, rely=0.14, relheight=0.06, relwidth=0.04)
        ID_Pentry = Entry(root, textvariable=P_ID, font='Helvetica 10 ')
        ID_Pentry.place(relx=0.8, rely=0.135, relheight=0.05, relwidth=0.087)

        ID_Olabel = Label(root, bg='#a0c0e5', fg='Black', text="--", anchor='nw',
                    font=('Amasis MT Pro Medium', 12, 'bold'))
        ID_Olabel.place(relx=0.894, rely=0.14, relheight=0.06, relwidth=0.04)
        ID_Oentry = Entry(root, textvariable=O_ID, font='Helvetica 10 ')
        ID_Oentry.place(relx=0.91, rely=0.135, relheight=0.05, relwidth=0.05)

        EmpStatus_label = Label(root, bg='#a0c0e5', fg='Black', text="Emploment Status ", anchor='nw',
                                font=('Amasis MT Pro Medium', 12, 'bold'))
        EmpStatus_label.place(relx=0.76, rely=0.205, relheight=0.06, relwidth=0.18)
        EmpStatsf = ttk.Combobox(root,
                                 values=["Permanent", "Job Order", "OJT", "Cadsual"],
                                 textvariable=EmpStatus)
        EmpStatsf.place(relx=0.76, rely=0.25, relheight=0.05, relwidth=0.2)
        EmpStatsf.config(font=ff)

        Appointment_label = Label(root, bg='#a0c0e5', fg='Black', text="Date of Appointment ", anchor='nw',
                                  font=('Amasis MT Pro Medium', 12, 'bold'))
        Appointment_label.place(relx=0.76, rely=0.315, relheight=0.05, relwidth=0.15)
        Appointment_entry = Entry(root, textvariable=Appointment, font='Helvetica 10 ')
        Appointment_entry.place(relx=0.76, rely=0.36, relheight=0.05, relwidth=0.2)

        Promotion_label = Label(root, bg='#a0c0e5', fg='Black', text="Date of Last Promotion ", anchor='nw',
                                font=('Amasis MT Pro Medium', 12, 'bold'))
        Promotion_label.place(relx=0.76, rely=0.425, relheight=0.05, relwidth=0.15)
        Promotion_entry = Entry(root, textvariable=Promotion, font='Helvetica 10 ')
        Promotion_entry.place(relx=0.76, rely=0.47, relheight=0.05, relwidth=0.2)

        Responsibilities_label = Label(root, bg='#a0c0e5', fg='Black', text="Responsibilities ", anchor='nw',
                                       font=('Amasis MT Pro Medium', 12, 'bold'))
        Responsibilities_label.place(relx=0.76, rely=0.535, relheight=0.05, relwidth=0.15)
        Responsibilities_entry = Entry(root, textvariable=Responsibilities, font='Helvetica 10 ')
        Responsibilities_entry.place(relx=0.76, rely=0.585, relheight=0.05, relwidth=0.2)

        cs_label = Label(root, bg='#a0c0e5', fg='Black', text="educational backround", anchor='nw',
                         font=('Amasis MT Pro Medium', 12, 'bold'))
        cs_label.place(relx=0.76, rely=0.65, relheight=0.05, relwidth=0.15)

        cs_entry = ttk.Combobox(root,
                                values=["Civil Service", "RA 1080", "Sub Professional", "Professional", "Others"],
                                textvariable=CS)
        cs_entry.place(relx=0.76, rely=0.7, relheight=0.05, relwidth=0.2)
        cs_entry.config(font=ff)

        # ==========
        def printer():
        #subprocess.call(['python Print.py'])
            subprocess.run(["E:\Programs\Python\python","Print.py"], shell=True)



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
            cursor.execute("SELECT * FROM employee_id WHERE Personal_id= " + values[1] + " AND Office_id= " + values[0] + ";")
            conn.commit()

            for e in cursor:
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
                (minfo, minfo1, pinfo1, pinfo2, pinfo3, pinfo4, pinfo5, pinfo6, pinfo7, pinfo8, pinfo9,einfo1, einfo2, einfo3, einfo4, einfo5))
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
                error = Label(root, text='Please Fill Up Personal Identification \n thanks', bg='#a0c0e5', fg='black', bd=2,
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
                error = Label(root, text='Please Fill Up Date of Last Promotion \n thanks', bg='#a0c0e5', fg='black', bd=2,
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
                               'cs':einfo1,
                               'res': einfo2,
                               'datepro': einfo3,
                               'dateapp': einfo4,
                               'emstat': einfo5,
                           })
            conn.commit()
            reload()
            root.update()

        def delete():
            minfo = P_ID.get()
            minfo1 = O_ID.get()
            conn = sqlite3.connect('Employee1.db')
            with conn:
                cursor = conn.cursor()
            cursor.execute("DELETE FROM employee_id WHERE Personal_id= '" + minfo1 + "'AND Office_id='" + minfo + "' ;")
            print(minfo1)
            print(minfo)
            conn.commit()
            reload()
            root.update()

        def reload():
            for e in my_tree.get_children():
                my_tree.delete(e)
            conn = sqlite3.connect('Employee1.db')
            with conn:
                cursor1 = conn.cursor()
            cursor1.execute("SELECT * FROM employee_id ")
            conn.commit()

            for e in cursor1:
                my_tree.insert(parent='', index='end', iid=e[1], text="Parent", values=(e[0], e[1], e[2], e[3],e[4]))
            my_tree.bind("<ButtonRelease-1>", selectRecord)
            root.update()

        button1 = Frame(root, bg="#4472c4", bd=1)
        button1.place(relx=0.515, rely=0.76, relwidth=0.1, relheight=0.05)
        button1a = Button(button1, text="Update", highlightthickness=0, bg="#4472c4", font=("Arial", 10),
                          command=check)
        button1a.place(relx=0, rely=0, relwidth=1, relheight=1)

        button2 = Frame(root, bg="#4472c4", bd=1)
        button2.place(relx=0.625, rely=0.76, relwidth=0.1, relheight=0.05)
        button2a = Button(button2, text="Delete", highlightthickness=0, bg="#4472c4", font=("Arial", 10),
                          command=delete)
        button2a.place(relx=0, rely=0, relwidth=1, relheight=1)

        button3 = Frame(root, bg="#4472c4", bd=1)
        button3.place(relx=0.735, rely=0.76, relwidth=0.1, relheight=0.05)
        button3a = Button(button3, text="Quit", highlightthickness=0, bg="#4472c4", font=("Arial", 10),
                          command=root.destroy)
        button3a.place(relx=0, rely=0, relwidth=1, relheight=1)

        button4 = Frame(root, bg="#4472c4", bd=1)
        button4.place(relx=0.845, rely=0.76, relwidth=0.1, relheight=0.05)
        button4a = Button(button4, text="Print", highlightthickness=0, bg="#4472c4", font=("Arial", 10),
                          command= printer)
        button4a.place(relx=0, rely=0, relwidth=1, relheight=1)

        reload()

        root.mainloop()
        # ========================================

        # ======================================

        # ==========================================================


if __name__ == '__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()