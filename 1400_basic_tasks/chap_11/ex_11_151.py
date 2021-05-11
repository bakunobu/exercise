# a
def make_simple_shift(my_lst:list) -> list:
    my_lst[1], my_lst[4] = my_lst[4], my_lst[1]
    return(my_lst)


# b
def make_ind_shift(my_lst:list, m:int, n:int) -> list:
    my_lst[m], my_lst[n] = my_lst[n], my_lst[m]
    return(my_lst)


# c
def change_with_max(my_lst:list) -> list:
    max_ind = my_lst.index(max(my_lst))
    mod_lst = make_ind_shift(my_lst, 2, max_ind)
    return(mod_lst)


# d
def find_last_min_ind(my_lst:list) -> list:
    ind_dict = dict()
    for i in range(len(my_lst)):
        if my_lst[i] not in ind_dict.keys():
            ind_dict[my_lst[i]] =[i, ]
        else:
            ind_dict[my_lst[i]].append(i)
    min_val = min(ind_dict.keys())
    return(ind_dict[min_val][-1])


def change_with_min(my_lst:list) -> list:
    min_ind = find_last_min_ind(my_lst)
    mod_lst = make_ind_shift(my_lst, 0, min_ind)
    return(mod_lst)