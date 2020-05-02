"""   | b - c | < a < b + c         a = num1
      | a - c | < b < a + c         b = num2
      | a - b | < c < a + b         c = num3

a = float(input('Type the first edge of the triangle: '))
b = float(input('Type the second edge of the triangle: '))
c = float(input('Type the third edge of the triangle: '))
num1 = a
num2 = b
num3 = c

if c > b:
    num2 = c
    num3 = b
if c > a:
    num1 = c
    num3 = a
if b > a:
    num2 = a
    num1 = b
if num2 - num3 < num1 < num2 + num3 and num1 - num3 < num2 < num1 + num3 and num1 - num2 < num3 < num1 + num2:
        print('Possible')
else:
        print('Impossible')

        ***Must be smaller than the sum of the other 2 edges***
    """
a = float(input('Enter the first edge of the triangle: '))
b = float(input('Enter the second edge of the triangle: '))
c = float(input('Enter the third edge of the triangle: '))
if a < b + c and b < a + c and c < a + b:
    print('Possible')
else:
    print('Impossible')
