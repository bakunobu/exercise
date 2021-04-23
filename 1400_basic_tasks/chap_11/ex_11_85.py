def tall_students(students:list) -> int:
    tall_studs = [x for x in students if x > 170]
    return(len(tall_studs))


def basket_team(students:list) -> bool:
    num_studs = tall_students(list)
    return(num_studs >= 5)