def print_nums(a:int, b:int, c:int) -> None:
    for x in range(a, b+1):
        if x % c == 0:
             print(x)