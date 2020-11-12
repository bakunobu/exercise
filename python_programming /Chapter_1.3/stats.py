""" Обобщая упражнение о равномерных случайных  числах,
составьте программу stats.ру, получающую в аргумен­те
командной строки целое число n и использующую функцию
random.random ( ) для вывода n равномерно случайных
чисел от О до 1, а затем вы­водящую их среднее,
минимальное и максимальное значения """


import random

def random_min_max_mean(n: int) -> None:
    """
    Generates n random nums
    Prints min, max and mean of a list
    
    Args:
    =====
    n: int
    number of numbers to be generated
    
    Return:
    =======
    None: None
    Prints results
    """
    
    total = 0
    min_x = 1
    max_x = 0
    for x in range(n):
        x = random.random()
        total += x
        min_x = min(min_x, x)
        max_x = max(max_x, x)
    print('Mean: {:.3f}\nmin: {:.3f}\nmax: {:.3f}'.format(total / n, min_x, max_x))