n = 564
first_digit = n % 10
n //= 10
n += first_digit * 100

print(n)