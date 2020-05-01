from termcolor import colored
km = float(input('Enter the distance in km of your travel: '))
if km <= 200:
    print(colored('You will pay R${:.2f}'.format(km*0.5), 'red'))
else:
    print(colored('You will pay R${:.2f}'.format(km*0.45), 'green'))

