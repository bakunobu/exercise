def move_els(elements:list, k:int) -> list:
    new_list = elements[k:] + elements[:k]
    return(new_list)