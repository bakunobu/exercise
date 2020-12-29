def choose_cat(w:float) -> str:
    if w < 60:
        return('легкий')
    elif 60 <= w < 64:
        return('первый полусредний')
    else:
        return('полусредний')