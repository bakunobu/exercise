def exam_results() -> int:
    groups = []
    
    for i in range(3):
        group = []
        for j in range(20):
            msg = f'Укажите оценки {i} студента {j} группы'
            while True:
                try:
                    a, b, c = [int(x) for x in input(msg).split()]
                    group += [a, b, c]
                except ValueError:
                    print('используйте целые числа')
        
        groups.append(group)
    mean = [sum(group) / 60 for group in groups]
    max_mean = max(mean)
    return(mean.index(max_mean))