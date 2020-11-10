
from typing import Union

def euc_dist(list_a: list, list_b:list) -> Union[float, bool]:
    if len(list_a) != len(list_b):
        return(False)
    dist = sum(list((x - y) ** 2 for x, y in zip(list_a, list_b)))
    return(dist ** 0.5)

# testing
print(euc_dist([1, 2, 3], [3, 4, 5]))

print(euc_dist([1, 1, 1], [1, 1, 2]))

print(euc_dist([1, 1, 1], [1, 1, ]))