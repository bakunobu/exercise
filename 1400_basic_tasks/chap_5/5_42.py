def calc_route(n:int=100) -> float:
    dist = 0
    h_dist = 0
    for x in range(1, n+1):
        dist += 1/x
        h_dist -= (-1)**x * (1/x)
    return(dist, h_dist)


# a 
print(calc_route()[0])


# b
print(calc_route()[1])