from main_funcs import get_input


def game_results(n:int) -> tuple:
    res_dict = {3:0,
                   1:0,
                   0:0}
    
    for x in range(n):
        result = get_input('Укажите количество очков: ', False)
        res_dict[result] += 1
    
    return(res_dict[3],
           res_dict[1],
           res_dict[0])