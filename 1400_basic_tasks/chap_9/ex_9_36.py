import math
from typing import Union


def is_int(x:Union[int, float]) -> bool:
    return(int(x) == float(x))
    

# a
def find_num_rect(s:int):
    rects = []
    for i in range(1, s+1):
        if is_int(s / i):
            rects.append((i, s // i))
    return(rects)

# print(* find_num_rect(100), sep='\n')

# b
def find_num_un_rect(s:int):
    rects = []
    m = int(math.sqrt(s)) + 1
    for i in range(1, m):
        if is_int(s / i):
            rects.append((i, s // i))
    return(rects)

# rint(* find_num_un_rect(102), sep='\n')