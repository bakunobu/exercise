def sum_greater_five(a:float, b:float, c:float, d:float) -> float:
    total = 0
    if a > 5:
        total += a
    if b > 5:
        total += b
    if c > 5:
        total += c
    if d > 5:
        total += d
    return(total)