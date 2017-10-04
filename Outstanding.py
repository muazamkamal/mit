import datetime as dt

temp = dt.datetime.now()
MonthcurrentPaid= (temp.month)
YearcurrentPaid= (temp.year)

MonthlastPaid = input("Last Month : ")
YearlastPaid = input ("Last Year : ")
TuitionFees = 100

MonthDifference = MonthcurrentPaid - MonthlastPaid

if MonthDifference < 0:
    OutstandingMonths = 12-(MonthDifference * (-1))
else:
    OutstandingMonths = MonthcurrentPaid- MonthlastPaid
    
if YearcurrentPaid == YearlastPaid:
    Outstanding = OutstandingMonths*TuitionFees
else:
    Outstanding = (YearcurrentPaid - YearlastPaid)*(OutstandingMonths)*TuitionFees




    

print OutstandingMonths
print Outstanding
