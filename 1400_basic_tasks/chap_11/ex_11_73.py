def short_students(heigth:list, r:float) -> int:
    short_studs = [1 for x in heigth if x <= r]
    return(len(short_studs))