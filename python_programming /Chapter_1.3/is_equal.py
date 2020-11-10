"""
Составьте программу, получающую в командной строке три целочислен­ных аргумента и выводящую слово 'equal', 
если все три равны, и 'not equal' в противном случае. 
"""


def is_equal(a: int, b: int, c: int) -> None:
    """
    checks if number one is equal both to number two and three
    
    Args:
    =====
    a: int
    number one
    b: int
    number two
    c: int
    number three
    
    Return:
    =======
    None: None
    but print 'equal' if the statement is correct and 'not equal' otherwise
    """
    
    if a == b == c:
        print('equal')
    else:
        print('not equal')