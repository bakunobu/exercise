def print_n_2(n):
    if n <= 0:
        pass
    else:
        i = 0
        while 2 ** i <= n:
            print(2 ** i)
            i += 1