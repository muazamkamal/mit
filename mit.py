import Tkinter as tk

class Management(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Configuring windows properties
        self.title("M.I.T")
        self.geometry("480x480")
        self.resizable(False,False)

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

        # quit_button = tk.Button(self, text="Quit", command = quit, bg = "white")
        # quit_button.pack(side = "bottom")

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

        global StudentName # To be accesed by "StudentDetail" class
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

        self.student_list_box.pack()

        menu_button = tk.Button(self, text="Main Menu", command = lambda: controller.show_frame(MainMenu), bg = "white")
        menu_button.pack(side = "bottom", padx = 10, pady = 10)

        detail_button = tk.Button(self, text="Detail Page", command = lambda: controller.show_frame(StudentDetail), bg = "white")
        detail_button.pack(side = "bottom", padx = 10, pady = 10)

class StudentDetail(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        # Fetching selected value from listbox in "Student" frame
        student_page = self.controller.get_page(Student)
        NAMETOSEARCH = student_page.student_list_box.get("active")
        print NAMETOSEARCH
        # NAMETOSEARCH = "Shafiq"

        DetailTitle = tk.Label(self, text= NAMETOSEARCH, font = 14, bg = "white")
        DetailTitle.pack(padx = 10, pady = 10)

        #Checking index number
        for index in range(0, len(StudentName)):
            if StudentName[index] == NAMETOSEARCH:
                break

        Name = tk.Label(self, text="Name: " + StudentData[index][0], bg = "white")
        Contact = tk.Label(self, text="Contact: " + StudentData[index][1], bg = "white")
        EContact = tk.Label(self, text="Emergency Contact: " + StudentData[index][2], bg = "white")
        Subject = tk.Label(self, text="Subject: " + StudentData[index][3], bg = "white")
        TuitionFees = tk.Label(self, text="Tuition Fees: RM" + StudentData[index][4], bg = "white")
        Outstanding = tk.Label(self, text="Outstanding Fees: RM" + StudentData[index][5], bg = "white")

        Name.pack(side = "top")
        EContact.pack(side = "top")
        Contact.pack(side = "top")
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
