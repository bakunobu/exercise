# a
def is_pos(my_list:list, s:int) -> bool:
    return(my_list[s] > 0)


# b
def is_even(my_list:list, k:int) -> bool:
    return(not my_list[k] % 2)

# c
def which_bigger(my_list:list, s:int, k:int) -> int:
    if my_list[s] < my_list[k]:
        return(k)
    else:
        return(s)