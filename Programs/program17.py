"""write the pythhon program to displa the calender"""
import calendar 
year = int(input("enter the year: "))
mon = int(input("enter the month: "))
cal = calendar.month(year,mon)
print(cal)
print("\n")
print(f"entire calender of the year{year}")
yr = calendar.calendar(year)
print(yr)

