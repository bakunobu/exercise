""" Составьте программу checkerboardру, получающую один аргумент ко­мандной строки n
и использующую вложенный цикл для вывода двумер­ного узора n х n, наподобие
шахматной доски с чередующимися пробела­ми и звездочками.
 """

def checker_board(n):
    for x in range(n):
        if x % 2 == 0:
            print(* list('*' * n), sep=' ')
        else:
            print(' ', end='')
            print(* list('*' * (n - 1)), sep=' ')