p = str(input('Enter an phrase: '))
p = p.replace(' ', '')
print(p[::-1])
if p[::] == p[::-1]:
    print('\033[32;mPalindrome\033[m')
else:
    print('\033[34;mNot an palindrome\033[m')





