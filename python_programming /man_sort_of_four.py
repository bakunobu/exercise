def sort_of_four(a: int, b: int, c: int, d: int) -> tuple:
    
    a, b = min(a, b), max(a, b)
    c, d = min(c, d), max(c, d)
    
    if b > c:
        b, c = c, b
        a, b = min(a, b), max(a, b)
        c, d = min(c, d), max(c, d)
    
    if b > c:
        b, c = c, b
    
    return(a, b, c, d)


# testing
from itertools import permutations
for _ in permutations([1, 2, 3, 4], 4):
    print('Input: ', * _)
    print('Result: ', * sort_of_four(* _))