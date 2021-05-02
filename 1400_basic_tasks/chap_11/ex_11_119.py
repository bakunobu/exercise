def aver_grade(grades:list) -> float:
    total = sum(aver_grade)
    total -= max(grades)
    total -= min(grades)
    return(total / (len(grades) - 2))