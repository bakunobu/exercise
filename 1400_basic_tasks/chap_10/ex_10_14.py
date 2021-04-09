import numpy.random as npr


def dice() -> int:
    return(npr.randint(1,7))


def three_player_game(k:int) -> None:
    player_1 = sum([dice() for i in range(k)])
    player_2 = sum([dice() for i in range(k)])
    player_3 = sum([dice() for i in range(k)])
    if player_1 > player_2 and player_1 > player_3:
        print('Player_1 wins!')
    elif player_2 > player_1 and player_2 > player_3:
        print('Player 2 wins!')
    elif player_3 > player_1 and player_3 > player_2:
        print('Player 3 wins!')
    else:
        print('It\'s a draw!')
