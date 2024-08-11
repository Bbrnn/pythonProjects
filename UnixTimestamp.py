#A Unix timestamp is like a stopwatch that tells us how many seconds have passed since January 1, 1970. It's a simple and universal way for computers to keep track of time.


import time
import datetime

#define the date
date = datetime.datetime(2024,8,17)

#Convert to unix timestamp
timestamp = int(time.mktime(date.timetuple()))


print("THe unix timestamp of the date 17-8-2024 is:",timestamp)
