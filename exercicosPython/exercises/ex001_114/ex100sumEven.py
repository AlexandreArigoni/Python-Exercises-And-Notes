from random import randint
li = list()


def sort():
    for c in range(0, 5):
        li.append(randint(1, 10))


def even(lis):
    s = 0
    for c in lis:
        if c % 2 == 0:
            s += c
    print(f'In the list {li} the sum of the even number is: {s}')


sort()
even(li)



