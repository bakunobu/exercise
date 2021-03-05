import math

# a
def calc_pair_mean(n:int) -> int:
    pairs = []
    msg = "Введите пару чисел (разделитель - ','): "
    
    for _ in range(n):
        while True:
            try:
                a, b = [float(x) for x in input(msg).split(', ')]
            except ValueError:
                print('Используйте вещественные числа (разделитель - \',\')')
        pairs.append(a, b)
        
    pair_mean = [(x[0] + x[1]) / 2 for x in pairs]
    max_mean = max(pair_mean)
    ind = pair_mean[::-1].index(max_mean)
    
    return(len(pair_mean) - ind)


# b
def calc_pair_geom(n:int) -> int:
    pairs = []
    msg = "Введите пару чисел (разделитель - ','): "
    
    for _ in range(n):
        while True:
            try:
                a, b = [float(x) for x in input(msg).split(', ')]
            except ValueError:
                print('Используйте вещественные числа (разделитель - \',\')')
        pairs.append(a, b)
        
    pair_geom = [math.sqrt(x[0] * x[1]) for x in pairs]
    max_geom = max(pair_geom)
    ind = pair_geom[::-1].index(max_geom)
    
    return(len(pair_geom) - ind)