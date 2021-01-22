import math

def least_than_squared(n:int) -> None:
    i = int(math.sqrt(n))
    for x in range(1, i+1):
        print(x)

