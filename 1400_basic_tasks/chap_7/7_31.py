def seq_sum() -> float:
    counter = 0
    my_sum = 0
    while True:
        x = int(input('Введите число: '))
        if x < 0:
            break
        counter += 1
        my_sum += x
    return(my_sum / counter)


print(seq_sum())