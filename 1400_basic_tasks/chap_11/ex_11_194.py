from typing import Union


def add_score(points:list, n:Union[int, float]) -> list:
    is_better_perform = [int(n < x) for x in points]
    return(is_better_perform.index(0))