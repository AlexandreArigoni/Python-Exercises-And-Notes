h = float(input('\033[1;31mEnter your height in metres \033[m'))
w = float(input('\033[1;34mEnter your weight in kilograms \033[m'))
i = w / (h ** 2)
if i < 18.5:
    print('Under weight')
elif 18.5 <= i < 25:
    print('Ideal weight')
elif 25 <= i < 30:
    print('Over weight')
elif 30 <= i < 40:
    print('Obesity')
else:
    print('Morbid obesity')


