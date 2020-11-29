def degree_to_hours(d:float) -> tuple:
    tot_mins = d * 0.5
    hours = tot_mins // 60
    mins = int(tot_mins - hours * 60)
    return(hours, mins)
    