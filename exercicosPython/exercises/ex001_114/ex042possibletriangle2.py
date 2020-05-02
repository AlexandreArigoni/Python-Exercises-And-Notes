a = float(input('Enter the first edge of the triangle '))
b = float(input('Enter the second edge of the triangle '))
c = float(input('Enter the third edge of the triangle '))
if b + c > a == b == c < a + b and b < a + c:
    print('Possible and Equilateral')
elif b + c > a == b != c < a + b and b < a + c or a == c != b or b == c != a:
    print('Possible and Isosceles')
elif b + c > a != b != c < a + b and b < a + c:
    print('Possible and Scalene')
else:
    print('Impossible')

# r1 != r2 != r3 != r1
