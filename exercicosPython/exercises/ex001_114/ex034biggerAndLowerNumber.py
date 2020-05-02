num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
num3 = int(input('Enter the third number: '))
# Verifying who is the biggest
biggest = num1
if num1 < num2 < num3:
    biggest = num3
if num1 < num3 < num2:
    biggest = num2
# Verifying who is the lowest
lowest = num1
if num1 > num2 > num3:
    lowest = num3
if num1 > num3 > num2:
    lowest = num2
print('The lowest number is {} and the biggest number is {}'.format(lowest, biggest))
