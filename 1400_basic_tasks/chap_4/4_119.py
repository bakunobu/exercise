from typing import Union


def calc_func(y:Union[float, int]) -> Union[float, int]:
    if y > 2:
        return(2)
    elif 0 < y <= 2:
        return(0)
    else:
        return(-3 * y)
    