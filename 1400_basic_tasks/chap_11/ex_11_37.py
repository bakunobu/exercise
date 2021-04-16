# a
def simple_transform(my_list:list, b:float) -> list:
    a_1 = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] < 0:
            my_list[i] += 1
        elif my_list[i] == 0:
            my_list[i] -= b
    return(my_list)


# b
def bit_harder_transform(my_list:list, a:float,
                         b:float, c:float) -> list:
    
    for i in range(len(my_list)):
        if my_list[i] > 0:
            my_list[i] -= a
        elif my_list[i] < 0:
            my_list[i] -= b
        else:
            my_list[i] += c
    
    return(my_list)