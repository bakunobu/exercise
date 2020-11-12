"""
Составьте программу, выводящую пять рав­номерных случайных чисел типа flоаt от О.О до 1.0, их среднее,
минимальное и максимальное значения. Используйте встроенные функции min() и max().
"""


import random

def gen_and_summarize() -> tuple:
    """
    generates five uniformly distributed random numbers between 0.0 and 1.0
    
    Return:
    =======
    result: tuple
    min, max and mean of five nums
    """
    
    nums = [random.random() for i in range(5)]
    
    return(min(nums), max(nums), sum(nums)/len(nums))


# test
print(* gen_and_summarize())
