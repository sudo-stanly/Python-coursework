import time
import datetime
from datetime import datetime, timedelta

ini_time_for_now = datetime.now()
#print(ini_time_for_now)

#print(datetime.timedelta()) #! -> AttributeError: type object 'datetime.datetime' has no attribute 'timedelta'

#print(timedelta()) #* OUTPUT -> 0:00:00
#print(timedelta(5)) #* OUTPUT -> 5 days, 0:00:00

#print(timedelta(days - 5)) #! -> "days" is not defined

#print(timedelta(7 - 5)); #*OUTPUT -> 2 days, 0:00:00

#print("DATE BEFORE: ", datetime.now()) #* OUTPUT: DATE BEFORE:  2025-08-18 10:14:51.235584
#print("DATE AFTER: ", datetime.now() - timedelta(7 - 5)) #* DATE AFTER:  2025-08-16 10:14:51.235658

day = 50
dateBefore = datetime.now()
dateAfter = datetime.now() - timedelta(day)
print("DATE BEFORE: ", dateBefore)
print("DATE AFTER: ", dateAfter)