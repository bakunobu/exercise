from typing import Match


import math


def rectangle_params(a:float, b:float) -> tuple:
    p = 2 * a * b
    d = math.sqrt(a ** 2 + b ** 2)
    return(p, d)


a, b = 3, 4
p, d = rectangle_params(a, b)
print('A perimeter of a rectangle wih sides %.2f and %.2f is %.3f' 
      % (a, b, p))
print('A diagonal of a rectangle wih sides %.2f and %.2f is %.3f'
      % (a, b, d))
