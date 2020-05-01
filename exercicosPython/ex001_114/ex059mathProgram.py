n = int(input('Enter the first number: '))
m = int(input('Enter the second number: '))
c = 0
while c != 5:
    print('Enter [1] for sum\nEnter [2] for multiplication\nEnter [3] to show the bigger number\n'
          'Enter [4] to select new numbers\nEnter [5] to exit ')
    c = int(input())
    if c == 1:
        print(n+m)
    elif c == 2:
        print(n*m)
    elif c == 3:
        if n < m:
            print(m)
        else:
            print(n)
    elif c == 4:
        n = int(input('Enter the first number: '))
        m = int(input('Enter the second number: '))
    elif c == 5:
        print()
    else:
        print('Impossible option')
print('End')
