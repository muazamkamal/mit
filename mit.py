import Tkinter as tk

class Management(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Configuring windows properties
        self.title("M.I.T")
        self.geometry("480x480")
        self.resizable(False,False)

        #Variables of all the details for StudentDetail frame
        global TitleOfStud
        global NameOfStud
        global ConOfStud
        global EmConOfStud
        global SubOfStud
        global FeeOfStud
        global OutFeeOfStud

        TitleOfStud = tk.StringVar()
        NameOfStud = tk.StringVar()
        ConOfStud = tk.StringVar()
        EmConOfStud = tk.StringVar()
        SubOfStud = tk.StringVar()
        FeeOfStud = tk.StringVar()
        OutFeeOfStud = tk.StringVar()

        # Setting up frames or pages
        global container
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # Layering the frames and bringing up "MainMenu" to the top
        self.frames = {}

        for F in (MainMenu, Student, StudentDetail):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(MainMenu)

    # Method for bringing up specific frames based on argument.
    def show_frame(self, cont):

        # Refreshing/reloading the called frame before bringing it up
        for F in (MainMenu, Student, StudentDetail):
            if cont == F:
                F(container, self)

        frame = self.frames[cont]
        frame.tkraise()

    # Method for getting variables between frames
    def get_page(self, classname):

        return self.frames[classname]

# MainMenu frame
class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        MenuTitle = tk.Label(self, text="Main Menu", font = 14, bg = "white")
        MenuTitle.pack(padx = 10, pady = 10)

        tutor_button = tk.Button(self, text="Student", command = lambda: controller.show_frame(Student), bg = "white")
        tutor_button.place(relx = 0.5, rely = 0.5, anchor = "center")

        quit_button = tk.Button(self, text="Quit", command = lambda: quit(), bg = "white")
        quit_button.pack(side = "bottom", pady = 10)

# Student frame
class Student(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        TutorTitle = tk.Label(self, text="Student List", font = 14, bg = "white")
        TutorTitle.pack(padx = 10, pady = 10)

        # Opening database
        studentdb = open("testdb", "r")
        temp = studentdb.readlines() # Temporary variable to store data read from database

        # To be accesed by "StudentDetail" class
        global StudentData
        global StudentName

        StudentData = [] # All the students including their data
        StudentName = [] # All of the students names only

        # Loop to split individual array for each student's data
        for i in range(0, len(temp)):
            StudentData.append(temp[i].replace("\n", " ").split(", "))

        self.student_list_box = tk.Listbox(self, bg = "white")

        # Appending student names from "StudentData" to "StudentName" as well as to listbox
        for i in range(0, len(StudentData)):
            StudentName.append(StudentData[i][0])
            self.student_list_box.insert("end", StudentData[i][0])

        self.student_list_box.pack(fill = "both")

        # Assign a method for mouse click
        self.student_list_box.bind('<<ListboxSelect>>', self.chooseNAME)

        menu_button = tk.Button(self, text="Main Menu", command = lambda: controller.show_frame(MainMenu), bg = "white")
        menu_button.pack(side = "bottom", padx = 10, pady = 10)

    def chooseNAME(self, event) :
        # Get the selected/clicked name from the listbox and set it to the global variable TitleOfStud
        selected = self.student_list_box.get(self.student_list_box.curselection()[0])
        TitleOfStud.set(selected)

        # Getting the index of the selected name
        for index in range(0, len(StudentName)):
            if StudentName[index] == selected:
                break

        # Individually set each of the details to the corresponding value from the StudentDate (with the help of index)
        NameOfStud.set("Name: %s" % StudentData[index][0])
        ConOfStud.set("Contact: %s" % StudentData[index][1])
        EmConOfStud.set("Emergency Contact: %s" % StudentData[index][2])
        SubOfStud.set("Subject: %s" % StudentData[index][3])
        FeeOfStud.set("Fees: %s" % StudentData[index][4])
        OutFeeOfStud.set("Outstanding Fees: %s" % StudentData[index][5])

        # Display the StudentDetail frame
        self.controller.show_frame(StudentDetail)


class StudentDetail(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        DetailTitle = tk.Label(self, textvariable = TitleOfStud, font = 14, bg = "white")
        DetailTitle.pack(padx = 10, pady = 10)

        Name = tk.Label(self, textvariable = NameOfStud, bg = "white")
        Contact = tk.Label(self, textvariable = ConOfStud, bg = "white")
        EContact = tk.Label(self, textvariable = EmConOfStud, bg = "white")
        Subject = tk.Label(self, textvariable = SubOfStud, bg = "white")
        TuitionFees = tk.Label(self, textvariable = FeeOfStud, bg = "white")
        Outstanding = tk.Label(self, textvariable = OutFeeOfStud, bg = "white")

        Name.pack(side = "top")
        Contact.pack(side = "top")
        EContact.pack(side = "top")
        Subject.pack(side = "top")
        TuitionFees.pack(side = "top")
        Outstanding.pack(side = "top")

        menu_button = tk.Button(self, text="Main Menu", command = lambda: controller.show_frame(MainMenu), bg = "white")
        menu_button.pack(side = "bottom", padx = 10, pady = 10)

        back_button = tk.Button(self, text="Back", command = lambda: controller.show_frame(Student), bg = "white")
        back_button.pack(side = "bottom", padx = 10, pady = 10)

if __name__ == "__main__":
    management = Management()
    management.mainloop()
