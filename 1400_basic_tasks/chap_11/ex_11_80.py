def results(grades:list) -> tuple:
    return(grades.count(5),
           grades.count(4),
           grades.count(3),
           grades.count(2)) 
 