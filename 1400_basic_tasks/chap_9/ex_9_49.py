def is_prime(n:int) -> bool:
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                return(False)
            break
        else:
            return(True)


def divs(n:int) -> list:
    divs = []
    i = 2
    while i <= n:
        if is_prime(i):
            if not n % i:
                divs.append(i)
        i += 1
            
    
    return(divs)