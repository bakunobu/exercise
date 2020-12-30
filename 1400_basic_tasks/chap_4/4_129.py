def which_smaller(a:float, b:float, c:float) -> float:
    if a < b and b < c:
        return(a)
    elif a < c and c < b:
        return(a)
    elif b < a and a < c:
        return(b)
    elif b < c and c < a:
        return(b)
    elif c < a and a < b:
        return(c)
    else:
        return(c)
    
def find_sum(a:float, b:float, c:float) -> float:
    min_dig = which_smaller(a, b, c)
    total  = a + b + c - min_dig
    return(total)