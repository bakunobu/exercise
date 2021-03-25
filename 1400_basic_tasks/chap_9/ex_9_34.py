"""
у нас есть уравнение

10 * x_0 + 5 * x_1 + 2 * x_2 + x_3 = 100
x_0 >= 0
x_1 >= 0
x_2 >= 0
x_3 >= 0

Самый очевидный способ - перебором
"""

def main_func(x_0:int, x_1:int, x_2:int, x_3:int, res:int=100) -> bool:
    return(10 * x_0 + 5 * x_1 + 2 * x_2 + x_3 == res)


# a
def main_loop(res) -> int:
    counter = 0
    for x_0 in range(0, res // 10 + 1):
        for x_1 in range(0, res // 5 + 1):
            for x_2 in range(0, res // 2 + 1):
                for x_3 in range(0, res + 1):
                    if main_func(x_0, x_1, x_2, x_3, res):
                        counter += 1
    return(counter)



# b
def main_loop(res) -> int:
    combo = [] 
    for x_0 in range(0, res // 10 + 1):
        for x_1 in range(0, res // 5 + 1):
            for x_2 in range(0, res // 2 + 1):
                for x_3 in range(0, res + 1):
                    if main_func(x_0, x_1, x_2, x_3, res):
                        print('10: {}, 5: {}, 2: {}, 1: {}'.format(x_0, x_1, x_2, x_3))
                        combo.append((x_0, x_1, x_2, x_3))
    return(combo)

main_loop(100)