""" Составьте программу,  получающую в  аргументах командной строки n
и выводящую все положительные степени числа 2, меньшие или равные n.
Удостоверьтесь, что программа работает правильно для всех значений n.
(Для отрицательных n программа не должна выводить ничего.) """

import math

def pos_power(n: int) -> None:
    """
    prints 2 ^ m for all 2 ^ m < n
    
    Args:
    n: int
    an upper limit (must be positive)
    
    Return:
    =======
    None: None
    """
    if n < 0:
        print('Hey')
    else:
        for x in range(0, int(math.pow(n, 0.5)+1)):
            if 2 ** x < n:
                print(2 ** x)

# Test
pos_power(-2)

pos_power(1025)

