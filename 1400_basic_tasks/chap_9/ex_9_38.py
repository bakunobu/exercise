def find_eq_solution(a:int=1, b:int=30) -> list:
    x_y_vals = []
    k_vals = [x ** 2 for x in range(a, b)]
    for x in range(a, b):
        for y in range(a, b):
            k = x ** 2 + y ** 2
            if k in k_vals:
                if (y, x) not in x_y_vals:
                    x_y_vals.append((x, y))
    return(x_y_vals)


