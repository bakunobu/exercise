def sum_dev_three(a:float, b:float, c:float, d:float) -> float:
    total = 0
    if a % 3 == 0:
        total += a
    if b % 3 == 0:
        total += b
    if c % 3 == 0:
        total += c
    if d % 3 == 0:
        total += d
    return(total)