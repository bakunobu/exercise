import random


def auto_true_false_replace(n:int=4, m:int=3) -> None:

    line = [bool(random.getrandbits(1)) for x in range(n)]
    my_list = [line for _ in range(m)]


    for i in range(len(my_list)):
        for j in range(len(line)):
            print(i, '-', j, end=' - ')
            if my_list[i][j]:
                print('*')
            else:
                print('_')
                
auto_true_false_replace()