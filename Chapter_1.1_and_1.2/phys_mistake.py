"""
Студент-физик получил неожиданный результат при использоваии кода 
force = G * mass1 * mass2 / radius * radius
для вычисления значения по формуле
F = G m_1 m_2 / r^2
Объясните проблему и исправьте код
"""

import math
import scipy.constants as const


def uni_grav(m_1:float, m_2:float, r:float, G:float=const.G) -> float:
    """
    The equasion for universal gravitation
    scipy.constants must be imported (import scipy.constants as const)
    """
    force = G * m_1 * m_2 / math.pow(r, 2)
    return(force)


# test
print(const.G)
print(uni_grav(1000000, 1000000, 2))
