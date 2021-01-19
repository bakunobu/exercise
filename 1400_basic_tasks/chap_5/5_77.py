for x in range(11, 100, 2):
    last_dig = x % 10
    if last_dig in (3, 7):
        print(x)