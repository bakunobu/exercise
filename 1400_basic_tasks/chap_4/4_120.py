from typing import Union

# a
def calc_func_one(x:Union[float, int]) -> Union[float, int]:
    if x < -1:
        return(0)
    elif x > 0:
        return(1)
    else:
        return(x)
    

# b
def calc_func_one(x:Union[float, int]) -> Union[float, int]:
    if x < -1:
        return(1)
    elif x > 1:
        return(-1)
    else:
        return(-x)

# c:
def calc_func_one(x:Union[float, int]) -> Union[float, int]:
    if -1 <= x < 0:
        return(-0.5 * x + 0.5)
    elif 0 < x <= 1:
        return(0.5 * x + 0.5)
    else:
        return(1)
