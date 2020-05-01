from time import sleep
from termcolor import colored
s = float(input('Enter here your salary '))
h = float(input('Enter here the value of the house '))
y = int(input('Enter in how many year you pretend to buy the house '))
sd = s*0.3
if sd * (12*y) >= h:
    print(colored('Processing', 'blue'))
    sleep(5)
    print('The bank will buy the house for you')
else:
    print(colored('Processing...', 'red'))
    sleep(5)
    print('The bank will not buy the house for you')
