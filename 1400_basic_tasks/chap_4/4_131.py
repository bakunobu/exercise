def which_median(a:float, b:float, c:float) -> float:
    if a < b and b < c:
        return(b)
    elif a < c and c < b:
        return(c)
    elif b < a and a < c:
        return(a)
    elif b < c and c < a:
        return(c)
    elif c < a and a < b:
        return(a)
    else:
        return(b)
    

def calc_mean(a:float, b:float, c:float,
              d:float, e:float, f:float) -> float:
    median_1 = which_median(a, b, c)
    median_2 = which_median(d, e, f)
    return((median_1 + median_2) / 2)