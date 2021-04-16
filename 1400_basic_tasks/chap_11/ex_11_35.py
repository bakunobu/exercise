def diff_num_list(my_list:list) -> list:
    # a
    m_1 = my_list[0]
    m_2 = my_list[1]
    my_list = [x - m_1 if x > 0 else x - m_2 for x in my_list]
    # b
    my_list = [my_list[i]*2 if not i%2 else my_list[i]-1 for i in range(len(my_list))]
    return(my_list)