# a

def print_even(my_list:list) -> None:
    even_nums = [x for x in my_list if not x % 2]
    print(* even_nums)
    
    
# b
def print_dec(my_list:list) -> None:
    dec_nums = [x for x in my_list if not x % 10]
    print(* dec_nums)