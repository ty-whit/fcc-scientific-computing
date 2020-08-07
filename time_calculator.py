def add_time(start, duration):
    start = separate_time_string(start)
    duration = separate_time_string(duration)
    
    #duration = numbers_of_days(duration)

    finalTime = [ start[0] + duration[0], start[1] + duration[1] ]
    print(finalTime)

    finalTime = correct_time_format(finalTime) 

    new_time = "{hour}:{minute}".format(hour=finalTime[0],minute=finalTime[1])

    #return "Not Finished"
    return new_time    

def separate_time_string(time):
    hour = int(time.split(sep=":")[0])
    try: 
        minute = int(time.split(sep=":")[1])
    except ValueError:  
        secondHalf = time.split(sep=":")[1].split()
        minute = secondHalf[0]
        if secondHalf[1] == "PM":
            minute = int(secondHalf[0])
            hour += 12
    return [hour, minute]
    

#def numbers_of_days(duration):
    
def correct_time_format24HR(finalTime):
    if finalTime[1] >= 60:
        finalTime[0] += finalTime[1]//60
        finalTime[1] %= 60
    
    if finalTime[0] >= 24:
        numDays = finalTime[0]//24
        finalTime[0] = finalTime[0]%24
        finalTime.append(numDays)

    return finalTime
