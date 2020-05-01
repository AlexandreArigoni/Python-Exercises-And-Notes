phrase = str(input('Enter a phrase ')).upper().strip()
print(phrase.upper().count('A'))
print('First A: {}'.format(phrase.find('A')+1))
# find = first time
print('Last A: {}'.format(phrase.rfind('A')+1))



