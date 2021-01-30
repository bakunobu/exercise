def if_nums_in(n:int, a: int=0, b:int=9) -> int:
    count_a = 0
    count_b = 9 
    
    while n:
        num = n % 10
        if num == a:
            count_a += 1
        elif num == b:
            count_b += 1
        n //= 10
    if count_a > count_b:
        return(a)
    else:
        return(b)