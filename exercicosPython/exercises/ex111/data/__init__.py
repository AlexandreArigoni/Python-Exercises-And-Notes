def readMoney(x):
    while True:
        from termcolor import colored
        num = input(x).replace(',', '.')
        if num.isalpha():
            print(colored('Error!', 'red'))
        else:
            return float(num)




