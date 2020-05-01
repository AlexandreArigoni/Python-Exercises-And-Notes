from termcolor import colored


def leiaNum():
    while True:
        try:
            int(input('Enter an int number: '))
        except (ValueError, TypeError):
            print(colored('ERROR! Try again... ', 'red'))
        # KeyboardInterrupt is not working
        except (KeyboardInterrupt):
            print(colored('The user optioned to not set a value', 'red'))
        else:
            while True:
                try:
                    float(input('Enter an real number: '))
                except (ValueError, TypeError):
                    print(colored('ERROR! Try again... ', 'red'))
                # KeyboardInterrupt is not working
                except (KeyboardInterrupt):
                    print(colored('The user optioned to not set a value', 'red'))
                else:
                    return 0


leiaNum()

