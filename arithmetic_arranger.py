def arithmetic_arranger(problems,showSolution=False):
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

    ############## Error Checking ##############
    try:
        checkNumberOfProbems(problems)
        checkCorrectOperators(operators)
        checkOperands(firstLineParts,secondLineParts)
        checkOperandLengths(firstLineParts,secondLineParts)
    except AssertionError as msg:
        #print(type(str(msg)))
        return str(msg)
    ############################################

    # Create empty strings for first line, second line, and bottom divider line
    firstLine = ''
    secondLine = ''
    thirdLine = ''
    # This list of buffers is used for proper formating if the solutions are shown. 
    bufferList = []

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
        bufferList.append(buffer)

        ################ Debugging ################
        #print(buffer)
        #print(type(buffer))
        ###########################################

        # Add all the pieces together. 
        firstLine += firstLineParts[i].rjust(buffer,' ') + spacer
        secondLine += operators[i] + secondLineParts[i].rjust(buffer-1,' ') + spacer
        thirdLine += '-'*buffer + spacer

    # Add all 3 lines together with a new line in between and we have a finished product. 
    arranged_problems = firstLine + '\n' + secondLine + '\n' + thirdLine

    # Code strictly to show the solution at the bottom of the display. 
    # This code will not run unlss the solution is asked for. 
    if showSolution:
        # Convert numbers to integers for addition
        firstLinePartsInt = [int(x) for x in firstLineParts]
        secondLinePartsInt = [int(x) for x in secondLineParts]
        # Check the operaation. If minus, second number is converted to negative. 
        for i in range(len(operators)):
            if operators[i] == '-': 
                secondLinePartsInt[i] *= -1

        # Add up each problem.
        solutionsParts = [firstLinePartsInt[i] + secondLinePartsInt[i] for i in range(len(firstLinePartsInt))]
        # Convert to formatted string.
        solutions = spacer.join([str(solutionsParts[i]).rjust(bufferList[i],' ') for i in range(len(solutionsParts))])
        # Add solutions to arranged problems. 
        arranged_problems += '\n' + solutions
    
    return arranged_problems

def checkNumberOfProbems(problems):
    assert len(problems) < 6, 'Error: Too many problems.'

def checkCorrectOperators(operators):
    for x in operators:
        assert x == '+' or x == '-', "Error: Operator must be '+' or '-'."

def checkOperands(firstLineParts,secondLineParts):
    for x in firstLineParts + secondLineParts:
        assert x.isdigit(), "Error: Numbers must only contain digits."

def checkOperandLengths(firstLineParts,secondLineParts):
    for x in firstLineParts + secondLineParts:
        assert len(x) < 5, "Error: Numbers cannot be more than four digits."