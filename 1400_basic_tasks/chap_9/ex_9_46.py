def dig_sum(x:int) -> int:
    digs = []
    while x:
        a = x % 10
        x //= 10
        digs.append(a)
    return(sum(digs))


def dig_root(n:int) -> int:
    while n >= 10:
        n = dig_sum(n)
    return(n)

