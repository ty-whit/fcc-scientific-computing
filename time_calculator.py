def add_time(start, duration):
    start = separate_time_string(start)
    duration = separate_time_string(duration)
    
    #duration = numbers_of_days(duration)

    finalTime = [ start[0] + duration[0], start[1] + duration[1] ]
    #print(finalTime)

    finalTime = correct_time_format24HR(finalTime) 

    finalTime = format_to_12hr(finalTime)

    new_time = "{hour}:{minute} {am_pm} {days}".format(hour=finalTime[0],minute=finalTime[1],am_pm=finalTime[2],days=finalTime[3])


    #return "Not Finished"
    return new_time    

def separate_time_string(time):
    hour = int(time.split(sep=":")[0])
    try: 
        minute = int(time.split(sep=":")[1])
    except ValueError:  
        secondHalf = time.split(sep=":")[1].split()
        minute = int(secondHalf[0])
        if secondHalf[1] == "PM":
            #minute = int(secondHalf[0])
            hour += 12
        #elif secondHalf[1] = "AM"

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
    else:
        finalTime.append(0)

    return finalTime

def format_to_12hr(finalTime):
    minute = str(finalTime[1]).rjust(2,"0")

    am_pm = ''
    if finalTime[0] in range(0,12):
        am_pm = "AM"
        if finalTime[0] == 0:
            finalTime[0] = "12"
    elif finalTime[0] in range(12,24):
        finalTime[0] -= 12
        am_pm = "PM"
    else:
        print("Error: Invalid hour found.")
        return None

    hour = str(finalTime[0]).rjust(2,"0")

    if finalTime[2] == 0:
        daysAfter = ""
    elif finalTime[2] == 1:
        daysAfter = "(next day)"
    else:
        daysAfter = "({n} days later)".format(n=finalTime[2])


    return [hour,minute,am_pm,daysAfter]
