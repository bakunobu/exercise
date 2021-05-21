from typing import Union


def add_heigh(heigth:list, n:Union[int, float]) -> list:
    is_shorter = [int(n > x) for x in heigth]
    return(is_shorter.index(0))