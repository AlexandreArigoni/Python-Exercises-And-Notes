n = ('zero', 'one', 'two', 'three', 'four', 'five')
num = int(input('Enter a number between 0 and 5 '))
while num > 5 or num < 0:
    num = int(input('Type a number between 0 and 5 '))
print(n[num])

