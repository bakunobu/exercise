def pos_sum(a:float, b:float, c:float) -> float:
    total = 0
    for x in (a, b, c):
        if x > 0:
            total += x
    return(total) 