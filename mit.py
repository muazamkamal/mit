import tkinter as tk
from tkinter import font
import sqlite3

class Management(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("M.I.T")
        self.geometry("640x480")
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

class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        MenuTitle = tk.Label(self, text="Main Menu", font = 14)
        MenuTitle.pack(padx = 10, pady = 10)

        tutor_button = tk.Button(self, text="Tutor", command = lambda: controller.show_frame(Tutor))
        tutor_button.place(relx = 0.5, rely = 0.5, anchor = "center")

class Tutor(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        conn = sqlite3.connect("Tutor.db")
        c = conn.cursor()

        TutorTitle = tk.Label(self, text="Tutor List", font = 14)
        TutorTitle.pack(padx = 10, pady = 10)

        c.execute("SELECT Name FROM Tutor ORDER BY Name ASC")

        tutor_list = c.fetchall()
        #print(len(tutor_list)) #debugging
        #print(tutor_list)
        tutor_name = []
        #print(tutor_name)
        for i in range(0, len(tutor_list)):
            #tutor_name[i] = tk.Label(self, text=tutor_list[i][0])
            tutor_name.append(tk.Label(self, text=tutor_list[i][0]))
            tutor_name[i].pack(side = "top")

        #print(tutor_name)

        menu_button = tk.Button(self, text="Main Menu", command = lambda: controller.show_frame(MainMenu))
        menu_button.pack(side = "bottom", padx = 10, pady = 10)

        detail_button = tk.Button(self, text="Detail Page", command = lambda: controller.show_frame(TutorDetail))
        detail_button.pack(side = "bottom", padx = 10, pady = 10)

class TutorDetail(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        SelectedTutor = "Ilyas"

        conn = sqlite3.connect("Tutor.db")
        c = conn.cursor()

        DetailTitle = tk.Label(self, text= SelectedTutor + "'s Details", font = 14)
        DetailTitle.pack(padx = 10, pady = 10)

        c.execute("SELECT Name, Contact, Subject FROM Tutor WHERE Name=?", (SelectedTutor,))

        TName, TContact, TSubject = c.fetchall()[0]

        Name = tk.Label(self, text="Name: " + TName)
        Contact = tk.Label(self, text="Contact: " + TContact)
        Subject = tk.Label(self, text="Subject: " + TSubject)

        Name.pack(side = "top")
        Contact.pack(side = "top")
        Subject.pack(side = "top")

        menu_button = tk.Button(self, text="Main Menu", command = lambda: controller.show_frame(MainMenu))
        menu_button.pack(side = "bottom", padx = 10, pady = 10)

        back_button = tk.Button(self, text="Back", command = lambda: controller.show_frame(Tutor))
        back_button.pack(side = "bottom", padx = 10, pady = 10)

if __name__ == "__main__":
    management = Management()
    management.mainloop()
