def two_five_pos(n:int, a:int, b:int) -> int:
    pos_a = None
    pos_b = None
    i = 0
    while n:
        num = n % 10
        if num == a:
            if not pos_a:
                pos_a = i
        elif num == b:
            if not pos_b:
                pos_b = i
        n //= 10
        i += 1
    if pos_a > pos_b:
        return(b)
    else:
        return(a)