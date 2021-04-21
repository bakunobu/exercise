from typing import Union


def moist_per_month(moist:list) -> Union[int, float]:
    """
    индексы:
    март - 2
    июнь - 5
    сентябрь - 8
    декабрь - 11
    """
    return(sum(moist[2::3]))


    