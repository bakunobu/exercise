import math
from scipy import constants as const 


def x_cord(v_0: float, t:float, a:float) -> float:
    x = v_0 * t * math.cos(a)
    return(x)


def y_cord(v_0: float, t:float, a:float) -> float:
    y = v_0 * t * math.sin(a) - (const.g * t ** 2) / 2
    return(y)


def calc_t(R:float, v_0:float, a:float) -> float:
    expr = v_0 * math.cos(a)
    t = R / expr
    return(t)

def firing_calc(R:float, H:float, v_0:float, a:float) -> bool:
    t = calc_t(R, v_0, a)
    h = y_cord(v_0, t, a)
    if 0 < h <= H:
        return(True)
    else:
        return(False)

