def num_divisors(n:int) -> list:
    divs = [x for x in range(1, n) if n % x == 0]
    return(divs)


n = 6

if n == sum(num_divisors(n)):
    print('Perfect')
else:
    print('Not Perfect')