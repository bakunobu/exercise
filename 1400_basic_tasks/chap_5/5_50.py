def race_mult(s:float) -> float:
    return(1.1*s)


def calc_route(n:int=10, s:float=10000.0) -> None:
    for x in range(n):
        s = race_mult(s)
        print(x, s, sep='->')


def calc_dist(n:int=7, s:float=10000.0) -> float:
    total = s
    for i in range(n):
        s = race_mult(s)
        total += s
    return(total)


