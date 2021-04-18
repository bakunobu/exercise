import math
from typing import Union

# a
def list_el_sqrt(my_list:list, num_el:int) -> Union[float, bool]:
    try:
        return(math.sqrt(my_list[num_el]))
    except IndexError:
        print('Index is out of range')
        return(False)
    
    
# b
def mean_two_els(my_list:list, num_el_a:int,
                 num_el_b:int) -> Union[float, bool]:
    try:
        return((my_list[num_el_a] + my_list[num_el_b])/2)
    except IndexError:
        print('Index is out of range')
        return(False)
     