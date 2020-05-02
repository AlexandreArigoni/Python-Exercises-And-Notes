t = ('Alo', 'Alexandre', 'Hello', 'Drop', 'xxx')
for c in t:
    print('In the word {} we have the vogals: '.format(c), end='')
    for x in range(0, len(c)):
        if c[x] in 'AaEeIiOoUu':
            print(c[x], end='' if x != len(c) - 1 else '\n')
print('\n')



