from main_funcs import get_input


def return_result() -> tuple:
    score = get_input('Укажите счет (одним числом): ', False)
    if score < 10:
        return(score, 0)
    else:
        g = score // 10
        l = score % 10
    return(g, l)