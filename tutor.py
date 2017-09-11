from tkinter import *
import sqlite3

conn = sqlite3.connect("Tutor.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Tutor(Name TEXT, Contact TEXT, Subject TEXT, TutorSalary REAL)")

def data_entry():
    TutorName = input("Please enter tutor name: ")
    Contact = input("Please enter contact number: ")
    Subject = input("Please enter subject to be teach: ")

    c.execute("INSERT INTO Tutor(Name, Contact, Subject) VALUES (?, ?, ?)", (TutorName, Contact, Subject))
    conn.commit()

def display_name():
    c.execute("SELECT Name FROM Tutor ORDER BY Name ASC")
    for disp_name in c.fetchall():
        print(' '.join(disp_name))

def tutor_selected():
    SelectedTutor = input("Please enter tutor to be selected: ")
    c.execute("SELECT Name, Contact, Subject FROM Tutor WHERE Name=?", (SelectedTutor,))
    temp = c.fetchall()

    for i in range(len(*temp)):
        print(temp[0][i])



#create_table()
#data_entry()
#display_name()
#tutor_selected()
#c.close()
#conn.close()
