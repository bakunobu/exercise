""" Переделайте программу tenhellos. ру, объединив ее с программой hellos.ру так,
чтобы она получала в аргументе командной строки количество выво­димых строк. 
Можно считать, что аргумент меньше 1 ООО.
Подсказка: чтобы решить, когда применять 
st, nd, rd или th при выводе i-го сообщения Hello, используйте выражения i  % 1О и i % 100/ """

def n_hellos(n:int) -> None:
    """
    Use the correct grammatical form for a number and a noun
    
    Args:
    =====
    n: int
    number of iterations
    
    Return:
    =======
    None: None
    print output 
    """
    for x in range(1, n+1):
        if 10 < x <=20:
            print(f'{x}th hello')
        elif x % 10 == 1:
            print(f'{x}st hello')
        elif x % 10 == 2:
            print(f'{x}nd hello')
        elif x % 10 == 3:
            print(f'{x}rd hello')
        else:
            print(f'{x}th hello')