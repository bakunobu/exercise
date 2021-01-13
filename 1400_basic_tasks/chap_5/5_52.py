import math


def calc_vol(r:float) -> float:
    return((4/3) * math.pi * r ** 3)


def cube_cm_to_liters(v:float) -> float:
    return(v / 1000)
    

r = 0
total_vol = 0

for x in range(12):
    v = calc_vol(r)
    r += 5
    total_vol += v


print(cube_cm_to_liters(total_vol))