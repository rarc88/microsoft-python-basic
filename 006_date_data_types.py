# To get current date and time
# we need use the datetime library
from datetime import datetime, timedelta

today = datetime.now()
# the now function returns a datetime object
print(f'Today is: {str(today)}')
print(f'Year: {today.year}')
print(f'Month: {today.month}')
print(f'Day: {today.day}')

# timedelta is used to difine a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print(f'Yesterday was: {str(yesterday)}')

birthday = input('When is your birthday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print(f'Birthday: {birthday_date.date()}')
