import numpy.random as npr
import time

def dice() -> int:
    return(npr.randint(1,7))


# a
def two_cast_game() -> None:
    player_1 = [dice() for x in range(2)]
    player_2 = [dice() for x in range(2)]
    if sum(player_1) > sum(player_2):
        print('Player 1 wins!')
    elif sum(player_1) < sum(player_2):
        print('Player 2 wins!')
    else:
        print('Draw!')
        
# b
def cont_game(n:int) -> None:
    scores = {'p_1': 0,
              'p_2': 0,
              'draw': 0}
    for i in range(n):
        print(f'Round {i+1}')
        player_1 = dice()
        print(f'Player 1 scores {player_1}!')
        player_2 = dice()
        print(f'Player 2 scores {player_2}!')
        
        if player_1 > player_2:
            print('Player 1 wins this round!')
            scores['p_1'] += 1
        elif player_2 > player_1:
            print('Player 2 wins this round!')
            scores['p_2'] += 1
        else:
            print('It\'s a tie!')
            scores['draw'] += 1
        time.sleep(1)
    if scores['p_1'] > scores['p_2']:
        print(f'Player 1 wins this game')
    elif scores['p_1'] < scores['p_2']:
            print(f'Player 2 wins this game')
    else:
        print('Draw')
    
    print('Score:')
    print(f'Player_1: {scores["p_1"]}')
    print(f'Player_2: {scores["p_2"]}')
    print(f'Draws: {scores["draw"]}')
    
    
cont_game(10)