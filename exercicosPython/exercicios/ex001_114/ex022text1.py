name1 = str(input('Enter your first name ')).strip()
name2 = str(input('Enter your last name ')).strip()
cname = name1 + ' ' + name2
cnamenospace = name1 + name2
print(cname)
print('Name uppercase: {}'.format(cname.upper()))
print('Name lowercase: {}'.format(cname.lower()))
splited = cname.split()
print('Your name without the spaces have {} letters'.format(len(cnamenospace)))
print('Your first name have {} letters'.format(len(splited[0])))

