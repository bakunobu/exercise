import math
import doctest


def area_to_side(a:float) -> float:
    return(math.sqrt(a))


def area_to_radius(a: float) -> float:
    r = math.sqrt(a / math.pi)
    return(r)

def compare_figs(a_r:float, a_c:float) -> str:
    my_side = area_to_side(a_r)
    diag = math.sqrt(2 * my_side ** 2)
    my_rad = area_to_radius(a_c)
    diam = 2 * my_rad
    if diag < diam:
        return('circle')
    elif diag < diam:
        return('rectangle')
    else:
        return('equal')

# a

def check_condition_a(result:str) -> bool:
    return(result.lower() == 'rectangle')

# b
def check_condition_b(result:str) -> bool:
    return(result.lower() == 'circle')
    

if __name__ == '__main__':
    doctest.testmod()