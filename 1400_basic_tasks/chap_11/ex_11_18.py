# a
def cond_one(x:int) -> bool:
    return(not x % 13 and not x % 17)

nums = []
x = 300

while len(nums) < 20:
    if cond_one(x):
        nums.append(x)
    x += 1

# print(nums)

# b
def first_n_primes(n:int=30) -> list:
    primes = [2]
    i = 3
    while len(primes) < n:
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
        i += 1
    return(primes) 
        
print(first_n_primes())