import math

def taylor_sine(x: float, i: int=20):
    return(sum([math.pow(-1, n) * (math.pow(x, (2 * n + 1)) / math.factorial(2 * n + 1)) for n in range(i)]))


# testing
print(taylor_sine(10))
print(math.sin(10))

