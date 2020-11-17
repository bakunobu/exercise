r = 6350 * 10**3

def hor_dist(h:float) -> float:
    D = ((r+h) ** 2 - r ** 2) ** 0.5
    return(D)


print(round(hor_dist(1.8), 3))