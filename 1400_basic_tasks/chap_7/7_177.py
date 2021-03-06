from main_funcs import get_input


def count_max(num_list:list) -> int:
    my_list = num_list[:]
    a = get_input('Введите число: ', False)
    max_num = max(my_list)
    my_list.append(a)
    return(my_list.count(max_num))