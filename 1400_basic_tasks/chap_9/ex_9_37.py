# a
def find_sides(v:int) -> list:
    sides = []
    for a in range(1, v+1):
        for b in range(1, v+1):
            for c in range(1, v+1):
                if a * b * c == v:
                    sides.append((a, b, c))
    return(sides)


# b
def find_dif_sides(v:int) -> list:
    sides = []
    for a in range(1, v+1):
        for b in range(1, v+1):
            for c in range(1, v+1):
                if a * b * c == v:
                    s = sorted([a, b, c])
                    if s not in sides:
                        sides.append(s)
    return(sides)


print(find_sides(100))
print(find_dif_sides(100))