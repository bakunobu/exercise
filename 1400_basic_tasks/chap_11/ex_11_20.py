import random


def get_input(msg:str) -> int:
    while True:
        try:
            resp = int(input(msg))
            if resp > 0:
                return(resp)
        except ValueError:
            print('Используйте только натуральные числа!')
            

def prod_checker(n:int=20) -> None:
    answers = []
    corr_answ = []
    for i in range(n):
        a = random.randint(1,10)
        b = random.randint(1, 10)
        msg = f'Чему равно произведение {a} и {b}? '
        repl = get_input(msg)
        answers.append(repl)
        corr_answ.append(a * b)
    for repl, tr in zip(answers, corr_answ):
        if repl == tr:
            print('OK!')
        else:
            print('NOT OK!')
            print(f'Your answer is {repl}, correct is {tr}')
            
            
            
prod_checker()