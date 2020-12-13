def pave_rect(a: int, b:int,
              c:int, d:int) -> int:
    x = a // c
    y = b // d
    return(x * y)


def compare(a: int, b:int,
              c:int, d:int) -> str:
    solution_1 = pave_rect(a,b,c,d)
    solution_2 = pave_rect(a,b,d,c)
    if solution_1 > solution_2:
        return('Solution 1')
    else:
        return('Solution 2')
    
    
def domino_pavement(a:float, b:float,
                    c:float, d:float, e:float) -> str:
    x, y = sorted([c, d, e])[:2]
    compare(a, b, x, y)