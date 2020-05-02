def biggest(*num):
    h = 0
    for c in num:
        if c > h:
            h = c
    print(f'In {num} {[len(num)]} the largest number is: {h}')


biggest(2, 9, 4, 7, 1)
biggest(4, 7, 0)
biggest(1, 2)
biggest(6)
biggest()




