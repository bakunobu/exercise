import math


def dist_to_hor(h:int, r:int=6350) -> float:
    expr_1 = (r + h) ** 2
    expr_2 = expr_1 - r ** 2
    return(math.sqrt(expr_2))


def print_dist() -> None:
    for x in range(1, 11):
        print(f'{x} {dist_to_hor(x)}')
        
        
print_dist()