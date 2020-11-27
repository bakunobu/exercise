"""
Меня вынесла формулировка.
На самом деле задание сводится к тому, что имеется последовательность
длиной 180 символов, в которой индекс есть у каждой пары чисел, например
номер элемента|->|индекс
1 -> 0
2 -> 0
3 -> 1
4 -> 1
5 -> 2
6 -> 2
и т.д.
"""
import doctest


# k = int(input())

# a
def find_index(k: int) -> int:
    """
    >>> find_index(1)
    0
    >>> find_index(2)
    0
    >>> find_index(3)
    1
    >>> find_index(4)
    1
    >>> find_index(5)
    2
    >>> find_index(6)
    2
    >>> find_index(180)
    89
    """
    return((k - 1) // 2)


# b
def find_num(k:int) -> int:
    """
    >>> find_num(1)
    10
    >>> find_num(2)
    10
    >>> find_num(3)
    11
    >>> find_num(4)
    11
    >>> find_num(5)
    12
    >>> find_num(6)
    12
    >>> find_num(180)
    99
    """
    return((k - 1) // 2 + 10)


# c_1
def find_even(k:int) -> int:
    """
    >>> find_even(2)
    0
    >>> find_even(4)
    1
    >>> find_even(6)
    2
    >>> find_even(180)
    89
    """
    return((k - 2) // 2)

#c_2
def find_odd(k:int) -> int:
    """
    >>> find_odd(1)
    0
    >>> find_odd(3)
    1
    >>> find_odd(5)
    2
    >>> find_odd(179)
    89
    """
    return((k-1) // 2)
    
    
if __name__ == "__main__":
    doctest.testmod()