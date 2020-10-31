""" Составьте программу fiveperline.ру,
использующую один цикл for и один оператор if для вывода, по пять в строку,
целые числа от 1 ООО (включи­тельно) до 2 ООО (исключительно).
Подсказка: используйте оператор %.  """

def print_thouthand() -> None:
    """
    prints all the numbers in [1000:2000) (five per line)
    """
    for x in range(1000, 2000):
        if x % 5 == 4:
            print(x, end='\n')
        else:
            print(x, end=' ')