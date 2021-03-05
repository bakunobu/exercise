from main_funcs import get_input


def get_seq(n:int) -> list:
    msg = 'Введите число: '
    my_seq = [get_input(msg, False) for x in range(n)]
    return(my_seq)


# a
def max_sum(my_list:list) -> int:
    pair_sum = [my_list[i] + my_list[i + 1] for i in range(len(my_list)-1)]
    return(max(pair_sum))


# b
def min_sum(my_list:list) -> int:
    pair_sum = [my_list[i] + my_list[i + 1] for i in range(len(my_list)-1)]
    return(min(pair_sum))


# c
def max_ind(my_list:list) -> tuple:
    pair_sum = [my_list[i] + my_list[i + 1] for i in range(len(my_list)-1)]
    max_num = max(pair_sum)
    ind = pair_sum.index(max_num)
    return(ind+1, ind+2)
    

# d
def min_ind(my_list:list) -> tuple:
    pair_sum = [my_list[i] + my_list[i + 1] for i in range(len(my_list)-1)]
    min_num = min(pair_sum)
    ind = pair_sum[::-1].index(min_num)
    true_ind = len(pair_sum) - ind
    return(true_ind+1, true_ind+2)