from typing import Union


def calc_func(x:Union[float, int]) -> Union[float, int]:
    if x <= 0:
        return(0)
    elif  0 < x <= 1:
        return(x)
    else:
        return(x ** 2)

