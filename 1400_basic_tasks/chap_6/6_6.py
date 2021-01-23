def find_fact(n:int) -> int:
    fact = 1
    i = 1
    while True:
        if fact == n:
            break
        i += 1
        fact *= i
    return(i)


