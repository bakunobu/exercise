week_days = {1: 'Monday',
             2: 'Tuesday',
             3: 'Wednesday',
             4: 'Thursday',
             5: 'Friday',
             6: 'Saturday',
             7: 'Sunday'}


def day_week(x:int) -> str:
    return(week_days.get(x))