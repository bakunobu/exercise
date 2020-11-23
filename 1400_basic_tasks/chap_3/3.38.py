n = 456
mid_dig = n %10
n //= 10
first_dig = n // 10
last_dig =  n % 10

n = last_dig + mid_dig * 10 + first_dig * 100
print(n)