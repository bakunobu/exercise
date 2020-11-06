def checker_board(n):
    for x in range(n):
        if x % 2 == 0:
            print(* list('*' * n), sep=' ')
        else:
            print(' ', end='')
            print(* list('*' * (n - 1)), sep=' ')