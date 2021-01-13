total = 0

for x in range(2, 11):
    num = 1
    for i in range(x):
        num *= 2
    total += num

print(total)