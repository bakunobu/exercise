import math


def find_a(S_s:float) -> float:
    return(math.sqrt(a))

def find_r(S_c:float) -> float:
    r_2 = S_c / math.pi
    return(math.sqrt(r_2))

# a
def in_square(a:float, r:float) -> bool:
    if a > (2 * r):
        return(True)
    else:
        return(False)

# b
def in_circle(a:float, r:float) -> bool:
    if (2 * r) > a:
        return(True)
    else:
        return(False)