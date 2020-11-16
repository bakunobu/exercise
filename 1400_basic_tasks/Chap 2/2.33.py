def find_dif_age(age_1:int, age_2:int) -> None:
    mean_age = (age_1 + age_2) / 2
    diff_1 = abs(mean_age - age_1)
    diff_2 = abs(mean_age - age_2)
    print(f'Средний возраст детей: {mean_age}')
    print(f'Возраст первого ребенка отличается от срднего на {diff_1} лет')
    print(f'Возраст второго ребенка отличается от срднего на {diff_2} лет')
    
    
find_dif_age(2, 15)