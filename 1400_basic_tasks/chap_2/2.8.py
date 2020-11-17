import math


def calc_circumference(r:float) -> float:
    P = 2 * math.pi * r
    return(P)


def calc_area(r:float) -> float:
    S = math.pi * r ** 2
    return(S)

def show_res(r:float) -> None:
    print('Circunference of the circle: %0.2f'
          % calc_circumference(r))
    print('Area of the circle: %0.2f'
          % calc_area(r))
    
    
show_res(10)
    