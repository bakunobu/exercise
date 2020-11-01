""" Модифицируйте свое решение упражнения о непрерывно начисляемом сложном проценте из раздела так,
чтобы оно выво­дило таблицу с общей суммой выплат и остающейся основной суммой вклада после каждой ежемесячной выплаты.  """

def calc_anuuity_monthly(K: float, P: float) -> float:
    """
    Calculates an annuity
    
    Args:
    =====
    P: float
    a principal
    K: float
    an annuity
    
    Return:
    =======
    x: float
    a monthly payment
    """
    x = K * P
    return(x)


def calc_annuity(i: float, n: int) -> float:
    """
    Calculates annuity
    
    Args:
    ====
    i: float
    an interest rate (yearly)
    n: int
    period (in months)
    
    Return:
    =======
    K: float
    an annuity
    
    """
    i_m = i / 12
    expr_1 = (i_m * (1 + i_m)**n)
    expr_2 = (1 + i_m) ** n - 1
    K = expr_1 / expr_2
    return(K)


def credit_calc(P: float, i: float, n: int) _-> None:
    """
    A credit calculator for annual payments
    
    Args:
    =====
    P: float
    a principal
    
    i: float
    an interest rate (yearly)
    
    n: int
    period (in months)
    
    Return:
    =======
    None: None
    prints a table
    """
    
    i_m = i / 12
    K = (i_m * (1 + i_m)**n) / ((1 + i_m) ** n - 1)
    x = K * P
    