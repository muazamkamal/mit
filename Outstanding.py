import datetime as dt

temp = dt.datetime.now()
MonthcurrentPaid= (temp.month)
YearcurrentPaid= (temp.year)

MonthlastPaid = input("Last Month : ")
YearlastPaid = input ("Last Year : ")
TuitionFees = 100

yearDifference = YearcurrentPaid - YearlastPaid
MonthDifference = (MonthcurrentPaid +(12* yearDifference)) - MonthlastPaid

if MonthDifference < 0:
    OutstandingMonths = 12-(MonthDifference * (-1))
else:
    OutstandingMonths = MonthDifference
    
if YearcurrentPaid == YearlastPaid:
    Outstanding = OutstandingMonths*TuitionFees
else:
    Outstanding = (OutstandingMonths)*TuitionFees




    

print OutstandingMonths
print Outstanding
