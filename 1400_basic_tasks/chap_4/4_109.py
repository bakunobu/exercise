def print_int(a:float, b:float, c:float,
              min_v:float=1.6, max_v:float=3.8) -> None:
    for x in (a, b, c):
        if min_v <= x <= max_v:
            print(x) 