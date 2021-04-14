# a
def ar_prog(a:int, d:int, n:int) -> list:
    ar_prog_l = [a + d * i for i in range(n)]
    return(ar_prog_l)

# b
def geom_prog(m:int, d:int, n:int) -> list:
    geom_prog_l = [m * d ** i for i in range(n)]
    return(geom_prog_l)