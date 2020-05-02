import urllib.request
from termcolor import colored

# This program checks if a website can be accessed from your computer and read the code of the site
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print(colored('Error', 'red'))
else:
    print(colored('Ok', 'green'))
    print(colored('Code of the site:', 'blue'))
    print(site.read())

# You can try any site, disconnect your ethernet for testing
