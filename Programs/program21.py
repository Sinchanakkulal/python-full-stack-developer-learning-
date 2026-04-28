"""Find all Mondays in a given month."""
import calendar
year = int(input("year: "))
month = int(input("month: "))
cal = calendar.monthcalendar(year,month)
print(cal)
for week in cal:
    if week[calendar.MONDAY] != 0:
        print(week[calendar.MONDAY])
    
