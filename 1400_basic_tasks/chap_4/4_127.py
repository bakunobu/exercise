# a
def which_bigger(a:int, b:int, c:int) -> int:
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

# b
def which_smaller(a:int, b:int, c:int) -> int:
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

# c
def which_median(a:int, b:int, c:int) -> int:
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