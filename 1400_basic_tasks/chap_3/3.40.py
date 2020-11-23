n = 654
last_dig = 654 // 100
n = 654 % 100
mid_dig = n % 10
first_dig = n // 10

n = last_dig + mid_dig * 10 + first_dig * 100
print(n)