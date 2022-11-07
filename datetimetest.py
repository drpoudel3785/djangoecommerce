import datetime
from datetime import datetime as dt, date, time, timedelta
import pytz

EndDate = dt.today() + datetime.timedelta(days=300)
print("Exitry Date =" , EndDate)

local = datetime.datetime.now()
print("Local:", local.strftime("%A, %m/%d/%Y, %H:%M:%S"))

tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))


datetime_object = datetime.datetime.now()
print(datetime_object)
#getting todays date
do= datetime.date.today()
print(do)

#whats inside datetime
print(dir(datetime))

#date object to represent a date
d = datetime.date(2019, 4, 13)
print(d)
#printing year, month, day in seperate line
print("Current year:", do.year)
print("Current month:", do.month)
print("Current day:", do.day)

# getting current date and time
t = datetime_object.strftime("%H:%M:%S")
d = datetime_object.strftime("%Y/%m/%d")
print("Date: ", d)
print("time:", t)



