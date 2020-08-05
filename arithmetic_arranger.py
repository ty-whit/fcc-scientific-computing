def arithmetic_arranger(problems):
    spacer = ' '*4
    # Create empty lists to hold all problems
    firstLineParts = []
    secondLineParts = []
    operators = []

    # Separate each problem into their first line, second line, and operator coponants. 
    for prob in problems:
        firstLineParts.append(prob.split()[0])
        secondLineParts.append(prob.split()[2])
        operators.append(prob.split()[1])
    
    ################ Debugging ################
    #print(firstLineParts)
    #print(secondLineParts)
    #print(operators)
    ###########################################

    # Create empty strings for first line, second line, and bottom divider line
    firstLine = ''
    secondLine = ''
    thirdLine = ''

    # Place each peice into the first and second lines, with appropriate spacing. 
    for i in range(len(problems)):
        # This buffer variable tells how much space is needed to right justify numbers. The value 2 is used to insure proper formating. 
        buffer = 2

        # If the first number is longer, than use it. 
        if len(firstLineParts[i]) > len(secondLineParts[i]):
            buffer += len(firstLineParts[i]) 
        # if the second, use it instead.
        else:  
            buffer += len(secondLineParts[i])
            
        ################ Debugging ################
        # print(buffer)
        ###########################################

        # Add all the pieces together. 
        firstLine += firstLineParts[i].rjust(buffer,' ') + spacer
        secondLine += operators[i] + secondLineParts[i].rjust(buffer-1,' ') + spacer
        thirdLine += '-'*buffer + spacer

    # Add all 3 lines together with a new line in between and we have a finished product. 
    arranged_problems = firstLine + '\n' + secondLine + '\n' + thirdLine
    
    return arranged_problems