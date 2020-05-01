from termcolor import colored
lis = list()
person = list()
print(colored('=' * 30, 'blue'))
print(colored('\tWelcome to the program!', 'blue'))
print(colored('=' * 30, 'blue'))
while True:
    print(colored('Press 1 to add a person to the list\n'
                  'Press 2 to show the list\n'
                  'Press 3 to close the program', 'red'))
    try:
        op = int(input(colored('What you want to do?\n', 'blue')))
    except (TypeError, ValueError):
        print(colored('Error in the type or value', 'yellow'))
        continue
    except:
        print(colored('Unexpected Error', 'yellow'))
        continue
    if op == 1:
        person.append(input(colored('Name: ', 'blue')))
        person.append(int(input(colored('Age: ', 'blue'))))
        lis.append(person[:])
        person.clear()
    if op == 2:
        count = 0
        print(colored('=' * 30, 'blue'))
        print(colored('\tAll listed persons', 'blue'))
        print(colored('=' * 30, 'blue'))
        for c in lis:
            print(colored(f'{lis[count][0]}', 'green'), end='')
            print(colored(f'\t\t{lis[count][1]}', 'green'))
            count += 1
        count = 0
    if op == 3:
        break