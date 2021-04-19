def total_par_resist(resist_list:resist) -> float:
    par_resist = [x ** -1 for x in resist_list]
    return(sum(par_resist))