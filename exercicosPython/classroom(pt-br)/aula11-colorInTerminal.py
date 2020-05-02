"""Colors in Terminal"""
#                  ANSI             #
->Stars with \
Colors: \033[0;33;44m    --->   U put print('\033[m xxxx \033[m') -> Put again in the end to pick just the word
            *style *text-color *background
"""Styles who works better for python"""
0 - None
1 - Bold
4 - Underline
7 - Negative (invert the configurations) --> if u put white letter she became a black one

"""Text"""
30 - 37
"""Background"""
40 - 47
Black -> Normal of the python terminal

#   Configurating Colors Example:
cores = {'Red': '\033[1;31m', 'Blue': '\033[1;34m', 'End': '\033[m'}
name3 = 'Joao'
print('{}{}{}'.format(cores['Blue'], name3, cores['End']))

             {}  -> Used for the list
             :   -> Add something to this thing of the list
             
#check out colorize
