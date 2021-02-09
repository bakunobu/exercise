def sum_squared() -> int:
    numbers = input().split()
    squares = [int(num) ** 2 for num in numbers]
    return(sum(squares))