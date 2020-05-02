#caracteres chain - String
#Example: phrase = 'Video course python'> [] < - Space count

''' Slicing - Fatiamento '''

phrase[9] -> 10 letter (starts in 0)
phrase[9:13] -> 9 to 12 (13 excluded) -1
phrase[9:21:2] -> 9 to 20 jumping 2
phrase[:5] -> 0 to 4
phrase[15:] -> 15 to the end
phrase[9::3] -> 9 to the end jumping 3

''' Analyze '''
len(phrase) -> length
phrase.count('o') -> count how many 'o's
phrase.count('o',0,13) -> count 'o's with slicing (Fatiamento)
phrase.find('deo') -> where the program found 'deo' (start)
frase.find('x') -> if x dont exist -1 is returned
'Curse' in phrase -> will return true (is not a function)

''' Transformation '''
phrase.replace('x', 'y') -> replace x with y (like in the game when he put your name)
phrase.upper() -> put the phrase in CAPITAL
phrase.lower()
phrase.capitalized() -> Only the first caracter in capital
phrase.title() -> First letter of words in capital
phrase.strip() -> Remove the uselees spaces in the beginning ant in the end
phrase.rstrip() -> Equal strip put only the end (right side)
phrase.lstrip() -> Equal strip but only the beginning (left side)

''' Division '''
phrase.split() -> Division in the spaces 012345 -> 012 *split* 012 ----> Transform in list
''' Junction '''
'-'.join(phrase) -> Junction with '-'


in     ---> Have?
