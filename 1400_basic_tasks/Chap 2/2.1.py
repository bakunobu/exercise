# a

def equation_one(x: float) -> float:
    y = 17 * x ** 2 - 6 * x + 13
    return(float(y))

for x in (-7, 12, 3.5, 0):
    print(equation_one(x))
    
# b

def equation_two(a: float) -> float:
    y = 3 * a ** 2 + 5 * a - 21
    return(float(y))


for a in (-7, 12, 3.5, 0):
    print(equation_two(a))