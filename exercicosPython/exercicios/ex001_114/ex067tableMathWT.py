while True:
    n = int(input('Enter a positive number: '))
    if n < 0:
        print('End')
        break
    x = 1
    print('-'*20)
    while x <= 10:
        print(n*x)
        x += 1
    print('-' * 20)
