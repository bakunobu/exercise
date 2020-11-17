def find_time(v_1: float, v_2:float, S:float) -> float:
    v_tot = v_1 + v_2
    return(S / v_tot)


print(find_time(50.0, 50.0, 100.0))