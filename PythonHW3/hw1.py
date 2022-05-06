#1
from datetime import date

my_mon = int(input("You : Enter month born (1-12): "))
my_day = int(input("You : Enter day born (1-31: )"))
my_year = int(input("You : Enter year born (4-digit) : "))
my_date = date(my_year, my_mon, my_day)

today_month = int(input("Enter month (1-12): "))
today_day = int(input("Enter day (1-31: )"))
today_year = int(input("Enter year (4-digit) : "))
today_date = date(today_year, today_month, today_day)

delta = today_date - my_date
print("Number of days you lived:",delta.days) # 일수로 변환 
