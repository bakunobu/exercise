import math


def strange_transform(my_list:list) -> list:
    # a
    my_list = [abs(x) for x in my_list] # can add if x < 0
    # b
    my_list = [math.sqrt(my_list[i]) if i % 2 else my_list[i] for i in range(len(my_list))]
    return(my_list)