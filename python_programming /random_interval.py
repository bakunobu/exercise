"""
Составьте прогрмму, получающую в аргументах командной строки два целых числа, a и b,
и выводящую случайное целое число в диапазоне от a до b.
"""

import sys
import random

def return_rand(a:int, b:int) -> int:
    """
    A random number from the given interval
    """
    return(random.randint(int(a), int(b)))

print(return_rand(sys.argv[1], sys.argv[2]))