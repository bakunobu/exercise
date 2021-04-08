import numpy.random as npr

#
def basic_input():
    msg = '«Чет (введите 2) или нечет (введите 1)?» '
    try:
        a = int(input(msg))
        if a in (1,2):
            return(a)
        else:
            print('Используйте числа 1 и 2!')
    except ValueError:
        print('Используйте только целые числа (1 и 2)!')
        
        
def exit_option(msg:str='Сыграть еще раз? ') -> bool:
    resp = input(msg).lower()
    if resp == 'нет':
        return(True)
    else:
        return(False)


def game_logic(a:int) -> bool:
    num = npr.randint(1,3)
    return(a == num)


def game_loop(n:int=1, game_score:bool=False) -> None:
    score = {'Computer': 0,
             'Player': 0}
    
    for i in range(n):
        a = basic_input()
        res = game_logic(a)
        if res:
            print('Player wins')
            score['Player'] += 1
        else:
            print('Computer wins')
            score['Computer'] += 1
    
    if game_score:
        print(f'{n} games played')
        print('Score:')
        for k, v in score.items():
            print(f'{k}: {v}')
        if score['Player'] > score['Computer']:
            print('Player wins!')
        elif score['Player'] < score['Computer']:
            print('Computer wins!')
        else:
            print('Draw!')
            
            
# a
game_loop()


# b
n = int(input('Укажите количество партий: '))
game_loop(n=n, game_score=True)


# c

def adv_game_loop(game_score:bool=False) -> None:
    counter = 1
    score = {'Computer': 0,
             'Player': 0}
    
    while 1:
        a = basic_input()
        res = game_logic(a)
        counter += 1
        if res:
            print('Player wins')
            score['Player'] += 1
        else:
            print('Computer wins')
            score['Computer'] += 1
        if exit_option():
            break
    
    if game_score:
        print(f'{counter} games played')
        print('Score:')
        for k, v in score.items():
            print(f'{k}: {v}')
        if score['Player'] > score['Computer']:
            print('Player wins!')
        elif score['Player'] < score['Computer']:
            print('Computer wins!')
        else:
            print('Draw!')