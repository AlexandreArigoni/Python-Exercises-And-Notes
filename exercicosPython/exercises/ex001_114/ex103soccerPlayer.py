def sheet(go='0', na='<unknown>'):
    if na == '':
        na = '<unknown>'
    if not go.isnumeric():
        go = 0
    else:
        go = int(go)
    print(f'The player {na} made {go} goals')


n = str(input('Name of the soccer player: '))
g = input('Goals of the soccer player: ')
sheet(g, n)

