p = 0
z = 0, 0
bigger = 0
smaller = 0
for c in range(1, 6):
    p = int(input('Enter the weight of the {}º person: '.format(c)))
    if c == 1:
        bigger = p
        smaller = p
    else:
        # Is changing the variable bigger and smaller according to the bigger and smaller number
        if p > bigger:
            bigger = p
        elif p < smaller:
            smaller = p
print('Bigger: {}'.format(bigger))
print('Smaller: {}'.format(smaller))




