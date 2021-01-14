import math


def calc_area(x_1:float=0.0,
              x_2:float=math.pi) -> float:
    cos_1 = math.cos(x_1)
    cos_2 = math.cos(x_2)
    return(cos_1 - cos_2)


