def srange_head_task(a: float, b:float, d:float) -> bool:
    limit = min(a, b)
    return((limit - d) > 1)