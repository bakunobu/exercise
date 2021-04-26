def le_mean_grade(grade:mean) -> None:
    g = sum(grade) / len(grade)
    for i in range(len(grade)):
        if grade[i] < g:
            print(i + 1)