import math


def eucl_dist(a:tuple, b:tuple) -> float:
    d_1 = (a[0] - b[0]) ** 2
    d_2 = (a[1] - b[1]) ** 2
    d = math.sqrt(d_1 + d_2)
    return(d)

print(eucl_dist([0,0], [2,2]))
