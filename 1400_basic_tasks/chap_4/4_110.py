def how_many_pos(a:float, b:float, c:float, d:float) -> int:
    counter = 0
    if a >= 0:
        counter += 1
    if b >= 0:
        counter += 1
    if c >= 0:
        counter += 1
    if d >= 0:
        counter += 1
    return(counter)