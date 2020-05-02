count = s = 0
while True:
    n = int(input('Enter a number [999 to exit]: '))
    if n == 999:
        break
    s += n
    count += 1
print(f'The sum of the {count} values is {s}.')

