from main_funcs import get_input
import math


def area_to_rad(area:float) -> float:
    return(math.sqrt(area / math.pi))


def find_least_circle(n:int) -> float:
    min_area = get_input('Укажите площать круга: ')
    for _ in range(1, n):
       my_area =  get_input('Укажите площать круга: ')
       min_area = min(my_area, min_area)
    return(area_to_rad(min_area))