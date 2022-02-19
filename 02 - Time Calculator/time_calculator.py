def add_time(start, duration,weekday = None):
    # Separate the start time string into parts for use later
    start = separate_time_string(start)

    # Separate the duration time into parts for use later
    duration = separate_time_string(duration)
    
    # Add the duration to the start time
    finalTime = [ start[0] + duration[0], start[1] + duration[1] ]

    # Correct some artifacts about the final time to bring it back to a 24-hour clock
    finalTime = correct_time_format24HR(finalTime) 
    # Save the number of days passed for easier use later
    numDays = finalTime[2]

    # Format 24-hour clock to 12-hour clock.
    finalTime = format_to_12hr(finalTime)

    # Format final time for  display
    new_time = "{hour}:{minute} {am_pm}{days}".format(hour=finalTime[0],minute=finalTime[1],am_pm=finalTime[2],days=finalTime[3])

    # Check to see if the weekday was provided in the function call
    if weekday is not None:
        # List of possible weekdays
        weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        # Correct capitalization errors
        weekday = weekday.title()

        # Is the provided weekday in the a valid weekday?
        if weekday in weekdays:
            # Find the new weekday after number of days have passed.
            index = (weekdays.index(weekday) + numDays) % 7 
            
            # End day as a string
            newDay = weekdays[index]

            # Format final time for display
            new_time = "{hour}:{minute} {am_pm}, {day}{days}".format(hour=finalTime[0],minute=finalTime[1],am_pm=finalTime[2],day=newDay,days=finalTime[3])

    return new_time    

def separate_time_string(time):
    # Convert hours into integer
    hour = int(time.split(sep=":")[0])

    # Try to convert minutes into minutes
    try: 
        minute = int(time.split(sep=":")[1])
    
    # If ValueError occurs, There is an AM or PM in the string
    except ValueError:  
        # Separate minutes from AM or PM
        secondHalf = time.split(sep=":")[1].split()
        # Convert minutes to integer
        minute = int(secondHalf[0])

        # Check to see if time given is in PM
        if secondHalf[1] == "PM":
            #If so, add 12 hours to convert to 24 hour clock
            hour += 12

    return [hour, minute]
    

 
def correct_time_format24HR(finalTime):
    # If final time has minutes greater than 60,
    if finalTime[1] >= 60:
        # Add overflow to hours
        finalTime[0] += finalTime[1]//60
        # Bring minutes to below 60
        finalTime[1] %= 60
    
    # if final time has hours greater than 24,
    if finalTime[0] >= 24:
        # save how many days later
        numDays = finalTime[0]//24
        # Bring hours to below 24.
        finalTime[0] = finalTime[0]%24
        # Save number of days in final time 
        finalTime.append(numDays)
    else:
        # if same day, append 0 in location for number of days. 
        finalTime.append(0)

    return finalTime

def format_to_12hr(finalTime):
    # Save minute as string with correct format
    minute = str(finalTime[1]).rjust(2,"0")

    # Check for AM and PM
    if finalTime[0] in range(0,12):
        am_pm = "AM"
        # Check to see if it is midnight
        if finalTime[0] == 0:
            finalTime[0] = "12"
    elif finalTime[0] in range(12,24):
        if finalTime[0] > 12:
            finalTime[0] -= 12
        am_pm = "PM"
    else:
        print("Error: Invalid hour found.")
        return None

    # Save hour as a string
    hour = str(finalTime[0])

    # check to see if final time is on a different day.
    if finalTime[2] == 0:
        daysAfter = ""
    elif finalTime[2] == 1:
        daysAfter = " (next day)"
    else:
        daysAfter = " ({n} days later)".format(n=finalTime[2])


    return [hour,minute,am_pm,daysAfter]
