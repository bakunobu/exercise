while True:
    try:
        i = int(input('Type in even number: '))
        if i % 2 == 0:
            break
        else:
            print('Use EVEN numbers')
    except ValueError:
        print('Use numbers only!')