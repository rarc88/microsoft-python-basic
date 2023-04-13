def get_initial(name: str, force_uppercase=True):
    initial = name[0:1]
    if force_uppercase:
        initial = initial.upper()
    return initial


first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

print(
    f'Yours initials are {get_initial(first_name)}{get_initial(force_uppercase=False, name=last_name)}')


def error_logger(error_code: int, error_severity: int, log_to_db: bool, error_message: str, source_module: str):
    print(f'oh no error: {error_message}')


first_number = 10
second_number = 5
if first_number > second_number:
    error_logger(error_code=45, error_severity=1, log_to_db=False,
                 error_message='Second number greater than first', source_module='my_math_method')
