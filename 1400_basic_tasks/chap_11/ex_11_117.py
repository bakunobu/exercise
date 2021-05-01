from typing import Union


def max_range(heigth: list) -> Union[int, float]:
    return(max(heigth) - min(heigth))