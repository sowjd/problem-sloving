"""
datetime document
https://docs.python.org/3.9/library/datetime.html
"""
import sys
from datetime import date

dayList = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
month, day = map(int, sys.stdin.readline().rstrip().split())

print(dayList[date(2007, month, day).weekday()])
