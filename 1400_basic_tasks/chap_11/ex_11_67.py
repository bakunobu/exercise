def build_pop(population:list) -> int:
    odd_nums = population[::2]
    even_nums = population[1::2]
    if odd_nums < even_nums:
        return(2)
    elif odd_nums > even_nums:
        return(1)
    else:
        return(100)