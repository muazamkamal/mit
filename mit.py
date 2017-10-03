import Tkinter as tk
import datetime as dt

class Management(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Configuring windows properties
        self.title("M.I.T")
        self.geometry("640x640")
        self.resizable(False,False)

        #Variables of all the dynamic StringVar
        global usrnm
        global pswd

        usrnm = tk.StringVar()
        pswd = tk.StringVar()

        global usrnmREG
        global pswdREG

        usrnmREG = tk.StringVar()
        pswdREG = tk.StringVar()

        global NameOfStudREG
        global ConOfStudREG
        global EmConOfStudREG
        global AddMathREG
        global PhyREG
        global ChemREG

        NameOfStudREG = tk.StringVar()
        ConOfStudREG = tk.StringVar()
        EmConOfStudREG = tk.StringVar()
        AddMathREG = tk.IntVar()
        PhyREG = tk.IntVar()
        ChemREG = tk.IntVar()

        global NameOfStud
        global ConOfStud
        global EmConOfStud
        global SubOfStud
        global FeeOfStud
        global OutFeeOfStud
        global REGdateStud

        NameOfStud = tk.StringVar()
        ConOfStud = tk.StringVar()
        EmConOfStud = tk.StringVar()
        SubOfStud = tk.StringVar()
        FeeOfStud = tk.StringVar()
        OutFeeOfStud = tk.StringVar()
        REGdateStud = tk.StringVar()

        # Setting up frames or pages
        global container
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # Layering the frames and bringing up "MainMenu" to the top
        self.frames = {}

        for F in (Welcome, Login, Register, MainMenu, Registration, StudentRegistration, Student, StudentDetail):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(Welcome)

    # Method for bringing up specific frames based on argument.
    def show_frame(self, cont):

        # Refreshing/reloading the called frame before bringing it up
        for F in (Welcome, Login, Register, MainMenu, Student, StudentDetail):
            if cont == F:
                F(container, self)

        frame = self.frames[cont]
        frame.tkraise()

    # Method for getting variables between frames
    def get_page(self, classname):
        return self.frames[classname]

# Welcome frame
class Welcome(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        WelcomeTitle = tk.Label(self, text="Welcome!", font = 22, bg = "white")
        WelcomeTitle.pack(padx = 10, pady = 10)

        loginButton = tk.Button(self, text="Login", command = lambda: controller.show_frame(Login), bg = "white")
        loginButton.pack(side = "top", padx = 10, pady = 10)

        registerButton = tk.Button(self, text="Register", command = lambda: controller.show_frame(Register), bg = "white")
        registerButton.pack(side = "top", padx = 10, pady = 10)

        testButton = tk.Button(self, text="Test", command = lambda: controller.show_frame(MainMenu), bg = "white")
        testButton.pack(side = "top", padx = 10, pady = 10)

        quitButton = tk.Button(self, text="Quit", command = lambda: quit(), bg = "white")
        quitButton.pack(side = "bottom", pady = 10)

# Login frame
class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        LoginTitle = tk.Label(self, text="Login", font = 22, bg = "white")
        LoginTitle.pack(padx = 10, pady = 10)

        usernameLabel = tk.Label(self, text = "Username", bg = "white")
        usernameEntry = tk.Entry(self, width = 25, textvariable = usrnm)
        passwordLabel = tk.Label(self, text = "Password", bg = "white")
        passwordEntry = tk.Entry(self, show = "*", width = 25, textvariable = pswd)

        usernameLabel.pack()
        usernameEntry.pack()
        passwordLabel.pack()
        passwordEntry.pack()

        submitButton = tk.Button(self, text="Login", command = lambda: self.auth(), bg = "white")
        submitButton.pack(padx = 10, pady = 10)

        backButton = tk.Button(self, text="Back", command = lambda: controller.show_frame(Welcome), bg = "white")
        backButton.pack(side = "bottom", padx = 10, pady = 10)

    def auth(self):
        # Fetch the user input
        submitUsrnm = usrnm.get()
        submitPswd = pswd.get()

        # Check if user put both username and password
        if submitUsrnm == "" or submitPswd == "":
            # Error box if user did not complete the input
            errorCREDS = tk.Toplevel(bg = "white")
            errorCREDS.grab_set()
            errorCREDS.title("Credentials Error")
            errorCREDS.geometry("250x100")
            errorCREDS.resizable(False,False)

            errorCREDSmsg = tk.Label(errorCREDS, text = "Please enter your username/password!", bg = "white")
            errorCREDSmsg.pack(padx = 10, pady = 10)

            dismissButton = tk.Button(errorCREDS, text = "Dismiss", bg = "white", command = errorCREDS.destroy)
            dismissButton.pack(padx = 10, pady = 10)

            self.wait_window(errorCREDS)
            errorCREDS.grab_release()

            # Set the input box back to empty
            usrnm.set("")
            pswd.set("")

        else:
            # Read data from database
            creds = open("credentialDB", "r") # Need to check if database exist or not REMEMBER ME TO DO THIS!
            temp = creds.readlines()
            creds.close()

            # Check if database is not empty
            if temp != []:
                credsData = []
                for i in range(len(temp)):
                    credsData.append(temp[i].replace("\n", " ").split(", "))

                # Cross check for every single username and password from database
                wrongcounter = 0
                for i in range(len(credsData)):
                    if submitUsrnm != credsData[i][0] or submitPswd != credsData[i][1]:
                        wrongcounter += 1

                # If there is a match, set input back to empty and login to MainMenu
                if wrongcounter != len(credsData):
                    usrnm.set("")
                    pswd.set("")

                    self.controller.show_frame(MainMenu)

                # If no match, display error box, input back to empty.
                else:
                    errorAUTH = tk.Toplevel(bg = "white")
                    errorAUTH.grab_set()
                    errorAUTH.title("Authentication Error")
                    errorAUTH.geometry("250x100")
                    errorAUTH.resizable(False,False)

                    errorAUTHmsg = tk.Label(errorAUTH, text = "Username/Password not found!", bg = "white")
                    errorAUTHmsg.pack(padx = 10, pady = 10)

                    dismissButton = tk.Button(errorAUTH, text = "Dismiss", bg = "white", command = errorAUTH.destroy)
                    dismissButton.pack(padx = 10, pady = 10)

                    self.wait_window(errorAUTH)
                    errorAUTH.grab_release()
                    usrnm.set("")
                    pswd.set("")

            # Error box if database is empty
            else:
                errorDB = tk.Toplevel(bg = "white")
                errorDB.grab_set()
                errorDB.title("Databse Error")
                errorDB.geometry("250x100")
                errorDB.resizable(False,False)

                errorDBmsg = tk.Label(errorDB, text = "Database empty!", bg = "white")
                errorDBmsg.pack(padx = 10, pady = 10)

                dismissButton = tk.Button(errorDB, text = "Dismiss", bg = "white", command = errorDB.destroy)
                dismissButton.pack(padx = 10, pady = 10)

                self.wait_window(errorDB)
                errorDB.grab_release()

                usrnm.set("")
                pswd.set("")

#Register frame
class Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        RegisterTitle = tk.Label(self, text="Register", font = 22, bg = "white")
        RegisterTitle.pack(padx = 10, pady = 10)

        usernameREGLabel = tk.Label(self, text = "Username", bg = "white")
        usernameREGEntry = tk.Entry(self, width = 25, textvariable = usrnmREG)
        passwordREGLabel = tk.Label(self, text = "Password", bg = "white")
        passwordREGEntry = tk.Entry(self, show = "*", width = 25, textvariable = pswdREG)

        usernameREGLabel.pack()
        usernameREGEntry.pack()
        passwordREGLabel.pack()
        passwordREGEntry.pack()

        registerButton = tk.Button(self, text="Register", command = lambda: self.register(), bg = "white")
        registerButton.pack(padx = 10, pady = 10)

        backButton = tk.Button(self, text="Back", command = lambda: controller.show_frame(Welcome), bg = "white")
        backButton.pack(side = "bottom", padx = 10, pady = 10)

    def register(self):
        registerUsrnm = usrnmREG.get()
        registerPswd = pswdREG.get()

        if registerUsrnm == "" or registerPswd == "":
            # Error if no username/password entered by user
            errorREG = tk.Toplevel(bg = "white")
            errorREG.grab_set()
            errorREG.title("Registration Error")
            errorREG.geometry("250x100")
            errorREG.resizable(False,False)

            errorREGmsg = tk.Label(errorREG, text = "Please enter your username/password!", bg = "white")
            errorREGmsg.pack(padx = 10, pady = 10)

            dismissButton = tk.Button(errorREG, text = "Dismiss", bg = "white", command = errorREG.destroy)
            dismissButton.pack(padx = 10, pady = 10)

            self.wait_window(errorREG)
            errorREG.grab_release()

            usrnmREG.set("")
            pswdREG.set("")

        else:
            # Add new username and password to database
            creds=open("credentialDB","a+")
            datatowrite=[registerUsrnm,registerPswd]
            for data in datatowrite:
                creds.write(data + ", ")
            creds.write("\n")
            creds.close()

            usrnmREG.set("")
            pswdREG.set("")

            # Redirect to Login frame
            self.controller.show_frame(Login)

            # Display success registration message
            successREG = tk.Toplevel(bg = "white")
            successREG.grab_set()
            successREG.title("Registration Successful")
            successREG.resizable(False,False)

            successREGmsg = tk.Label(successREG, text = "Username \"%s\" has been successfully registered!" % registerUsrnm, bg = "white")
            successREGmsg.pack(padx = 10, pady = 10)

            dismissButton = tk.Button(successREG, text = "Dismiss", bg = "white", command = successREG.destroy)
            dismissButton.pack(padx = 10, pady = 10)

            self.wait_window(successREG)
            successREG.grab_release()

# MainMenu frame
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        MenuTitle = tk.Label(self, text="Main Menu", font = 22, bg = "white")
        MenuTitle.pack(padx = 10, pady = 10)

        registrationButton = tk.Button(self, text="Registration", command = lambda: controller.show_frame(Registration), bg = "white")
        registrationButton.pack(padx = 10, pady = 10)

        studentButton = tk.Button(self, text="Student", command = lambda: controller.show_frame(Student), bg = "white")
        studentButton.pack(padx = 10, pady = 10)

        quitButton = tk.Button(self, text="Quit", command = lambda: quit(), bg = "white")
        quitButton.pack(side = "bottom", pady = 10)

# Student/Tutor Registration
class Registration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        RegistrationTitle = tk.Label(self, text="Registration", font = 22, bg = "white")
        RegistrationTitle.pack(padx = 10, pady = 10)

        StudentRegistrationButton = tk.Button(self, text="Student", command = lambda: controller.show_frame(StudentRegistration), bg = "white")
        StudentRegistrationButton.pack(side = "top", padx = 10, pady = 10)

        # TutorRegistrationButton = tk.Button(self, text="Student", command = lambda: controller.show_frame(TutorRegistration), bg = "white")
        # TutorRegistrationButton.pack(side = "top", padx = 10, pady = 10)

        backButton = tk.Button(self, text="Back", command = lambda: controller.show_frame(MainMenu), bg = "white")
        backButton.pack(side = "bottom", padx = 10, pady = 10)

# Student Registration
class StudentRegistration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        RegistrationTitle = tk.Label(self, text="Student Registration", font = 22, bg = "white")
        RegistrationTitle.pack(padx = 10, pady = 10)

        NameOfStudREGLabel = tk.Label(self, text = "Name", bg = "white")
        NameOfStudREGEntry = tk.Entry(self, width = 25, textvariable = NameOfStudREG)
        ConOfStudREGLabel = tk.Label(self, text = "Contact", bg = "white")
        ConOfStudREGEntry = tk.Entry(self, width = 25, textvariable = ConOfStudREG)
        EmConOfStudREGLabel = tk.Label(self, text = "Emergency Contact", bg = "white")
        EmConOfStudREGEntry = tk.Entry(self, width = 25, textvariable = EmConOfStudREG)
        SubOfStudREGLabel = tk.Label(self, text = "Subject", bg = "white")

        checkbuttonAddMath = tk.Checkbutton(self, text="Additional Mathematics", variable=AddMathREG, bg = "white")
        checkbuttonPhy = tk.Checkbutton(self, text="Physics", variable=PhyREG, bg = "white")
        checkbuttonChem = tk.Checkbutton(self, text="Chemistry", variable=ChemREG, bg = "white")

        NameOfStudREGLabel.pack(padx = 10, pady = 8)
        NameOfStudREGEntry.pack(padx = 10, pady = 8)
        ConOfStudREGLabel.pack(padx = 10, pady = 8)
        ConOfStudREGEntry.pack(padx = 10, pady = 8)
        EmConOfStudREGLabel.pack(padx = 10, pady = 8)
        EmConOfStudREGEntry.pack(padx = 10, pady = 8)
        SubOfStudREGLabel.pack(padx = 10, pady = 8)
        checkbuttonAddMath.pack(padx = 10, pady = 5)
        checkbuttonPhy.pack(padx = 10, pady = 5)
        checkbuttonChem.pack(padx = 10, pady = 5)

        saveButton = tk.Button(self, text="Save", command = lambda: self.registerstudent(), bg = "white")
        saveButton.pack(padx = 10, pady = 10)

        menuButton = tk.Button(self, text="Main Menu", command = lambda: controller.show_frame(MainMenu), bg = "white")
        menuButton.pack(side = "bottom", padx = 10, pady = 10)

        backButton = tk.Button(self, text="Back", command = lambda: controller.show_frame(Registration), bg = "white")
        backButton.pack(side = "bottom", padx = 10, pady = 10)

    def registerstudent(self):
        registerName = NameOfStudREG.get()
        registerCon = ConOfStudREG.get()
        registerEm = EmConOfStudREG.get()
        registerAddMath = AddMathREG.get()
        registerPhy = PhyREG.get()
        registerChem = ChemREG.get()
        registerFees = 0.0

        if (
            registerName == "" or registerCon == "" or
            registerEm == "" or
            (registerAddMath == 0 and registerPhy == 0 and
            registerChem == 0)
            ):
            # print "we not coo"
            #  Error if incomplete form
            errorINCOMP = tk.Toplevel(bg = "white")
            errorINCOMP.grab_set()
            errorINCOMP.title("Registration Error")
            errorINCOMP.geometry("250x100")
            errorINCOMP.resizable(False,False)

            errorINCOMPmsg = tk.Label(errorINCOMP, text = "Please complete the form!", bg = "white")
            errorINCOMPmsg.pack(padx = 10, pady = 10)

            dismissButton = tk.Button(errorINCOMP, text = "Dismiss", bg = "white", command = errorINCOMP.destroy)
            dismissButton.pack(padx = 10, pady = 10)

            self.wait_window(errorINCOMP)
            errorINCOMP.grab_release()

        else:
            # print "we coo"

            if registerAddMath == 1:
                registerFees += 55.0
                # print "addmath chosen"

            if registerPhy == 1:
                # print "physics chosen"
                registerFees += 40.0

            if registerChem == 1:
                # print "chemistry chosen"
                registerFees += 50.0

            registerOutFees = registerFees

            temp = dt.datetime.now()
            today = "%s/%s/%s" % (temp.day, temp.month, temp.year)

            registerDate = today

            registerInput = [registerName, registerCon, registerEm, str(registerFees), str(registerOutFees), today, ]

            if registerAddMath == 1:
                registerInput.append("Additional Mathematics")

            if registerPhy == 1:
                registerInput.append("Physics")

            if registerChem == 1:
                registerInput.append("Chemistry")

            studentREGDB = open("studentDB", "a+")

            for data in registerInput:
                studentREGDB.write(data + ", ")

            studentREGDB.write("\n")

            studentREGDB.close()

            # Display success student registration message
            successStudREG = tk.Toplevel(bg = "white")
            successStudREG.grab_set()
            successStudREG.title("Registration Successful")
            successStudREG.resizable(False,False)

            successStudREGmsg = tk.Label(successStudREG, text = "Student \"%s\" has been successfully registered!" % registerName, bg = "white")
            successStudREGmsg.pack(padx = 10, pady = 10)

            dismissButton = tk.Button(successStudREG, text = "Dismiss", bg = "white", command = successStudREG.destroy)
            dismissButton.pack(padx = 10, pady = 10)

            self.wait_window(successStudREG)
            successStudREG.grab_release()

            NameOfStudREG.set("")
            ConOfStudREG.set("")
            EmConOfStudREG.set("")
            AddMathREG.set("")
            PhyREG.set("")
            ChemREG.set("")

            self.controller.quit()

# Tutor Registration
# class TutorRegistration(tk.Frame):

# Student frame
class Student(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        TutorTitle = tk.Label(self, text="Student List", font = 22, bg = "white")
        TutorTitle.pack(padx = 10, pady = 10)

        # Opening database
        studentdb = open("studentdb", "r")
        temp = studentdb.readlines() # Temporary variable to store data read from database

        # To be accesed by "StudentDetail" class
        global StudentData
        global StudentName

        StudentData = [] # All the students including their data
        StudentName = [] # All of the students names only

        # Loop to split individual array for each student's data
        for i in range(len(temp)):
            StudentData.append(temp[i].replace("\n", " ").split(", "))

        self.student_list_box = tk.Listbox(self, bg = "white")

        # Appending student names from "StudentData" to "StudentName" as well as to listbox
        for i in range(len(StudentData)):
            StudentName.append(StudentData[i][0])
            self.student_list_box.insert("end", StudentData[i][0])

        self.student_list_box.pack(fill = "both")

        # Assign a method for mouse click
        self.student_list_box.bind('<<ListboxSelect>>', self.chooseNAME)

        backButton = tk.Button(self, text="Back", command = lambda: controller.show_frame(MainMenu), bg = "white")
        backButton.pack(side = "bottom", padx = 10, pady = 10)

    def chooseNAME(self, event) :
        # Get the selected/clicked name from the listbox and set it to the global variable TitleOfStud
        selected = self.student_list_box.get(self.student_list_box.curselection()[0])

        # Getting the index of the selected name
        for index in range(len(StudentName)):
            if StudentName[index] == selected:
                break

        # Individually set each of the details to the corresponding value from the StudentDate (with the help of index)
        NameOfStud.set("Name: %s" % StudentData[index][0])
        ConOfStud.set("Contact: %s" % StudentData[index][1])
        EmConOfStud.set("Emergency Contact: %s" % StudentData[index][2])
        FeeOfStud.set("Fees: %s" % StudentData[index][3])
        OutFeeOfStud.set("Outstanding Fees: %s" % StudentData[index][4])
        REGdateStud.set("Date registered: %s" % StudentData[index][5])

        # Checking if multiple subject present
        if len(StudentData[index]) == 10:
            SubOfStud.set("Subject: %s, %s, %s" % (StudentData[index][6].replace(",", ""), StudentData[index][7], StudentData[index][8]) )
        elif len(StudentData[index]) == 9:
            SubOfStud.set("Subject: %s, %s" % (StudentData[index][6], StudentData[index][7]))
        elif len(StudentData[index]) == 8:
            SubOfStud.set("Subject: %s" % StudentData[index][6])

        # Display the StudentDetail frame
        self.controller.show_frame(StudentDetail)

# Student Detail frame
class StudentDetail(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        DetailTitle = tk.Label(self, textvariable = NameOfStud, font = 22, bg = "white")
        DetailTitle.pack(padx = 10, pady = 10)

        Name = tk.Label(self, textvariable = NameOfStud, bg = "white")
        Contact = tk.Label(self, textvariable = ConOfStud, bg = "white")
        EContact = tk.Label(self, textvariable = EmConOfStud, bg = "white")
        Subject = tk.Label(self, textvariable = SubOfStud, bg = "white")
        TuitionFees = tk.Label(self, textvariable = FeeOfStud, bg = "white")
        Outstanding = tk.Label(self, textvariable = OutFeeOfStud, bg = "white")
        DateRegister = tk.Label(self, textvariable = REGdateStud, bg = "white")

        Name.pack(side = "top")
        Contact.pack(side = "top")
        EContact.pack(side = "top")
        Subject.pack(side = "top")
        TuitionFees.pack(side = "top")
        Outstanding.pack(side = "top")
        DateRegister.pack(side = "top")

        menuButton = tk.Button(self, text="Main Menu", command = lambda: controller.show_frame(MainMenu), bg = "white")
        menuButton.pack(side = "bottom", padx = 10, pady = 10)

        backButton = tk.Button(self, text="Back", command = lambda: controller.show_frame(Student), bg = "white")
        backButton.pack(side = "bottom", padx = 10, pady = 10)

if __name__ == "__main__":
    management = Management()
    management.mainloop()
