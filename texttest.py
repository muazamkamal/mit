def writeDB():

    num = input("Please enter number of students: ")
    studentdb = open("testdb", "a")
    for i in range(0, num):
        print "\nData for student number ", i + 1
        StudentName = raw_input("\nPlease enter name: ")
        Contact = raw_input("\nPlease enter contact: ")
        EContact = raw_input("\nPlease enter emergency contact: ")
        Subject = raw_input("\nPlease enter subject: ")
        TuitionFees = input("\nPlease enter tuition fees: ")
        Outstanding = input("\nPlease enter outstanding: ")

        TuitionFees = float(TuitionFees)
        Outstanding = float(Outstanding)
        TuitionFees = str(TuitionFees)
        Outstanding = str(Outstanding)

        StudentInput = [StudentName, Contact, EContact, Subject, TuitionFees, Outstanding]

        for data in StudentInput:
            studentdb.write(data + ", ")

        studentdb.write("\n")


def readDB():

    global StudentData
    global index
    studentdb = open("testdb", "r")
    temp = studentdb.readlines()

    StudentData = []
    StudentNameArray = []

    for i in range(0, len(temp)): #Loop to split individual array
        StudentData.append(temp[i].replace("\n", " ").split(", "))

    for j in range(0,len(StudentData)):
        print StudentData[j][0]
        StudentNameArray.append(StudentData[j][0])


    NAMETOSEARCH = raw_input("Please enter the name of the student that you want: ")
    #Checking index number
    for index in range(0, len(StudentNameArray)):
        if StudentNameArray[index] == NAMETOSEARCH:
            break
    print "Name : ",StudentData[index][0]
    print "Contact Number : ", StudentData[index][1]
    print "Emergency Contact Number : ", StudentData[index][2]
    print "Subject Taken : ", StudentData[index][3]
    print "Tuition Fees : RM",StudentData[index][4]
    print "Outstanding : RM",StudentData[index][5]

def paymentDB() :

    OutstandingMonths = float(StudentData[index][5])/ float(StudentData[index][4])
    print "This student has outstanding fees for ",OutstandingMonths," months !"
    Payment =input("Please enter how much this student wants to pay: ")
    StudentData[index][5] = float(StudentData[index][5])- float(Payment)
    print "The outstanding balance for this student is RM ",StudentData[index][5]
    outstanding = str(StudentData[index][5])

    studentdb = open("testdb", "w")
    for i in range(0, len(StudentData)):
        for j in range(0, 6):
            studentdb.write(str(StudentData[i][j]) + ", ")

        studentdb.write("\n")

    studentdb.close()

    # studentdb = open("testdb", "a")
    # StudentName = StudentData[index][0]
    # Contact = StudentData[index][1]
    # EContact = StudentData[index][2]
    # Subject = StudentData[index][3]
    # TuitionFees = StudentData[index][4]
    # Outstanding = outstanding
    #
    # StudentInput = [StudentName, Contact, EContact, Subject, TuitionFees, Outstanding]
    #
    # for data in StudentInput:
    #     studentdb.write(data + ", ")

# writeDB()
readDB()
# paymentDB()
