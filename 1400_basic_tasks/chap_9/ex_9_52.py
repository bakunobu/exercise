import math


def mut_prime_divs(n:int, q:int) -> list:
    mut_primes = [i for i in range(1, n) if math.gcd(i, q) == 1 and not n % i]
    return(mut_primes)