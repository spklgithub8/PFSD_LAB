import datetime
import time

print(time.time())
print(time.asctime())

datetime_obj=datetime.datetime.now()
print(datetime_obj)
print("Year:",datetime_obj.year)
print("Month:",datetime_obj.month)
print("day:",datetime_obj.day)
print("hour:",datetime_obj.hour)
print("minute:",datetime_obj.minute)
print("isoweekday:",datetime_obj.isoweekday())
print("isoclender:",datetime_obj.isocalendar())

import calendar
s = calendar.prcal(2024)
s2 = calendar.month(2024,4)
s1 = calendar.isleap(2024)

x=datetime.datetime.now()
from datetime import timedelta
print(x + timedelta(days=-89))

import time
from datetime import datetime
import pytz

time1=pytz.timezone('Asia/Kolkata')
print("Current Time in INDIA is: ",datetime.now(time1))
time2=pytz.timezone('Asia/Tokyo')
print("Current Time in JAPAN is: ",datetime.now(time2))
time3=pytz.timezone('Europe/Copenhagen')
print("Current Time in COPENHAGEN is: ",datetime.now(time3))