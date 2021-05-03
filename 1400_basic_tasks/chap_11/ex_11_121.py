# a
def rainy_day(moist:list) -> int:
    return(moist.index(max(moist)))


# b
def last_rainy_day(moist:list) -> int:
    max_moist = max(moist)
    for x in range(len(moist) - 1, 0, -1):
        if moist[x] == max_moist:
            return(x)
    return(0)