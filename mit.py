import Tkinter as tk



class Management(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("M.I.T")
        self.geometry("480x480")
        self.resizable(False,False)

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (MainMenu, Tutor, TutorDetail):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(MainMenu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, classname):
        # for page in self.frames.values():
        #     if str(page.__class__.__name__) == classname:
        #         return page

        return self.frames[classname]

class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        MenuTitle = tk.Label(self, text="Main Menu", font = 14, bg = "white")
        MenuTitle.pack(padx = 10, pady = 10)

        tutor_button = tk.Button(self, text="Student", command = lambda: controller.show_frame(Tutor), bg = "white")
        tutor_button.place(relx = 0.5, rely = 0.5, anchor = "center")
		
        # quit_button = tk.Button(self, text="Quit", command = quit, bg = "white")
        # quit_button.pack(side = "bottom")
        
class Tutor(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        TutorTitle = tk.Label(self, text="Tutor List", font = 14, bg = "white")
        TutorTitle.pack(padx = 10, pady = 10)



        global StudentData
        global StudentNameArray
        global index
        global j
        studentdb = open("testdb", "r")
        temp = studentdb.readlines()
        #print temp
        StudentData = []
        StudentNameArray = []

        #print len(temp)
        for i in range(0, len(temp)): #Loop to split individual array
            StudentData.append(temp[i].replace("\n", " ").split(", "))



        self.tutor_list_box = tk.Listbox(self, bg = "white")

        
        for j in range(0,len(StudentData)):
            # tutor_name.append(tk.Label(self, text=tutor_list[i][0]))
            # tutor_name[i].pack(side = "top")
            StudentNameArray.append(StudentData[j][0])
            self.tutor_list_box.insert("end", StudentData[j][0])


        self.tutor_list_box.pack()

        menu_button = tk.Button(self, text="Main Menu", command = lambda: controller.show_frame(MainMenu), bg = "white")
        menu_button.pack(side = "bottom", padx = 10, pady = 10)

        detail_button = tk.Button(self, text="Detail Page", command = lambda: controller.show_frame(TutorDetail), bg = "white")
        detail_button.pack(side = "bottom", padx = 10, pady = 10)

    def test():
        self.nice = "very"

class TutorDetail(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        tutor_page = self.controller.get_page(Tutor)

        
        NAMETOSEARCH = "Shafiq"

        DetailTitle = tk.Label(self, text= NAMETOSEARCH + "'s Details", font = 14, bg = "white")
        DetailTitle.pack(padx = 10, pady = 10)

    
        #Checking index number
        for index in range(0, len(StudentNameArray)):
            if StudentNameArray[index] == NAMETOSEARCH:
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

        back_button = tk.Button(self, text="Back", command = lambda: controller.show_frame(Tutor), bg = "white")
        back_button.pack(side = "bottom", padx = 10, pady = 10)


if __name__ == "__main__":
    management = Management()
    management.mainloop()
