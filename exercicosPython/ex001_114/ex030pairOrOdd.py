from termcolor import colored
num = int(input('Enter a number: '))
if num % 2 == 0:
    print(colored('Is an even number', 'red'))
else:
    print(colored('Is an odd number', 'yellow'))
