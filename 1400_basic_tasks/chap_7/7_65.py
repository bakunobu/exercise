def team_score(n:int) -> int:
    winning = 0
    msg = 'Введите количество побед и поражений команды (через пробел): '
    for _ in range(n):
        while True:
            try:
                win, lose = [int(x) for x in input(msg).split(' ')]
                if win > lose:
                    winning += 1
                break
            except ValueError:
                print('Используйте целые числа!')
    return(winning)

print(team_score(5))