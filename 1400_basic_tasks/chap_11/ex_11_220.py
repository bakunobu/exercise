from typing import Any


def calc_els(my_array:list) -> Any:
    for x in my_array:
        if my_array.count(x) > 1:
            return(x)