import math


def air_dense(h:int) -> float:
    p_0 = 1.29
    z = 1.25 * 10 ** -4
    power = -1 * h * z
    return(p_0 * math.exp(power))


def print_density() -> None:
    for x in range(0, 1001, 100):
        print(f'{x} m - {air_dense(x)}')   