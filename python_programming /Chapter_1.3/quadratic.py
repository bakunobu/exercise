""" Составьте более общую и надежную версию программы для решения квадратного уравнения """

def sq_eq_solver(a: int, b: int, c: int) -> tuple:
    """
    A simple square equation solver (linear case included)
    
    Args:
    =====
    a: int
    coef a
    
    b: int
    coef b
    
    c: int
    coef c
    
    Return:
    =======
    result: tuple
    contains one or two elements (based on a number of solutions, None if no solutions)
    """
    
    if a == 0:
        return(tuple(-c / b, ))
    D = b ** 2 - (4 * a * c)
    if D < 0:
        print('No roots')
        return(None)
    elif D > 0:
        x_1 = (-b + D ** 0.5) / (2 * a)
        x_2 = (-b - D ** 0.5) / (2 * a)
        return((x_1, x_2,))
    else:
        return(tuple(-b / (2 * a)))