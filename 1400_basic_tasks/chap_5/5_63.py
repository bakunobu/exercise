tot = 0

for n in range(20, 0, -1):
    if n == 2:
        tot += n 
    else:
        tot = tot ** 2 - n ** 2

print(tot)