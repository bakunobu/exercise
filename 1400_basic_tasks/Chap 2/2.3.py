import math

# a
def solve_expr_one(a: float) -> float:
    expr_1 = 2 * a + math.sin(abs(3 * a))
    y = (expr_1 / 3.56) * 0.5
    return(y)


for a in (1, -1, 0, 10):
    print(solve_expr_one(a))
    
# b
def solve_expr_two(x: float) -> float:
    try:
        r = (3.2 + math.sqrt(1+x)) / abs(5 * x)
    except ZeroDivisionError:
        print('Деление на ноль невозможно!')
        return(None)
    y = math.sin(r)
    return(y)

for x in (1, -1, 0, 10):
    print(solve_expr_two(x))