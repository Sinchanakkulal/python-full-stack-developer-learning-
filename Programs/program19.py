"""find the day of the week"""
import calendar
year = int(input("enter the year name "))
month = int(input("enter the month name "))
date = int(input("Enter the date "))
day = calendar.day_name[calendar.weekday(year,month,date)]
print(f"day name is {day}")