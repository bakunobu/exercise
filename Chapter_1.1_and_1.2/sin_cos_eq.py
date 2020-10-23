import math

def check_eq(theta, epsilon:float=1e-6) -> bool:
    """
    Proves that sin(x)^2 + cos(x)^2 == 1.
    
    Args:
    =====
    theta: int or float
    angle in degrees
    
    epsilon: float
    an error estimation for the float's comparison
    
    Returns:
    ========
    bool
    True in case the equasion is correct
    """
    eq = math.sin(theta) ** 2 + math.cos(theta) **2
    return(abs(1 - eq) <= epsilon)


# test

for x in (0, 35.5, 47, 90, 180, 282):
    print(check_eq(x))