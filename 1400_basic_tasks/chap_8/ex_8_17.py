import fractions
from fractions import Fraction



def calc_seq(eps:float=0.001) -> fractions.Fraction:
    prev_num = 1
    prev_den = 1
    num = 2
    den = 1
    while abs((num / den) - (prev_num / prev_den)) > eps:
        prev_num, num = num, prev_num + num
        prev_den, den = den, prev_den + den
    return(Fraction(num, den))

print(calc_seq())