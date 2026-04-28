"""Find the number of leap years between two years."""

import calendar
year1 = int(input("enter the starting year"))
year2 = int(input("enter the end year"))
count = 0
for i in range(year1,year2+1):
    if calendar.isleap(i):
        count += 1

print(f"number of the leap year in between {year1} and {year2} is :",count)
