from datetime import datetime


def print_time():
    print('task completed')
    print(datetime.now())
    print()


first_name = 'Susan'
print_time()

for x in range(0, 10):
    print(x)
    print_time()


def get_initial(name: str):
    initial = name[0:1].upper()
    return initial


first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

print(
    f'Yours initials are {get_initial(first_name)}{get_initial(last_name)}')
