student = dict()
student['name'] = str(input('Name of the student: '))
student['average'] = float(input(f'Average of the student {student["name"]}: '))
print(student['name'])
print(student['average'])
if student['average'] >= 6:
    print('Aprovado!')
