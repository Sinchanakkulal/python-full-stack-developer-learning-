"""write a programt o check whether the  given year is leap year or not """
import calendar
year = int(input("enter the given year: "))
if calendar.isleap(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")