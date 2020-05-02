def archExist(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createArchive(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('Error in the creation of the file')
    else:
        print(f'Archive {name} created')


def readArchive(name):
    try:
        a = open(name, 'rt')
    except:
        print('Error in the reading of the archive')
    else:
        for line in a:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<25} {data[1]:>3}')
    finally:
        a.close()


def register(arc, name='unknown', age=0):
    try:
        a = open(arc, 'at')
    except:
        print('An error happened in the opening of the archive')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print('An error happened in the writing of the data')
        else:
            print('Person registered!')
