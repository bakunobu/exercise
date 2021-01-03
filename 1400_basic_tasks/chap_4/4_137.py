def how_many_days(n: int) -> int:
    if n in (1, 3, 5, 7, 8, 10, 12):
        return(31)
    elif n in (4, 6, 9, 11):
        return(30)
    else:
        return(28)