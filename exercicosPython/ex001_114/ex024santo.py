''' city = str(input('Type the name of the city: '))
city2 = city.upper().split()
print(city2[0].find('SANTO')) '''

city = str(input('Enter the name of the city: '))
print(city[:5].upper() == 'SANTO')


