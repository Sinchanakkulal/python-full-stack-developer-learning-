"""count the number of the day in the month """
import calendar
year = int(input("year:"))
month = int(input("month: "))

count = calendar.monthrange(year,month)[1]
print("number of days:",count)