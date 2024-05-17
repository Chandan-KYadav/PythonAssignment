# Write a python script to display the current date and time. first create variables to store date and time, then display date and time in proper format(like 13-08-2022 and 9:00 PM)

from datetime import datetime
current_datetime = datetime.now()

date = current_datetime.date()
time = current_datetime.time()

# print(current_datetime)
print(date.strftime("%d-%m-%Y"))
print(time.strftime("%I:%M %p"))