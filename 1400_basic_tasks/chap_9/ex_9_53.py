def first_cubes_sum():
    cubes = [i ** 3 for i in range(1, 100)]
    for a in cubes:
        for b in cubes:
            for c in cubes:
                for d in cubes:
                    if a + b == c + d:
                        if len(set((a, b, c, d))) == 4:
                            return(a+b)


print(first_cubes_sum())