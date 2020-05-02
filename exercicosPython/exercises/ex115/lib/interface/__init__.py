from termcolor import colored
from ex115.lib.arquivo import *
arc = 'archive.txt'
if not archExist(arc):
    print(archExist(arc))
    createArchive(arc)
print('=' * 30)
print('\tWelcome to the program!')
print('=' * 30)
while True:
    print(colored('1 - add a person to the list\n'
                  '2 - show the list\n'
                  '3 - close the program', 'red'))
    try:
        op = int(input(colored('What you want to do?\n', 'blue')))
    except (TypeError, ValueError):
        print(colored('Error in the type or value', 'yellow'))
        continue
    except:
        print(colored('Unexpected Error', 'yellow'))
        continue
    if op == 1:
        na = input(colored('Name: ', 'blue'))
        ag = int(input(colored('Age: ', 'blue')))
        register(arc, na, ag)
    if op == 2:
        count = 0
        print('=' * 30)
        print('\tAll listed persons')
        print('=' * 30)
        readArchive(arc)
        print('=' * 30)
    if op == 3:
        break
