# a
def is_cont_three(x:int) -> bool:
    tens = x // 10
    units = x % 10
    return(tens == 3 or units == 3)


# b
def is_cont_a(x:int, a:int) -> bool:
    tens = x // 10
    units = x % 10
    return(tens == a or units == a)