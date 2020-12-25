# a
def greater_of_four(a:float, b:float, c:float, d:float) -> float:
    if a > b and c > d:
        if a > c:
            return(a)
        return(c)
    if a < b and c < d:
        if b < d:
            return(d)
        return(b)
    if a > b and c < d:
        if a > d:
            return(a)
        return(d)
    if a < b and c > d:
        if b > c:
            return(b)
        return(c)
    
    def lesser_of_four(a:float, b:float, c:float, d:float) -> float:
        if a < b and c < d:
            if a < c:
                return(a)
            return(c)
        if a > b and c > d:
            if b > d:
                return(d)
            return(b)
        if a > b and c < d:
            if b > c:
                return(c)
            return(b)
        if a < b and c > d:
            if a > d:
                return(d)
            return(a)