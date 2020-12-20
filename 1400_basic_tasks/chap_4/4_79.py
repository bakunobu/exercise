from itertools import filterfalse


def check_sides(a: float, b:float, c:float) -> bool:
    return(a + b > c)


def check_trianle(a:float, b:float, c:float) -> bool:
    for x in [(a, b, c), (b, c, a), (a, c, b)]:
        if not check_sides(* x):
            return(False)
    return(True)




