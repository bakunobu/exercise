import random


# a
def simple_math_question() -> bool:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    msg = f'Чему равно произведение {a} и {b}? '
    while True:
        try:
            r = int(input(msg))
            print(r)
            if r == 0:
                return(-1)
            elif r > 0:
                print(r == a * b)
                return(r == a * b)
            
        except ValueError:
            print('Используйте только натуральные числа')
            
            
def one_round_game() -> None:
    if simple_math_question():
        print('Это правильный ответ!')
    else:
        print('Неправильный ответ!')
        
        
# b
def play_n_times(n:int=20) -> None:
    score = {1:0,
             0:0}
    for i in range(n):
        if simple_math_question():
            print('Это правильный ответ!')
            score[1] += 1
        else:
            print('Неправильный ответ!')
            score[0] += 1
    print(f'Всего правильных ответов: {score[1]}, неправильных: {score[0]}')
    

# play_n_times(5)

# c
def infinite_play() -> None:
    score = {1:0,
             0:0}
    while True:
        answer = simple_math_question()
        if answer == -1:
            print('Quiting')
            break
        elif answer == True:
            score[1] += 1
            print('Good!')
        else:
            score[0] += 1
            print('Not good!')
            

    print(f'Всего правильных ответов: {score[1]}, неправильных: {score[0]}')
    
    
infinite_play()
