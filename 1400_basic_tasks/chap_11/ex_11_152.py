# a
def change_halves(my_lst:list) -> list:
    i = len(my_lst) // 2
    lst_1 = my_lst[:i]
    lst_2 = my_lst[i:]
    return(lst_2 + lst_1)


# b
def step_change(my_lst:list) -> list:
    new_lst = []
    lst_1 = my_lst[::2]
    lst_2 = my_lst[1::2]
    for x_2, x_1 in zip(lst_2, lst_1):
        new_lst.append(x_2)
        new_lst.append(x_1)
    return(new_lst)


# c
def change_tails(my_lst:lst) -> list:
    for i in range(len(my_lst) // 2):
        j = i  * (-1) - 1
        my_lst[i], my_lst[j] = my_lst[j], my_lst[i]
    return(my_lst)