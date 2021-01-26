S = 10
r = 0.1
 
# a
m = 0

while S <= 20:
    m += 1
    S *= 1.1
print(m)

# b
S = 10
dist = 0
m = 0
while dist <= 100:
    m += 1
    dist += S
    S *= 1.1
print(m)
    
    