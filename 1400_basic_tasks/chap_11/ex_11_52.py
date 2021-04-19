# a
def is_even_sum(my_list:list) -> bool:
    return(not sum(my_list) % 2)


# b
def has_five_digs(my_list:list) -> bool:
    cubes = [x * 2 for x in my_list]
    return(9999 < sum(cubes) < 99_999)