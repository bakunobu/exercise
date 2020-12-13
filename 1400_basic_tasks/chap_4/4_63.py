def envelope_task(a:float, b:float,
                  c:float, d:float) -> bool:
    dim_1 = max(a, b) - max(c, d)
    dim_2 = min(a, b) - min(c, d)
    return(dim_1 > 1 and dim_2 > 1)