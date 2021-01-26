# a
def floor_div(a:int, b:int) -> int:
    i = 0
    while b >= a:
        i += 1
        b -= a
    return(i)


# b
def mod_div(a:int, b:int) -> int:
    while b >= a:
        b -= a
    return(b)

