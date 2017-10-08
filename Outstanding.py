import datetime as dt

temp = dt.datetime.now()
MonthcurrentPaid= (temp.month)
YearcurrentPaid= (temp.year)

StudentMonthPaid = input("Last Month : ")
StudentYearPaid = input ("Last Year : ")
TuitionFees = 100

yearDifference = YearcurrentPaid - StudentYearPaid
MonthDifference = (MonthcurrentPaid +(12* yearDifference)) - StudentMonthPaid

if MonthDifference < 0:
    OutstandingMonths = 12-(MonthDifference * (-1))
else:
    OutstandingMonths = MonthDifference
    
if YearcurrentPaid == StudentYearPaid:
    Outstanding = OutstandingMonths*TuitionFees
else:
    Outstanding = (OutstandingMonths)*TuitionFees




    

print OutstandingMonths
print Outstanding
