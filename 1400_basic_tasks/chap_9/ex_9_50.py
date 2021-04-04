import math


def mut_prime_list(n:int) -> list:
    mut_primes = [(i,n) for i in range(n) if math.gcd(i, n) == 1]
    return(mut_primes)