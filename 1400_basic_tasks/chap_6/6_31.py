P = 1000
r = 0.02

# a
m = 0
p = 0
while p <= 30:
    m += 1
    p = P * r
    P += p
print(m)

# b
P = 1000
m = 0
while P <= 1200:
    m += 1
    P += P * r
print(m)