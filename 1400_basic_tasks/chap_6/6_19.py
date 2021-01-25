def print_digits(n:int) -> None:
    while n:
        print(n % 10)
        n //= 10