passwd = 123


while True:
    try:
        i = int(input('Enter your password: '))
        if i == passwd:
            print('Password accepted!')
            break
        else:
            print('Wrong password')
    except ValueError:
        print('Wrong password')