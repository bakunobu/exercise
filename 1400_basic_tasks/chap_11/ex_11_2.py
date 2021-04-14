def input_to_list(msg:str) -> list:
    my_list = [input(msg) for i in range(10)]
    return(my_list)


msg = 'Укажите элемент массива: '
my_list = input_to_list(msg)
print('Массив содержит следующие элементы:')
print(* my_list, sep=';\n')