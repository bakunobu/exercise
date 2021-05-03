# a
def max_speed(speed:list) -> int:
    return(speed.index(max(speed)))


# b
def last_max_speed(speed:list) -> int:
    max_val = max(speed)
    speed_rev = speed[::-1]
    ind = speed_rev.index(max_val)
    return(len(speed) - ind - 1)
