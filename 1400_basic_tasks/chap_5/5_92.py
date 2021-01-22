def gen_primes(n:int) -> list:
    primes = []
    nums = [x for x in range(2, n)]
    while nums:
        i = nums.pop(0)
        primes.append(i)
        nums = [x for x in nums if x % i != 0]
    return(primes)


def is_prime(n:int) -> bool:
    primes = gen_primes(n+1)
    if n in primes:
        return(True)
    else:
        return(False)
    
    
print(100, is_prime(100))
print(2, is_prime(2))
print(3, is_prime(3))
print(4, is_prime(4))
print(5, is_prime(5))