li = []
while True:
    n = int(input('Enter a number[0 to exit]: '))
    if n == 0:
        break
    else:
        if li.count(n) != 0:
            continue
        elif li.count(n) == 0:
            li.append(n)
li.sort()
print(li)


