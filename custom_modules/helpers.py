from colorama import init, Fore

# helpers.py


def display(message: str, is_warning=False):
    if is_warning:
        print(Fore.RED + message)
    else:
        print(Fore.BLUE + message)
