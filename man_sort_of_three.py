def sort_of_three(a: int, b: int, c: int) -> tuple:
    a, b = min(a, b), max(a, b)
    
    if b > c:
        b, c = c, b
        a, b = min(a, b), max(a, b)

    return(a, b, c)

# testing
from itertools import permutations
for _ in permutations([1, 2, 3], 3):
    print('Input: ', * _)
    print('Result: ', * sort_of_three(* _))
