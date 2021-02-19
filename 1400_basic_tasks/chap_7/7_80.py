from main_funcs import get_input


def calc_score() -> tuple:
    msg = 'Укажите количество забитых и промущенных мячей (разделитель - пробел): '
    try:
        while True:
            scored, failed = [int(x) for x in input(msg).split(' ')]
            return(scored, failed)
    except ValueError:
        print('Используйте пары целых чисел!')

        
# a
def print_result(score:tuple) -> None:
    if score[0] > score[1]:
        print('Победа')
    elif score[0] < score[1]:
        print('Поражение')
    else:
        print("Ничья")
        
        
for x in range(20):
    score = calc_score()
    print_result(score)


# b
def calc_wins(n:int=20) -> int:
    wins = 0
    for _ in range(n):
        score = calc_score()
        if score[0] > score[1]:
            wins += 1
    return(wins)


# c
def calc_wins_n_loses(n:int=20) -> tuple:
    wins = 0
    loses = 0
    for _ in range(n):
        score = calc_score()
        if score[0] > score[1]:
            wins += 1
        elif score[0] < score[1]:
            loses += 1
    return(wins, loses)


# d
def calc_all_res(n:int=20) -> tuple:
    wins = 0
    loses = 0
    draws = 0
    for _ in range(n):
        score = calc_score()
        if score[0] > score[1]:
            wins += 1
        elif score[0] < score[1]:
            loses += 1
        else:
            draws += 1
    return(wins, loses, draws)


# e
def goal_diff(n:int=20, g:int=3) -> int:
    diff_pos = 0
    for _ in range(n):
        score = calc_score()
        if abs(score[0] - score[1]) >= 3:
            diff_pos += 1
    return(diff_pos)


# f
def calc_points(n:int) -> int:
    win, lose, draw = calc_all_res(n)
    return(win * 3 + draw)

           