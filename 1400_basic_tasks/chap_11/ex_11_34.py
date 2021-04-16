def diff_num_list(my_list:list) -> list:
    # a
    k_1 = my_list[0]
    k_2 = my_list[1]
    my_list = [x - k_1 if x > 0 else x - k_2 for x in my_list]
    # b
    my_list = [my_list[i]-1 if not i%2 else my_list[i]+1 for i in range(len(my_list))]
    return(my_list)