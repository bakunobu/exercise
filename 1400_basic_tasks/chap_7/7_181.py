from main_funcs import get_input


# a
def domino_series(n:int=20) -> bool:
    prev_tile = False
    for i in range(n):
        tile = get_input('Укажите номинал кости: ', False)
        a, b = tile // 10, tile % 10
        
        if not prev_tile:
            prev_tile = a, b
            
        else:
            if prev_tile[1] != b:
                return(False)
            
        
    return(True)


# b
def domino_series(n:int=20) -> bool:
    prev_tile = False
    for i in range(n):
        tile = get_input('Укажите номинал кости: ', False)
        a, b = tile // 10, tile % 10
        
        if not prev_tile:
            prev_tile = a, b
            
        else:
            cond_a = a in (prev_tile[0], prev_tile[1])
            cond_b = b in (prev_tile[0], prev_tile[1])
            if not cond_a or not cond_b:
                return(False)         
    
        
    return(True)