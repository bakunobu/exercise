"""
Давай подумаем над логикой.
Для случая а:
условие достигается, кода углы равны.
Наверное, самый удобный способ: создать
список таких состояний. Потом сравнивать.
Для случая б:
условие для достижения этого состояния - модуль разности должен быть равен 90 либо 270.
Также создаем список таких состояний и сравниваем последовательно первый и второй элемент, пока оба они не будут больше предложенных
"""

def h_to_min(h:int) -> int:
    return(h * 60)


def min_to_sec(m:int) -> int:
    return(m * 60)

def sec_to_deg(s: int) -> float:
    return(s * 0.1)

def main(h:int, m:int, s:int=0 ) -> float:
    m += h_to_min(h)
    s += min_to_sec(m)
    return(sec_to_deg(s) / 12)

# a
def generate_zero_state() -> list:
    positions = []
    for h in range(13):
        for m in range(60):
            h_pos = main(h, m)
            m_pos = m * 6
            if abs(h_pos - m_pos) < 3:
                positions.append((h, m))
    return(positions)


def find_time_diff(h:int, m:int) -> tuple:
    positions = generate_zero_state()
    i = 0
    while i <= h:
        if h == 12:
            if m == 0:
                next_pos = positions[0]
                break
            else:
                next_pos = positions[1]
                break
        if h == positions[i][0]:
            if m < positions[i][1]:
                next_pos = positions[i]
                break
            else:
                next_pos = positions[i+1]
                break
        i += 1
    if m > next_pos[1]:
        h_diff = next_pos[0] - h - 1
        mins_diff = next_pos[1] + 60 - m
    else:
        h_diff = next_pos[0] - h
        mins_diff = next_pos[1] - m
    return(h_diff, mins_diff)


# b
def generate_ninety_state() -> list:
    positions = []
    for h in range(13):
        for m in range(60):
            h_pos = main(h, m)
            m_pos = m * 6
            if abs(abs(h_pos - m_pos) - 90) < 3 or abs(abs(h_pos - m_pos) - 270) < 3: 
                positions.append((h, m))
    return(positions)


def find_time_diff_b(h:int, m:int) -> tuple:
    positions = generate_ninety_state()
    i = 0
    while i < len(positions):

        if h == positions[i][0]:
            if m < positions[i][1]:
                next_pos = positions[i]
                break
            else:
                next_pos = positions[i+1]
                break
            
        if h == 12:
            if m == 0:
                next_pos = positions[0]
                break
            else:
                next_pos = positions[1]
                break
        i += 1
        
    if m > next_pos[1]:
        h_diff = next_pos[0] - h - 1
        mins_diff = next_pos[1] + 60 - m
        
    else:
        h_diff = next_pos[0] - h
        mins_diff = next_pos[1] - m
    return(h_diff, mins_diff)


print(find_time_diff_b(2,15))