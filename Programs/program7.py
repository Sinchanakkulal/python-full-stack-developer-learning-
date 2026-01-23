#write the program to display the calender
import calendar


Year=int(input("enter the Year: "))
Month=int(input("enter the month of the year :"))

cal=calendar.month(Year,Month)
print(cal)