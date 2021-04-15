# a

def print_pos(my_list:list) -> None:
    pos_list = [x for x in my_list if x >= 0]
    print(* pos_list)
    
    
# b
def print_le_hund(my_list:list) -> None:
    le_hund = [x for x in my_list if x <= 100]
    print(* le_hund)  