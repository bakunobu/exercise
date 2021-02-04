def draw_hedge(a:int=4, b:int=6) -> int:
    a, b = min(a, b), max(a, b)
    line = 0
    cut = 0
    while cut <= a:
        if cut == 0:
            cut += 1
            line += a - cut
        cut += 1
        line += b - cut
        line += a - cut
    return(line)        
    
    