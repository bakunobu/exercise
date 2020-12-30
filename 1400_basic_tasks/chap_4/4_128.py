def min_max_three(a:float, b:float, c:float) -> None:
    if a > b and b > c:
        print(f'Max: {a}, min: {c}')
    elif a > b and b < c:
        print(f'Max: {a}, min: {b}')
    elif a < b and b < c:
        print(f'Max: {c}, min: {a}')
    elif a < c and b > c:
        print(f'Max: {b}, min {a}')
    elif a > c and a < b:
        print(f'Max {b}, min: {c}')
    else:
        print(f'Max{c}, min {b}')