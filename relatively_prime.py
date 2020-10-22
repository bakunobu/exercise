import math


n = int(input())

a = [[0 for i in range(n)] for j in range(n)]

b = []

for i in range(n):
    row = [math.gcd(i, j) == 1 for j in range(n)]
    b.append(row)


print(b)