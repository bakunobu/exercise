from typing import Union


def calc_func(x:Union[float, int]) -> Union[float, int]:
    if x < - 1:
        return(-1)
    elif x > -1:
        return(x)
    else:
        return(1)