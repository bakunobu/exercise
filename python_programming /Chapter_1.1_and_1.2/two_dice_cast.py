"""
Составьте программу, выводящую сумму двух случайных целых чисел от 1 до 6
(как при бросании кубика)
"""

import random

def cast_dice(n:int=2) -> int:
    """
    Returns the sum of n die cast
    
    Args:
    =====
    n: int
    A number of dice
    
    Return:
    =======
    cast_sum: int
    a sum of two dice cast
    """
    casts = [random.randint(1, 6) for i in range(n)]
    cast_sum = sum(casts)
    
    return(cast_sum)


# test

print(cast_dice())
