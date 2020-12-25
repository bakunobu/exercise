def is_even(a:int, n:int) -> bool:
    if a % 2 == 0 and n % 2 != 0:
        return(True)
    elif a % 2 != 0 and n % 2 == 0:
        return(True)
    else:
        return(False)
        