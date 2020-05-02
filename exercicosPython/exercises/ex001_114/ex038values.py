num1 = int(input('Enter the first number '))
num2 = int(input('Enter the second number '))
if num1 > num2:
    print('The first number is higher')
elif num2 > num1:
    print('The second number is higher')
else:
    print('\033[1;31;40mThe numbers are equal\033[m')
