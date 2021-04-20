def count_points(points:list) -> int:
    if sum(points[:6]) < sum(points[6:]):
        return(2)
    else:
        return(1)