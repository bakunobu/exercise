def brick_task(a: float, b:float, c:float,
               x:float, y:float) -> bool:
    min_x, min_y = sorted([a, b, c])[:2]
    return(max(x, y) > max(min_x, min_y) and min(x, y) > min(min_x, min_y))

