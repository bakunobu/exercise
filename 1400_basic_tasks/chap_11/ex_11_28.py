def num_dec_els(my_list:list) -> list:
    indices = [i for i in range(len(my_list)) if not my_list[i] % 10]
    return(indices)