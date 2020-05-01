from math import sin, cos, tan, radians
ang = int(input('Enter the angle: '))

print('The sine, cosine and tangent of {}º are respectively: \n'.format(ang))
ang = radians(ang)
# can put the function radians inside sen, cos, tan
print('{:.2f}\n{:.2f}\n{:.2f}\n'.format(sin(ang), cos(ang), tan(ang)))

