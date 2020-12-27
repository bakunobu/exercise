def pos_squared(a:float, b:float, c:float) -> tuple:
    res = [x ** 2 if x >= 0 else x for x in (a, b, c)]
    return(res)