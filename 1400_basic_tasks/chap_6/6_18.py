import math

# a
def print_sqrt(a:int, b:int) -> None:
    while a > b:
        print(math.sqrt(a))
        a -= 1
        
        
# b
def print_sqrt_alt(a:int, b:int) -> None:
    while True:
        print(math.sqrt(a))
        a -= 1
        if a == b:
            break