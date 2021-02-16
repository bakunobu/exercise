from typing import Union


def get_input(message:str, is_float:bool=True) -> Union[int, float]:
    """
    Gets a number as an imput and returns it. If input is incorrect,
    i.e. float instead of int or a string that can't be converted to 
    number prints warning and asks for another input
    
    Works while the correct input is being typed in
    
    Args:
    =====
    message: str
    A message that is shown each time
    is_float: bool
    if is_float=True expects the input is float, otherwise int (True is a default value)
    
    Return:
    =======
    a: Union[int, float]
    The return is float if is_float (default value) otherwise int.
    
    """
    if is_float:
        while True:
            try:
                a = float(input(message))
                return(a)
            except ValueError:
                print('Используйте только числа (разделитель - \'.\')')
    else:
        while True:
            try:
                a = int(input(message))
                return(a)
            except ValueError:
                print('Используйте только целые числа')