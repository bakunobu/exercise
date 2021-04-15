def print_even_tnah_odd(my_list:list) -> None:
    even_nums = [x for x in my_list if not x % 2]
    odd_nums = [x for x in my_list if x % 2]
    print(* even_nums)
    print(* odd_nums)