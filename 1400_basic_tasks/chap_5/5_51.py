S = 100.0
V = 20.0

inc_S = 0.05
inc_V = 0.02


def calc_growth(p:float, i:float, t:int) -> float:
    return(p * (1 + i) ** t)


# a
for j in range(2, 9):
    print(j, calc_growth(V, inc_V, j))

    
# b
for i in range(4, 8):
    print(i, calc_growth(S, inc_S, i))
    

# c
total = 0
for y in range(6):
    crop = calc_growth(S, inc_S, y) * calc_growth(V, inc_V, y)
    total += crop

print(crop)