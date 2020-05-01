from datetime import date
person = dict()
person['name'] = str(input('Name: '))
person['born'] = int(input('Year of birth: '))
person['ctps'] = int(input('CTPS (Enter 0 if you dont have one): '))
if person['ctps'] == 0:
    print(f'Name: {person["name"]}\nAge: {date.today().year - person["born"]}\nCTPS: {person["ctps"]}')
else:
    person['ycontract'] = int(input('Year of hiring: '))
    r = person['ycontract'] - person['born'] + 35
    person['salary'] = float(input('Salary: '))
    person['retirement'] = r
    print(f'Name: {person["name"]}\nAge: {date.today().year - person["born"]}\nCTPS: {person["ctps"]}\n'
          f'Year of hiring: {person["ycontract"]}\nSalary: {person["salary"]}\nRetirement: {r}')
