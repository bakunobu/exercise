from typing import Any


def show_el(i:int, my_list:list) -> Any:
    try:
        return(my_list[i])
    except IndexError:
        print('Index prvided is out of range!')