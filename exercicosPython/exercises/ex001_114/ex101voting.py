def vote(born):
    from datetime import date
    if date.today().year - born < 16:
        print(f'U cant vote because youu have {date.today().year - born} years old')
    elif 18 >= date.today().year - born >= 16:
        print(f'Your vote is optional because you have {date.today().year - born} years old ')
    else:
        print('Your vote is necessary because you have 18 years or more')


vote(2004)

