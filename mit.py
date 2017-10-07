import Tkinter as tk
import datetime as dt

# Create database if it doesn't exist
def checkDB(dbname):
    try:
        open(dbname, "r")
    except IOError:
        temp = open(dbname, "w")
        temp.close()

class Management(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Configuring windows properties
        self.title("M.I.T")
        self.geometry("640x550")
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

        global payment
        global salary

        payment = tk.IntVar()
        salary = tk.IntVar()

        global NameOfTutorREG
        global ConOfTutorREG
        global EmConOfTutorREG
        global TAddMathREG
        global TPhyREG
        global TChemREG

        NameOfTutorREG = tk.StringVar()
        ConOfTutorREG = tk.StringVar()
        EmConOfTutorREG = tk.StringVar()
        TAddMathREG = tk.IntVar()
        TPhyREG = tk.IntVar()
        TChemREG = tk.IntVar()

        global NameOfTutor
        global ConOfTutor
        global EmConOfTutor
        global SubOfTutor
        global FeeOfTutor
        global OutFeeOfTutor
        global REGdateTutor

        NameOfTutor = tk.StringVar()
        ConOfTutor = tk.StringVar()
        EmConOfTutor = tk.StringVar()
        SubOfTutor = tk.StringVar()
        FeeOfTutor = tk.StringVar()
        OutFeeOfTutor = tk.StringVar()
        REGdateTutor = tk.StringVar()

        # Setting up frames or pages
        global container
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # Layering the frames and bringing up "MainMenu" to the top
        self.frames = {}

        for F in (Welcome, Login, Signup, MainMenu, Registration, StudentRegistration, Student, StudentDetail, TutorRegistration, Tutor, TutorDetail):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(Welcome)

    # Method for bringing up specific frames based on argument.
    def show_frame(self, cont):

        # Refreshing/reloading the called frame before bringing it up
        for F in (Welcome, Login, Signup, MainMenu, Registration, StudentRegistration, StudentDetail, TutorRegistration, TutorDetail):
            if cont == F:
                F(container, self)

        frame = self.frames[cont]
        frame.tkraise()

    # Method for getting variables between frames
    def get_page(self, classname):
        return self.frames[classname]

class Welcome(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        WelcomeTitle = tk.Label(self, text="Welcome!", font = 22, bg = "white")
        WelcomeTitle.pack(padx = 10, pady = 10)

        loginButton = tk.Button(self, text="Login", command = lambda: controller.show_frame(Login), bg = "white")
        loginButton.pack(side = "top", padx = 10, pady = 10)

        registerButton = tk.Button(self, text="Sign Up", command = lambda: controller.show_frame(Signup), bg = "white")
        registerButton.pack(side = "top", padx = 10, pady = 10)

        testButton = tk.Button(self, text="Developer's Mode", command = lambda: controller.show_frame(MainMenu), bg = "white")
        testButton.pack(side = "top", padx = 10, pady = 10)

        quitButton = tk.Button(self, text="Quit", command = lambda: quit(), bg = "white")
        quitButton.pack(side = "bottom", pady = 10)

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
            checkDB("credentialDB.txt")
            creds = open("credentialDB.txt", "r")
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

                errorDBmsg = tk.Label(errorDB, text = "Database empty! Please register first!", bg = "white")
                errorDBmsg.pack(padx = 10, pady = 10)

                dismissButton = tk.Button(errorDB, text = "Dismiss", bg = "white", command = errorDB.destroy)
                dismissButton.pack(padx = 10, pady = 10)

                self.wait_window(errorDB)
                errorDB.grab_release()

                usrnm.set("")
                pswd.set("")

class Signup(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        SignupTitle = tk.Label(self, text="Sign Up", font = 22, bg = "white")
        SignupTitle.pack(padx = 10, pady = 10)

        usernameREGLabel = tk.Label(self, text = "Username", bg = "white")
        usernameREGEntry = tk.Entry(self, width = 25, textvariable = usrnmREG)
        passwordREGLabel = tk.Label(self, text = "Password", bg = "white")
        passwordREGEntry = tk.Entry(self, show = "*", width = 25, textvariable = pswdREG)

        usernameREGLabel.pack()
        usernameREGEntry.pack()
        passwordREGLabel.pack()
        passwordREGEntry.pack()

        signupButton = tk.Button(self, text="Signup", command = lambda: self.signup(), bg = "white")
        signupButton.pack(padx = 10, pady = 10)

        backButton = tk.Button(self, text="Back", command = lambda: controller.show_frame(Welcome), bg = "white")
        backButton.pack(side = "bottom", padx = 10, pady = 10)

    def signup(self):
        signupUsrnm = usrnmREG.get()
        signupPswd = pswdREG.get()

        if signupUsrnm == "" or signupPswd == "":
            # Error if no username/password entered by user
            errorREG = tk.Toplevel(bg = "white")
            errorREG.grab_set()
            errorREG.title("Sign up Error")
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
            creds=open("credentialDB.txt","a+")
            datatowrite=[signupUsrnm,signupPswd]
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

            successREGmsg = tk.Label(successREG, text = "Username \"%s\" has been successfully registered!" % signupUsrnm, bg = "white")
            successREGmsg.pack(padx = 10, pady = 10)

            dismissButton = tk.Button(successREG, text = "Dismiss", bg = "white", command = successREG.destroy)
            dismissButton.pack(padx = 10, pady = 10)

            self.wait_window(successREG)
            successREG.grab_release()

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

        studentButton = tk.Button(self, text="Tutor", command = lambda: controller.show_frame(Tutor), bg = "white")
        studentButton.pack(padx = 10, pady = 10)

        quitButton = tk.Button(self, text="Quit", command = lambda: quit(), bg = "white")
        quitButton.pack(side = "bottom", pady = 10)

class Registration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        RegistrationTitle = tk.Label(self, text="Registration", font = 22, bg = "white")
        RegistrationTitle.pack(padx = 10, pady = 10)

        StudentRegistrationButton = tk.Button(self, text="Student", command = lambda: controller.show_frame(StudentRegistration), bg = "white")
        StudentRegistrationButton.pack(side = "top", padx = 10, pady = 10)


        TutorRegistrationButton = tk.Button(self, text="Tutor", command = lambda: controller.show_frame(TutorRegistration), bg = "white")
        TutorRegistrationButton.pack(side = "top", padx = 10, pady = 10)

        backButton = tk.Button(self, text="Back", command = lambda: controller.show_frame(MainMenu), bg = "white")
        backButton.pack(side = "bottom", padx = 10, pady = 10)

class StudentRegistration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        RegistrationTitle = tk.Label(self, text="Student Registration", font = 22, bg = "white")
        RegistrationTitle.pack(padx = 10, pady = 10)

        NameOfStudREGLabel = tk.Label(self, text = " Full Name", bg = "white")
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

        backButton = tk.Button(self, text="Back", command = lambda: controller.show_frame(Registration), bg = "white")
        backButton.pack(side = "bottom", padx = 10, pady = 10)

        menuButton = tk.Button(self, text="Main Menu", command = lambda: controller.show_frame(MainMenu), bg = "white")
        menuButton.pack(side = "bottom", padx = 10, pady = 10)

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

            StudentMonthPaid= str(temp.month)
            StudentYearPaid = str(temp.year)

            registerInput = [registerName, registerCon, registerEm, str(registerFees), str(registerOutFees), today, StudentMonthPaid, StudentYearPaid]

            if registerAddMath == 1:
                registerInput.append("Additional Mathematics")

            if registerPhy == 1:
                registerInput.append("Physics")

            if registerChem == 1:
                registerInput.append("Chemistry")

            studentREGDB = open("studentDB.txt", "a+")

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
            AddMathREG.set(0)
            PhyREG.set(0)
            ChemREG.set(0)

            student_list_box.insert("end", registerName)

class TutorRegistration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        RegistrationTitle = tk.Label(self, text=" Tutor Registration", font = 22, bg = "white")
        RegistrationTitle.pack(padx = 10, pady = 10)

        NameOfTutorREGLabel = tk.Label(self, text = " Full Name", bg = "white")
        NameOfTutorREGEntry = tk.Entry(self, width = 25, textvariable = NameOfTutorREG)
        ConOfTutorREGLabel = tk.Label(self, text = "Contact", bg = "white")
        ConOfTutorREGEntry = tk.Entry(self, width = 25, textvariable = ConOfTutorREG)
        EmConOfTutorREGLabel = tk.Label(self, text = "Emergency Contact", bg = "white")
        EmConOfTutorREGEntry = tk.Entry(self, width = 25, textvariable = EmConOfTutorREG)
        SubOfTutorREGLabel = tk.Label(self, text = "Teaching Subject", bg = "white")

        checkbuttonTAddMath = tk.Checkbutton(self, text="Additional Mathematics", variable=TAddMathREG, bg = "white")
        checkbuttonTPhy = tk.Checkbutton(self, text="Physics", variable=TPhyREG, bg = "white")
        checkbuttonTChem = tk.Checkbutton(self, text="Chemistry", variable=TChemREG, bg = "white")

        NameOfTutorREGLabel.pack(padx = 10, pady = 8)
        NameOfTutorREGEntry.pack(padx = 10, pady = 8)
        ConOfTutorREGLabel.pack(padx = 10, pady = 8)
        ConOfTutorREGEntry.pack(padx = 10, pady = 8)
        EmConOfTutorREGLabel.pack(padx = 10, pady = 8)
        EmConOfTutorREGEntry.pack(padx = 10, pady = 8)
        SubOfTutorREGLabel.pack(padx = 10, pady = 8)
        checkbuttonTAddMath.pack(padx = 10, pady = 5)
        checkbuttonTPhy.pack(padx = 10, pady = 5)
        checkbuttonTChem.pack(padx = 10, pady = 5)

        saveButton = tk.Button(self, text="Save", command = lambda: self.registertutor(), bg = "white")
        saveButton.pack(padx = 10, pady = 10)

        backButton = tk.Button(self, text="Back", command = lambda: controller.show_frame(Registration), bg = "white")
        backButton.pack(side = "bottom", padx = 10, pady = 10)

        menuButton = tk.Button(self, text="Main Menu", command = lambda: controller.show_frame(MainMenu), bg = "white")
        menuButton.pack(side = "bottom", padx = 10, pady = 10)

    def registertutor(self):
        registerName = NameOfTutorREG.get()
        registerCon = ConOfTutorREG.get()
        registerEm = EmConOfTutorREG.get()
        registerTAddMath = TAddMathREG.get()
        registerTPhy = TPhyREG.get()
        registerTChem = TChemREG.get()
        Salary = 0.0

        if (
            registerName == "" or registerCon == "" or
            registerEm == "" or
            (registerTAddMath == 0 and registerTPhy == 0 and
            registerTChem == 0)
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

            if registerTAddMath == 1:
                Salary += 350.0
                # print "addmath chosen"

            if registerTPhy == 1:
                # print "physics chosen"
                Salary += 340.0

            if registerTChem == 1:
                # print "chemistry chosen"
                Salary += 355.0

            OutstandingSalary = Salary

            temp = dt.datetime.now()
            today = "%s/%s/%s" % (temp.day, temp.month, temp.year)

            registerDate = today

            TutorMonthPaid= str(temp.month)
            TutorYearPaid = str(temp.year)

            registerInput = [registerName, registerCon, registerEm, str(Salary), str(OutstandingSalary), today, TutorMonthPaid, TutorYearPaid, ]

            if registerTAddMath == 1:
                registerInput.append("Additional Mathematics")

            if registerTPhy == 1:
                registerInput.append("Physics")

            if registerTChem == 1:
                registerInput.append("Chemistry")

            tutorREGDB = open("tutorDB.txt", "a+")

            for data in registerInput:
                tutorREGDB.write(data + ", ")

            tutorREGDB.write("\n")

            tutorREGDB.close()

            # Display success student registration message
            successTutorREG = tk.Toplevel(bg = "white")
            successTutorREG.grab_set()
            successTutorREG.title("Registration Successful")
            successTutorREG.resizable(False,False)

            successTutorREGmsg = tk.Label(successTutorREG, text = "Tutor \"%s\" has been successfully registered!" % registerName, bg = "white")
            successTutorREGmsg.pack(padx = 10, pady = 10)

            dismissButton = tk.Button(successTutorREG, text = "Dismiss", bg = "white", command = successTutorREG.destroy)
            dismissButton.pack(padx = 10, pady = 10)

            self.wait_window(successTutorREG)
            successTutorREG.grab_release()

            NameOfTutorREG.set("")
            ConOfTutorREG.set("")
            EmConOfTutorREG.set("")
            TAddMathREG.set(0)
            TPhyREG.set(0)
            TChemREG.set(0)

            tutor_list_box.insert("end", registerName)

class Student(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        StudentTitle = tk.Label(self, text="Student List", font = 22, bg = "white")
        StudentTitle.pack(padx = 10, pady = 10)

        # Opening database
        checkDB("studentDB.txt")
        studentdb = open("studentDB.txt", "r")
        temp = studentdb.readlines() # Temporary variable to store data read from database

        # To be accesed by "StudentDetail" class
        global StudentData
        global StudentName

        StudentData = [] # All the students including their data
        StudentName = [] # All of the students names only

        # Loop to split individual array for each student's data
        for i in range(len(temp)):
            StudentData.append(temp[i].replace("\n", " ").split(", "))

        global student_list_box

        student_list_box = tk.Listbox(self, bg = "white")

        # Appending student names from "StudentData" to "StudentName" as well as to listbox
        j = 0
        while j < len(StudentData):
            StudentName.append(StudentData[j][0])
            student_list_box.insert("end", StudentData[j][0])

            j += 1

        studentdb.close()

        student_list_box.pack(fill = "both")

        # Assign a method for mouse click
        student_list_box.bind('<<ListboxSelect>>', self.chooseNAME)

        backButton = tk.Button(self, text="Back", command = lambda: controller.show_frame(MainMenu), bg = "white")
        backButton.pack(side = "bottom", padx = 10, pady = 10)

        menuButton = tk.Button(self, text="Main Menu", command = lambda: controller.show_frame(MainMenu), bg = "white")
        menuButton.pack(side = "bottom", padx = 10, pady = 10)

    def chooseNAME(self, event) :
        # Get the selected/clicked name from the listbox
        SearchStudent = student_list_box.get(event.widget.curselection()[0])

        # Opening database
        checkDB("studentDB.txt")
        studentdb = open("studentDB.txt", "r")
        temp = studentdb.readlines() # Temporary variable to store data read from database

        StudentData = [] # All the students including their data
        StudentName = [] # All of the students names only

        # Loop to split individual array for each student's data
        for i in range(len(temp)):
            StudentData.append(temp[i].replace("\n", " ").split(", "))

        # Appending student names from "StudentData" to "StudentName" as well as to listbox
        j = 0
        while j < len(StudentData):
            StudentName.append(StudentData[j][0])

            j += 1

        studentdb.close()

        # Getting the index of the selected name
        global index
        index = -1

        while True:
            index += 1

            if StudentName[index] == SearchStudent:
                break

        # Individually set each of the details to the corresponding value from the StudentDate (with the help of index)
        NameOfStud.set("Name: %s" % StudentData[index][0])
        ConOfStud.set("Contact: %s" % StudentData[index][1])
        EmConOfStud.set("Emergency Contact: %s" % StudentData[index][2])
        FeeOfStud.set("Fees: RM%s" % StudentData[index][3])
        OutFeeOfStud.set("Outstanding Fees: RM%s" % StudentData[index][4])
        REGdateStud.set("Date registered: %s" % StudentData[index][5])

        # Checking if multiple subject present
        if len(StudentData[index]) == 12:
            SubOfStud.set("Subject: %s, %s, %s" % (StudentData[index][8].replace(",", ""), StudentData[index][9], StudentData[index][10]) )
        elif len(StudentData[index]) == 11:
            SubOfStud.set("Subject: %s, %s" % (StudentData[index][8], StudentData[index][9]))
        elif len(StudentData[index]) == 10:
            SubOfStud.set("Subject: %s" % StudentData[index][8])

        # Display the StudentDetail frame
        self.controller.show_frame(StudentDetail)

class StudentDetail(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        DetailTitle = tk.Label(self, text = "Student's Details", font = 22, bg = "white")
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

        PaymentButton = tk.Button(self, text="Payment", command = lambda: self.paymentpage(), bg = "white")
        PaymentButton.pack(padx = 10, pady = 10)

        backButton = tk.Button(self, text="Back", command = lambda: controller.show_frame(Student), bg = "white")
        backButton.pack(side = "bottom", padx = 10, pady = 10)

        menuButton = tk.Button(self, text="Main Menu", command = lambda: controller.show_frame(MainMenu), bg = "white")
        menuButton.pack(side = "bottom", padx = 10, pady = 10)

        deleteButton = tk.Button(self, text="Delete Student", command = lambda: self.confirmdel(), bg = "white")
        deleteButton.pack(side = "bottom", padx = 10, pady = 10)

    def paymentpage(self):
        # Display payment
        paymentwindow = tk.Toplevel(bg = "white")
        paymentwindow.grab_set()
        paymentwindow.title("Payment")
        paymentwindow.resizable(False,False)

        # Opening database
        checkDB("studentDB.txt")
        studentdb = open("studentDB.txt", "r")
        temp = studentdb.readlines() # Temporary variable to store data read from database

        StudentData = [] # All the students including their data
        StudentName = [] # All of the students names only

        # Loop to split individual array for each student's data
        for i in range(len(temp)):
            StudentData.append(temp[i].replace("\n", " ").split(", "))

        # Appending student names from "StudentData" to "StudentName" as well as to listbox
        j = 0
        while j < len(StudentData):
            StudentName.append(StudentData[j][0])

            j += 1

        studentdb.close()

        OutstandingMonths = float(StudentData[index][4])/ float(StudentData[index][3])

        Outstanding = tk.Label(paymentwindow, textvariable = OutFeeOfStud, bg = "white")
        Outstanding.pack(side = "top")

        OutMsg = tk.Label(paymentwindow, text ="This student has outstanding fees for %d months !" % OutstandingMonths, bg = "white")
        OutMsg.pack(padx = 10, pady = 8)

        def pay():
            StudentData[index][4] = float(StudentData[index][4])- float(payment.get())

            Balance = tk.Label(paymentwindow, text ="The outstanding balance for this student is RM%.2f " % StudentData[index][4], bg = "white")
            Balance.pack(padx = 10, pady = 8)

            paydate = dt.datetime.now()
            StudentData[index][6] = str(paydate.month)

            studentdb = open("studentDB.txt", "w")
            for i in range(len(StudentData)):
                for j in range(len(StudentData[i]) - 1):
                    studentdb.write(str(StudentData[i][j]) + ", ")

                studentdb.write("\n")

            studentdb.close()

            payment.set("")

            OutFeeOfStud.set("Outstanding Fees: RM%s" % StudentData[index][4])

            quitButton = tk.Button(paymentwindow, text="Done", command = paymentwindow.destroy, bg = "white")
            quitButton.pack(side = "bottom", padx = 10, pady = 10)

        if StudentData[index][4] != "0.0":
            paymentLabel = tk.Label(paymentwindow, text = "Payment", bg = "white")
            paymentLabel.pack(padx = 10, pady = 8)

            paymentEntry = tk.Entry(paymentwindow, width = 10, textvariable = payment)
            paymentEntry.pack(padx = 10, pady = 8)

            payButton = tk.Button(paymentwindow, text = "Pay", command = pay, bg = "white"  )
            payButton.pack(side = "bottom", padx = 10, pady = 10)

        self.wait_window(paymentwindow)
        paymentwindow.grab_release()
        # self.controller.quit()

    # Student delete
    def confirmdel(self):
        confirmationDEL = tk.Toplevel(bg = "white")
        confirmationDEL.grab_set()
        confirmationDEL.title("Are you sure?")
        confirmationDEL.resizable(False,False)

        # Opening database
        checkDB("studentDB.txt")
        studentdb = open("studentDB.txt", "r")
        temp = studentdb.readlines() # Temporary variable to store data read from database

        StudentData = [] # All the students including their data
        StudentName = [] # All of the students names only

        # Loop to split individual array for each student's data
        for i in range(len(temp)):
            StudentData.append(temp[i].replace("\n", " ").split(", "))

        # Appending student names from "StudentData" to "StudentName" as well as to listbox
        j = 0
        while j < len(StudentData):
            StudentName.append(StudentData[j][0])

            j += 1

        studentdb.close()

        def delete():
            studentdb = open("studentDB.txt", "w")

            for i in range(len(StudentData)):
                if StudentData[i][0] != StudentData[index][0]:
                    for j in range(len(StudentData[i]) - 1):
                        studentdb.write(str(StudentData[i][j]) + ", ")

                    studentdb.write("\n")

            studentdb.close()

            student_list_box.delete(student_list_box.curselection())

            confirmationDEL.destroy()

            self.controller.show_frame(Student)

        sure = tk.Label(confirmationDEL, text="Are you sure you want to delete this student?", bg = "white", font = 16)
        yesButton = tk.Button(confirmationDEL, text="Yes", bg = "white", command = lambda: delete())
        noButton = tk.Button(confirmationDEL, text="No", bg = "white", command = lambda: confirmationDEL.destroy())

        sure.pack()
        yesButton.pack(padx = 10, pady = 10)
        noButton.pack(padx = 10, pady = 10)

class Tutor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        TutorTitle = tk.Label(self, text="Tutor List", font = 22, bg = "white")
        TutorTitle.pack(padx = 10, pady = 10)

        # Opening database
        checkDB("tutorDB.txt")
        tutordb = open("tutorDB.txt", "r")
        temp = tutordb.readlines() # Temporary variable to store data read from database

        # To be accesed by "StudentDetail" class
        global TutorData
        global TutorName

        TutorData = [] # All the students including their data
        TutorName = [] # All of the students names only

        # Loop to split individual array for each student's data
        for i in range(len(temp)):
            TutorData.append(temp[i].replace("\n", " ").split(", "))

        global tutor_list_box

        tutor_list_box = tk.Listbox(self, bg = "white")

        # Appending student names from "StudentData" to "StudentName" as well as to listbox
        j = 0
        while j < len(TutorData):
            TutorName.append(TutorData[j][0])
            tutor_list_box.insert("end", TutorData[j][0])

            j += 1

        tutordb.close()

        tutor_list_box.pack(fill = "both")

        # Assign a method for mouse click
        tutor_list_box.bind('<<ListboxSelect>>', self.chooseNAME)

        backButton = tk.Button(self, text="Back", command = lambda: controller.show_frame(MainMenu), bg = "white")
        backButton.pack(side = "bottom", padx = 10, pady = 10)

        menuButton = tk.Button(self, text="Main Menu", command = lambda: controller.show_frame(MainMenu), bg = "white")
        menuButton.pack(side = "bottom", padx = 10, pady = 10)

    def chooseNAME(self, event) :
        # Get the selected/clicked name from the listbox and set it to the global variable TitleOfStud
        SearchTutor = tutor_list_box.get(event.widget.curselection()[0])

        # Opening database
        checkDB("tutorDB.txt")
        tutordb = open("tutorDB.txt", "r")
        temp = tutordb.readlines() # Temporary variable to store data read from database

        TutorData = [] # All the students including their data
        TutorName = [] # All of the students names only

        # Loop to split individual array for each student's data
        for i in range(len(temp)):
            TutorData.append(temp[i].replace("\n", " ").split(", "))

        # Appending student names from "StudentData" to "StudentName" as well as to listbox
        j = 0
        while j < len(TutorData):
            TutorName.append(TutorData[j][0])

            j += 1

        tutordb.close()

        # Getting the index of the selected name
        global counter
        counter = -1

        while True:
            counter += 1
            if TutorName[counter] == SearchTutor:
                break

        # Individually set each of the details to the corresponding value from the StudentDate (with the help of index)
        NameOfTutor.set("Name: %s" % TutorData[counter][0])
        ConOfTutor.set("Contact: %s" % TutorData[counter][1])
        EmConOfTutor.set("Emergency Contact: %s" % TutorData[counter][2])
        FeeOfTutor.set("Salary : RM%s" % TutorData[counter][3])
        OutFeeOfTutor.set("Outstanding Salary: RM%s" % TutorData[counter][4])
        REGdateTutor.set("Date registered: %s" % TutorData[counter][5])

        # Checking if multiple subject present
        if len(TutorData[counter]) == 12:
            SubOfTutor.set("Subject: %s, %s, %s" % (TutorData[counter][8].replace(",", ""), TutorData[counter][9], TutorData[counter][10]) )
        elif len(TutorData[counter]) == 11:
            SubOfTutor.set("Subject: %s, %s" % (TutorData[counter][8], TutorData[counter][7]))
        elif len(TutorData[counter]) == 10:
            SubOfTutor.set("Subject: %s" % TutorData[counter][8])

        # Display the StudentDetail frame
        self.controller.show_frame(TutorDetail)

class TutorDetail(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        DetailTitle = tk.Label(self, text = "Tutor's Details", font = 22, bg = "white")
        DetailTitle.pack(padx = 10, pady = 10)

        Name = tk.Label(self, textvariable = NameOfTutor, bg = "white")
        Contact = tk.Label(self, textvariable = ConOfTutor, bg = "white")
        EContact = tk.Label(self, textvariable = EmConOfTutor, bg = "white")
        Subject = tk.Label(self, textvariable = SubOfTutor, bg = "white")
        TuitionFees = tk.Label(self, textvariable = FeeOfTutor, bg = "white")
        Outstanding = tk.Label(self, textvariable = OutFeeOfTutor, bg = "white")
        DateRegister = tk.Label(self, textvariable = REGdateTutor, bg = "white")

        Name.pack(side = "top")
        Contact.pack(side = "top")
        EContact.pack(side = "top")
        Subject.pack(side = "top")
        TuitionFees.pack(side = "top")
        Outstanding.pack(side = "top")
        DateRegister.pack(side = "top")


        SalaryButton = tk.Button(self, text="Salary", command = lambda: self.salarypage(), bg = "white")
        SalaryButton.pack(padx = 10, pady = 10)

        backButton = tk.Button(self, text="Back", command = lambda: controller.show_frame(Tutor), bg = "white")
        backButton.pack(side = "bottom", padx = 10, pady = 10)

        menuButton = tk.Button(self, text="Main Menu", command = lambda: controller.show_frame(MainMenu), bg = "white")
        menuButton.pack(side = "bottom", padx = 10, pady = 10)

        deleteButton = tk.Button(self, text="Delete Tutor", command = lambda: self.confirmdel(), bg = "white")
        deleteButton.pack(side = "bottom", padx = 10, pady = 10)


    def salarypage(self):
        # Display salary
        salarywindow = tk.Toplevel(bg = "white")
        salarywindow.grab_set()
        salarywindow.title("Salary")
        salarywindow.resizable(False,False)

        # Opening database
        checkDB("tutorDB.txt")
        tutordb = open("tutorDB.txt", "r")
        temp = tutordb.readlines() # Temporary variable to store data read from database

        TutorData = [] # All the students including their data
        TutorName = [] # All of the students names only

        # Loop to split individual array for each student's data
        for i in range(len(temp)):
            TutorData.append(temp[i].replace("\n", " ").split(", "))

        # Appending student names from "StudentData" to "StudentName" as well as to listbox
        j = 0
        while j < len(TutorData):
            TutorName.append(TutorData[j][0])

            j += 1

        tutordb.close()

        OutstandingMonths = float(TutorData[counter][4])/ float(TutorData[counter][3])

        Outstanding = tk.Label(salarywindow, textvariable = OutFeeOfTutor, bg = "white")
        Outstanding.pack(side = "top")

        OutMsg = tk.Label(salarywindow, text ="This tutor has outstanding salary for %d months !" % OutstandingMonths, bg = "white")
        OutMsg.pack(padx = 10, pady = 8)

        def pay():
            TutorData[counter][4] = float(TutorData[counter][4])- float(salary.get())

            Balance = tk.Label(salarywindow, text ="The outstanding balance for this tutor is RM%.2f " % TutorData[counter][4], bg = "white")
            Balance.pack(padx = 10, pady = 8)

            paydate = dt.datetime.now()
            TutorData[counter][6] = str(paydate.month)

            tutordb = open("tutorDB.txt", "w")
            for i in range(len(TutorData)):
                for j in range(len(TutorData[i]) - 1):
                    tutordb.write(str(TutorData[i][j]) + ", ")

                tutordb.write("\n")

            tutordb.close()

            salary.set("")

            OutFeeOfTutor.set("Outstanding Fees: RM%s" % TutorData[counter][4])

            quitButton = tk.Button(salarywindow, text="Done", command = salarywindow.destroy, bg = "white")
            quitButton.pack(side = "bottom", padx = 10, pady = 10)

        if TutorData[counter][4] != "0.0":
            paymentLabel = tk.Label(salarywindow, text = "Payment", bg = "white")
            paymentLabel.pack(padx = 10, pady = 8)

            paymentEntry = tk.Entry(salarywindow, width = 10, textvariable = salary)
            paymentEntry.pack(padx = 10, pady = 8)

            payButton = tk.Button(salarywindow, text = "Pay", command = pay, bg = "white"  )
            payButton.pack(side = "bottom", padx = 10, pady = 10)

        salary.set("")
        self.wait_window(salarywindow)
        salarywindow.grab_release()
        # self.controller.quit()

    # Student delete
    def confirmdel(self):
        confirmationDEL = tk.Toplevel(bg = "white")
        confirmationDEL.grab_set()
        confirmationDEL.title("Are you sure?")
        confirmationDEL.resizable(False,False)

        # Opening database
        checkDB("tutorDB.txt")
        tutordb = open("tutorDB.txt", "r")
        temp = tutordb.readlines() # Temporary variable to store data read from database

        TutorData = [] # All the students including their data
        TutorName = [] # All of the students names only

        # Loop to split individual array for each student's data
        for i in range(len(temp)):
            TutorData.append(temp[i].replace("\n", " ").split(", "))

        # Appending student names from "StudentData" to "StudentName" as well as to listbox
        j = 0
        while j < len(TutorData):
            TutorName.append(TutorData[j][0])

            j += 1

        tutordb.close()

        def delete():
            tutordb = open("tutorDB.txt", "w")

            for i in range(len(TutorData)):
                if TutorData[i][0] != TutorData[counter][0]:
                    for j in range(len(TutorData[i]) - 1):
                        tutordb.write(str(TutorData[i][j]) + ", ")

                    tutordb.write("\n")

            tutordb.close()

            tutor_list_box.delete(tutor_list_box.curselection())

            confirmationDEL.destroy()

            self.controller.show_frame(Tutor)

        sure = tk.Label(confirmationDEL, text="Are you sure you want to delete this tutor?", bg = "white", font = 16)
        yesButton = tk.Button(confirmationDEL, text="Yes", bg = "white", command = lambda: delete())
        noButton = tk.Button(confirmationDEL, text="No", bg = "white", command = lambda: confirmationDEL.destroy())

        sure.pack()
        yesButton.pack(padx = 10, pady = 10)
        noButton.pack(padx = 10, pady = 10)

if __name__ == "__main__":
    management = Management()
    management.mainloop()
