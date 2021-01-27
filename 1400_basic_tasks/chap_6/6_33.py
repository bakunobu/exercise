def square_prog(s: float, r:float=0.05) -> float:
    r += 1
    return(s * r)

def crop_prog(y: float, i:float=0.02) -> float:
    i += 1
    return(y * i)

# a
t = 0
y = 20
while y <= 22:
    t += 1
    y = crop_prog(y)
    
print(t)

# b
t=0
a = 100
while a <= 120:
    t += 1
    a = square_prog(a)
    
print(t)


# c
t = 0
y = 20
a = 100
crop = 0
while crop <= 800:
    t += 1
    crop += a * y
    a = square_prog(a)
    y = square_prog(y)


print(t)    