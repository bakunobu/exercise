import numpy.random as npr


def dice() -> int:
    return(npr.randint(1,7))


def gamify() -> None:
    player_1 = dice()
    player_2 = dice()
    if player_1 > player_2:
        print('Player 1 wins!')
    elif player_1 < player_2:
        print('Player_2 wins!')
    else:
        print('Draw!')