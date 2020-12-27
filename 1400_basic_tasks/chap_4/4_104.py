def abs_value(a:float) -> float:
    if a < 0:
        return(-a)
    return(a)


# a
def calc_half_sum(a:float, b:float) -> float:
    a = abs_value(a)
    b = abs_value(b)
    return((a+b) / 2)

# b
import math
def calc_prod_sqrt(a:float, b:float) -> float:
    a = abs_value(a)
    b = abs_value(b)
    return(math.sqrt(a * b))  