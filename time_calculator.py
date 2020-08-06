def add_time(start, duration):
    start = [separate_hour(start),separate_minute(start)]
    duration = [[separate_hour(duration),separate_minute(duration)]]

    new_time = 0
    return new_time    

def separate_hour(time):
    return time.split(sep=":")[0]

def separate_minute(time):
    return time.split(sep=":")[1]





