def which_bigger(a:float, b:float, c:float) -> float:
    if a < b and b < c:
        return(c)
    elif a < c and c < b:
        return(b)
    elif b < a and a < c:
        return(c)
    elif b < c and c < a:
        return(a)
    elif c < a and a < b:
        return(b)
    else:
        return(a)
    
def prod_of_two(a:float, b:float, c:float) -> float:
    max_num = which_bigger(a, b, c)
    total = a * b * c
    return(total / max_num)