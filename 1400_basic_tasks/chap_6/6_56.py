def two_five_pos(n:int) -> int:
    pos_two = 0
    pos_five = 0
    i = 0
    while n:
        num = n % 10
        if num == 2:
            pos_two = i
        elif num == 5:
            pos_five = i
        n //= 10
        i += 1
    if pos_two > pos_five:
        return(2)
    else:
        return(5)