from termcolor import colored


def leiaInt(phrase):
    while True:
        num = input(f'{phrase} ')
        if num.isnumeric():
            return num
        else:
            print(colored('ERROR!', 'red'))


n = leiaInt('Enter an number: ')
print(f'You enter the number: {n}')


