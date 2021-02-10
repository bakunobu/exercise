def load(n:int, load_cap:float) -> bool:
    cap = 0
    for i in range(n):
        while True:
            try:
                l = float(input('Укажит массу предмета: '))
                cap += l
                break
            except ValueError:
                print('Используйте только числа (разделитель - \'.\')')
    return(cap <= load_cap)