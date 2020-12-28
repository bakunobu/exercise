from typing import Union


def calc_func(a:Union[float, int]) -> Union[float, int]:
    if  a > 0:
        return(1)
    elif a < 0:
        return(-1)
    else:
        return(0) 