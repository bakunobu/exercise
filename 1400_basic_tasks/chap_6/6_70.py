def cut_square(a:int, b:int) -> tuple:
    return(max(a, b) - min(a, b), min(a, b))


def cutter(a:int, b:int) -> None:
    cut_dict = dict()
    while a > 1 or b > 1:
        k = f'{min(a, b)}x{min(a, b)}'
        if k not in cut_dict.keys():
            cut_dict[k] = 1
        else:
            cut_dict[k] += 1
        a, b = cut_square(a, b)
    for k, i in cut_dict.items():
        print(f'{k}: {i}')
        