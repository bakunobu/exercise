def how_many_even(a: int, b:int, c: int, d: int) -> int:
    res = [1 if x % 2 == 0 else 0 for x in (a, b, c, d)]
    return(sum(res))