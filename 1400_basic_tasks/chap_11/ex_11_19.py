from math import factorial

def is_prime(x):
    return factorial(x - 1)  % x == x - 1

primes_gt_hund = []
x = 100
while len(primes_gt_hund) < 10:
    if is_prime(x):
        primes_gt_hund.append(x)
        
    x += 1
    
print(* primes_gt_hund)