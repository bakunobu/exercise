def calc_points(num_judge:int=5) -> float:
    msg = 'Введите судейские оценки (через пробел)'
    points = [float(x) for x in input(msg).split(' ')]
    total = sum(points) - min(points) - max(points)
    return(total / num_judge - 2)


def calc_results(n:int, num_judge:int=5) -> None:
    for i in range(n):
        result = calc_points(num_judge)
        print(f'{i+1} спортсмен получил оценку: {result}')


