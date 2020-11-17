import math

def find_c(a: float, b: float) -> float:
    c = math.sqrt(a ** 2 + b ** 2)
    return(c)

def find_p(a: float, b: float) -> float:
    c = find_c(a, b)
    return(sum((a, b, c)))


print(find_p(3, 4))

