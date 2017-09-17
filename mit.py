import Tkinter as tk
import sqlite3

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

        tutor_button = tk.Button(self, text="Tutor", command = lambda: controller.show_frame(Tutor), bg = "white")
        tutor_button.place(relx = 0.5, rely = 0.5, anchor = "center")

class Tutor(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg = "white")
        self.controller = controller

        conn = sqlite3.connect("Tutor.db")
        c = conn.cursor()

        TutorTitle = tk.Label(self, text="Tutor List", font = 14, bg = "white")
        TutorTitle.pack(padx = 10, pady = 10)

        c.execute("SELECT Name FROM Tutor ORDER BY Name ASC")

        tutor_list = c.fetchall()

        tutor_name = []

        self.tutor_list_box = tk.Listbox(self, bg = "white")

        for i in range(0, len(tutor_list)):
            # tutor_name.append(tk.Label(self, text=tutor_list[i][0]))
            # tutor_name[i].pack(side = "top")
            tutor_name.append(tutor_list[i][0])
            self.tutor_list_box.insert("end", tutor_list[i][0])

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

        print tutor_page.tutor_list_box.get("active")
        SelectedTutor = "Raimi"

        conn = sqlite3.connect("Tutor.db")
        c = conn.cursor()

        DetailTitle = tk.Label(self, text= SelectedTutor + "'s Details", font = 14, bg = "white")
        DetailTitle.pack(padx = 10, pady = 10)

        c.execute("SELECT Name, Contact, Subject FROM Tutor WHERE Name=?", (SelectedTutor,))

        TName, TContact, TSubject = c.fetchall()[0]

        Name = tk.Label(self, text="Name: " + TName, bg = "white")
        Contact = tk.Label(self, text="Contact: " + TContact, bg = "white")
        Subject = tk.Label(self, text="Subject: " + TSubject, bg = "white")

        Name.pack(side = "top")
        Contact.pack(side = "top")
        Subject.pack(side = "top")

        menu_button = tk.Button(self, text="Main Menu", command = lambda: controller.show_frame(MainMenu), bg = "white")
        menu_button.pack(side = "bottom", padx = 10, pady = 10)

        back_button = tk.Button(self, text="Back", command = lambda: controller.show_frame(Tutor), bg = "white")
        back_button.pack(side = "bottom", padx = 10, pady = 10)


if __name__ == "__main__":
    management = Management()
    management.mainloop()
