def win_or_lose(results:list) -> str:
    if results.index(3) < results.index(0):
        return('Победа')
    elif results.index(3) > results.index(0):
        return('Поражение')
    else:
        return('Все игры были сыграны вничью')