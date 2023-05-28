from datetime import date

from datetime import time, timedelta
from datetime import datetime

# print(datetime.MAXYEAR)  # MAX YEAR
# print(datetime.MINYEAR)  # MIN YEAR

# DATA TYPES OF DATETIME MODULE

# 1.Class datetime.date (YEAR MONTH DAY) AS A PARAMETER


date_1 = date(2020, 2, 12)
date_2 = date(year=2000, month=12, day=14)

print(date_1, date_2)
print(type(date_1))

# 2.Class datetime.time (hr, min, sec, micro and tz-info) parameters

time1 = time(2, 23, 55, 999)
time2 = time(hour=14, minute=20)
print(time1)
print(time2)

# 3.Class datetime.datetime
# datetime(year, month, day[, hour[, minute[, second[, microsecond[,tz-info]]]]])

datetime_1 = datetime(2000, 12, 14, 21, 45, 10, 876)
print(datetime_1)

# 4.Class datetime.timedelta

d1 = timedelta(hours=10)
d2 = timedelta(days=20, seconds=40, microseconds=21, milliseconds=122, minutes=36000, hours=24, weeks=2)
print(d1)
print(d2)

# 5. class datetime.tz-info

# 6. class datetime.timezone

from datetime import  datetime,date

# tz1 = timezone(offset=timedelta(hours=9, minutes=45))
# print(tz1)
#
# # Adding timedelta to the datetime instance.
# # We can add timedelta value to date or datetime instance to get the new date or datetime.
#
# date_1 = date(1999, 6, 14)
#
# date_2 = date_1 + timedelta(days=5)
# print(date_2)
#
# datetime_1 = datetime(1999, 12, 12, 22, 23, 21, 122, )
# datetime_2 = datetime_1 - timedelta(days=12, hours=22)
# print(datetime_2)
date_1 = date(2023, 5, 28)
date_2 = date(1999, 10, 15).month
# diff = date_1 - date_2
d = date_1.strftime('%Y %b %a')
print(d)