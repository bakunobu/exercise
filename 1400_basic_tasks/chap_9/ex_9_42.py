def all_three_digits():
    for x in range(1, 10):
        for y in range(1, 10):
            for z in range(1, 10):
                if x != y and x != z and y != z:
                    print(x * 100 + y * 10 + z)
                    

all_three_digits()