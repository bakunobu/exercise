def will_it_fit(a:float, b:float,
                c:float, d:float) -> bool:
    return(max(a,b) > max(c,d) and min(a,b) > min(c,d))