p = float(input('Enter the price of the product '))
print('[1] In cash : Money/Check\n'
      '[2] In cash: Card\n'
      '[3] 2x on Card\n'
      '[4] 3x or above on Card')
t = int(input('Select how you wanna pay the product '))
if t == 1:
    print('Price: {:.2f}'.format(p*0.9))
elif t == 2:
    print('Price: {:.2f}'.format(p*0.95))
elif t == 3:
    print('Price: {:.2f}'.format(p))
elif t == 4:
    j = int(input('How many payment installments? '))
    print('Price: {:.2f}'.format((p*(j*1.2))/j))
else:
    print('Enter an correct number')
