total = 0

for x in range(1, 11):
    mult = (-1) ** x
    num = mult * x ** 2
    total += num

print(total)