def choose_team(results:list) -> tuple:
    first_runner = None
    first_time = None
    second_runner = None
    second_time = None
    third_runner = None
    third_time = None
    forth_runner = None
    forth_time = None
    
    for i in range(len(results)):
        if first_runner is None:
            first_runner = i
            first_time = results[i]
            
        elif second_runner is None:
            if results[0] < results[i]:
                second_runner = i
                second_time = results[i]
            else:
                first_runner, second_runner = i, first_runner
                first_time, second_time = results[i], first_time
                
        elif third_runner is None:
            if results[i] < first_runner:
                third_runner = second_runner
                third_time = second_time
                second_runner = first_runner
                second_time = first_time
                first_runner = results[i]
                first_time = i
            elif results[i] < second_runner:
                third_runner = second_runner
                third_time = second_time
                second_runner = results[i]
                second_time = i
            else:
                third_runner = results[i]
                third_time = i
                
        elif forth_runner is None:
            if results[i] < first_runner:
                forth_runner = third_runner
                forth_time = third_time
                third_runner = second_runner
                third_time = second_time
                second_runner = first_runner
                second_time = first_time
                first_runner = results[i]
                first_time = i
            elif results[i] < second_runner:
                forth_runner = third_runner
                forth_time = third_time
                third_runner = second_runner
                third_time = second_time
                second_runner = results[i]
                second_time = i
            elif results[i] < third_runner:
                forth_runner = third_runner
                forth_time = third_time
                third_runner = results[i]
                third_time = i
            else:
                forth_runner = results[i]
                forth_time = i
        else:
            if results[i] < first_runner:
                forth_runner = third_runner
                forth_time = third_time
                third_runner = second_runner
                third_time = second_time
                second_runner = first_runner
                second_time = first_time
                first_runner = results[i]
                first_time = i
            elif results[i] < second_runner:
                forth_runner = third_runner
                forth_time = third_time
                third_runner = second_runner
                third_time = second_time
                second_runner = results[i]
                second_time = i
            elif results[i] < third_runner:
                forth_runner = third_runner
                forth_time = third_time
                third_runner = results[i]
                third_time = i
            elif results[i] < forth_runner:
                forth_runner = results[i]
                forth_time = i
            else:
                pass
    return(first_time,
           second_time,
           third_time,
           forth_time)
        