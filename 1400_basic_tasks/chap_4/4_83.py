def print_shroom(k:int) -> None:
    if 11 <= k <= 19:
        print('В лесу {k} грибов.')
    elif k % 10 == 0:
        print('В лесу {k} грибов.')
    elif k % 10 == 1:
        print('В лесу {k} гриб.') 
    elif k % 10 in (2, 3, 4):
        print('В лесу {k} гриба.')
    else:
        print('В лесу {k} грибов.')
        