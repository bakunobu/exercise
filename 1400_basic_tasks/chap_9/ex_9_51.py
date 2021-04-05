import math


def mut_prime_list(n:int, p:int) -> list:
    mut_primes = [i for i in range(n) if math.gcd(i, p) == 1]
    return(mut_primes)