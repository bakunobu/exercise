def chem_grades(grades:list) -> int:
    neg_grades = [0 for x in grades if x == 2]
    return(len(neg_grades))