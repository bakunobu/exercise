def find_eight_pos(n:int) -> int:
    position = 0
    i = 0
    while n:
        num = n % 10
        if num == 8:
            position = i
        i += 1
    
    return(position)