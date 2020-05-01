g = str(input('Enter a gender[M/F]: ')).strip().upper()[0]
while g not in 'MF':
    g = str(input('Enter a gender: ')).strip().upper()[0]
print("Gender {} registered".format(g))
