atmpts = 0


while True:
    try:
        i = int(input('Enter your password: '))
        atmpts += 1
        if atmpts == 10:
            break 
        if i == 0:
            break
        

    except ValueError:
        print('Not a number!')