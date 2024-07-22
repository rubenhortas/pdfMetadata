import os


def clear_screen():
    if 'nt' in os.name:
        os.system('cls')
    elif 'posix' in os.name:
        os.system('clear')
