# a
def change_els(my_list:list) -> list:
    for i in range(len(my_list)):
        if my_list[i] % 10 == 0:
            my_list[i] = 0
    return(my_list)


# b
def change_more_els(my_list:list) -> list:
    for j in range(len(my_list)):
        if my_list[j] % 2:
            my_list[j] *= 2
        else:
            my_list[j] /=2
    return(my_list)


# c
def ransform_list(my_list:list, m:int, n:int) -> list:
    for i in range(len(my_list)):
        if my_list[i] % 2:
            my_list[i] -= m
        if i % 2:
            my_list[i] += n
    return(my_list)