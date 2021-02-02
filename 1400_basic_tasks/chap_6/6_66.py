def eucl_gcd(a:int, b:int) -> int:
    while a > 0 and b > 0:
        a, b = min(a, b), max(a, b) % min(a, b)
    return(a)


def gcd_three_el(a:int, b:int, c:int) -> int:
    return(eucl_gcd(eucl_gcd(a, b), c))


