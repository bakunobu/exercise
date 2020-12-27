def print_even(a:int, b:int, c:int) -> None:
    for x in (a, b, c):
        if x % 2 == 0:
            print(x)