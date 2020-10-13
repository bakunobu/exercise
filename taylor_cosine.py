import math

def taylor_cosine(x: float, i: int=20):
    return(sum([math.pow(-1, n) * (math.pow(x, (2 * n)) / math.factorial(2 * n)) for n in range(i)]))


# testing
print(taylor_cosine(10))
print(math.cos(10))
