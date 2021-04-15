def print_pos_then_neg(my_list:list) -> None:
    pos_nums = [x for x in my_list if x >= 0]
    neg_nums = [x for x in my_list if x < 0]
    print(* pos_nums)
    print(* neg_nums)