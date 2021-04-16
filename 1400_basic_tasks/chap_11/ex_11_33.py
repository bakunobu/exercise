import math


def strange_transform(my_list:list) -> list:
    # a
    my_list = [math.pow(x, 2) for x in my_list if x > 10]
    # b
    my_list = [abs(my_list[i]) if not i % 2 else my_list[i] for i in range(len(my_list))]
    return(my_list)