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
    while n > 1 and i <= n:
        if is_prime(i):
            if n % i == 0:
                divs.append(i)
                n //= i
                
        
        else:
            i += 1
            
    
    return(divs)
# a
print(set(divs(256)))


# b
print(divs(256))