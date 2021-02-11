from typing import Union


def get_input(message:str, is_float:bool=True) -> Union[int, float]:
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



def area_and_crop(num_dist:int=10) -> list:
    tot_crop = 0
    tot_yild = 0
    for dist in range(num_dist):
        dist_area = get_input('Укажите посевную площадь в {}-м районе: '.format(dist+1))
        dist_crop = get_input('Укажите урожайность в {}-м районе'.format(dist+1))
        tot_crop += dist_crop
        dist_yild = dist_crop / dist_area
        tot_yild += dist_yild
    return([tot_crop, tot_yild / num_dist])

