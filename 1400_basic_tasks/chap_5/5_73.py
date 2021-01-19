import math

def find_other_side(c:float, a:float) -> float:
    """
    Finds an unknown leg of a triangle
    Args:
    =====
    c: float
    a hypotenuse
    a: float
    a known leg of a triangle
    """
    return(math.sqrt(c ** 2 - a ** 2))


def calc_cos(c:float, b:float) -> float:
    """
    Args:
    =====
    b:float
    adjasent
    c:float
    hypotenuse
    """
    return(b / c)



def calc_acos_deg(my_cos:float) -> float:
    return(math.degrees(math.acos(my_cos)))




a = find_other_side(4.5, 3)

while a >= 0.2:
    
    b = find_other_side(4.5, a)
    angle = calc_acos_deg(calc_cos(4.5, b))
    print(f'Длина a: {round(a, 3)}', end='->')
    print(f'Угол {round(angle, 3)}')
    a -= 0.2


 