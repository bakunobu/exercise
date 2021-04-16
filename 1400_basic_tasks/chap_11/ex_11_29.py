def no_moist_days(my_list:list) -> list:
    indices = [i+1 for i in range(len(my_list)) if my_list[i] == 0]
    return(indices)