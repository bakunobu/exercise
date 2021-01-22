
def num_divisors(n:int) -> list:
    divs = [x for x in range(1, n+1) if n % x == 0]
    return(divs)

n = 102
 
# a 
all_divs = num_divisors(n)
print(all_divs)

# b
print(sum(all_divs))

# c
def num_divs_even(n:int) -> list:
    even_divs = [x for x in range(2, n+1, 2) if n % x == 0]
    return(even_divs)

even_divs = num_divs_even(n)
print(sum(num_divs_even(n)))

# d
print(len(all_divs))

# e
print(len(all_divs) - len(even_divs))

# f
print(len(all_divs), len(even_divs))

# g
def num_divs_big(n:int, d:int) -> list:
    divs = [x for x in range(d, n+1) if n % x == 0]
    return(divs)