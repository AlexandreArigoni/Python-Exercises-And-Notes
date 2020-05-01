n1 = float(input('Enter your first grade: '))
n2 = float(input('Enter your second grade: '))
m = (n1 + n2) / 2
if m < 5:
    print('\033[1;31mDisapproved')
elif 5 <= m <= 6.9:
    print('\033[1;34mRecuperation')
else:
    print('\033[1;35mApproved')
