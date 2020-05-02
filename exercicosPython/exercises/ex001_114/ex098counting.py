from time import sleep


def younow(first, last, skip):
    print()
    print('-=' * 25)
    print(f'Counting between {first} and {last} {skip} by {skip}')
    print('-=' * 25)
    if skip == 0:
        skip = 1
    if first < last:
        if skip < 0:
            for c in range(last, first - 1, skip):
                sleep(0.4)
                print(c, end=' ')
        else:
            for c in range(first, last+1, skip):
                sleep(0.4)
                print(c, end=' ')
    else:
        if skip < 0:
            for c in range(first, last - 1, skip):
                sleep(0.4)
                print(c, end=' ')
        else:
            for c in range(first, last-1, -skip):
                sleep(0.4)
                print(c, end=' ')


younow(10, 5, 1)


