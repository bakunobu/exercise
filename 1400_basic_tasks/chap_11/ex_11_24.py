# a

def print_two_digs(my_list:list) -> None:
    two_nums = [x for x in my_list if 10 <= x < 100]
    print( * two_nums)
    
    
# b
def print_three_digs(my_list:list) -> None:
    three_nums = [x for x in my_list if 100 <= x < 1000]
    print(* three_nums)