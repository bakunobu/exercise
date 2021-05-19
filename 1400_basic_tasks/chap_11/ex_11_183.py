def popul_man_sort(popul:list) -> list:
    last = popul.pop()
    i = len(popul) - 1
    while i > 0:
        if last < popul[i]:
            i -= 1
        else:
            popul.insert(i, last)
            return(popul)
    popul.insert(0, last)
    return(popul)