n = 546

mid_dig = n // 100
n %= 100
first_dig = n // 10
last_dig = n % 10

print(last_dig + mid_dig * 10 + first_dig * 100)
