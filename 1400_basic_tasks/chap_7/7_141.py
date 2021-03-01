from main_funcs import get_input
import math


def area_to_diag(area:float) -> float:
    side = math.sqrt(area)
    diag = math.sqrt(2 * side ** 2)
    return(diag)


def find_least_circle(n:int) -> float:
    max_area = get_input('Укажите площать квадрата: ')
    for _ in range(1, n):
       my_area =  get_input('Укажите площать круга: ')
       max_area = max(my_area, max_area)
    return(area_to_diag(max_area))