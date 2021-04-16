# a
def diff_num_list(my_list:list, n:float) -> list: 
    k_1 = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > 0:
            my_list[i] -= k_1
        elif my_list[i] < 0:
            my_list[i] += n
    return(my_list)


# b
def anothter_diff(my_list:list, n:float,
                  a:float, b:float) -> my_list:
    for i in range(len(my_list)):
        if my_list[i] == 0:
            my_list[i] += n
        elif my_list[i] > 0:
            my_list[i] -= a
        else:
            my_list[i] += b
    return(my_list)