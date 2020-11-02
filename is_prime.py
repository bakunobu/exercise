def is_prime(n: int) -> list:
    primes = []
    nums = [x for x in range(2, n]
    while nums:
        i = nums.pop(0)
        primes.append(i)
        nums = [x for x in nums if x % i != 0]
    return(primes)