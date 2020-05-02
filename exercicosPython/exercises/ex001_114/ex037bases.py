num = int(input('Enter an int number '))
uwant = int(input('Enter \n'
                  ' [1] for binary \n'
                  ' [2] for octal \n'
                  ' [3] for hexadecimal \n '))
if uwant == 1:
    print(bin(num)[2:])
elif uwant == 2:
    print(oct(num)[2:])
elif uwant == 3:
    print(hex(num)[2:])
else:
    print('Enter a possible number ')


