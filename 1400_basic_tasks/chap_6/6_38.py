def find_three_pos(n:int) -> int:
    position = 0
    i = 0
    while n:
        num = n % 10
        if num == 3:
            position = i
            break
        i += 1
    
    return(position)