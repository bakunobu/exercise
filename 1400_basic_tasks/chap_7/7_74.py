from main_funcs import get_input


def is_triangle(a:int, b:int, c:int) -> bool:
    cond_a = a < (b + c)
    cond_b = b < (a + c)
    cond_c = c < (a + b)
    return(cond_a and cond_b and cond_c)


def how_many_triangles(n:int) -> int:
    counter = 0
    msg = 'Введите стороны треугольника (через пробел): '
    for i in range(n):
        while True:
            try:
                a, b, c = [int(x) for x in input(msg).split(' ')]
                if is_triangle(a, b, c):
                    counter += 1
                break
            except ValueError:
                print('Используйте целые числа!')
    return(counter)