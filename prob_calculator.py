import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        # Save the number of each type of ball to a dictionary element of the class
        self.ballSet = kwargs
        # Start an empty list of the balls contained in the hat. 
        self.contents = [ ]

        # Loop over each type/color of ball
        for (key,val) in self.ballSet.items():
            # Loop over the number of this type of ball
            for i in range(val):
                # And add it to the contents of the hat
                self.contents.append(key)
        return
    
    def draw(self,numBalls):
        # Make a copy of the hat that we can pull balls from
        contents_copy = copy.copy(self.contents)
        # Create a pile of the balls that we have removed
        ballsRemoved = []
        
        # Loop over number of balls to be removed
        for i in range(numBalls):
            # Remove a random ball, and add it to the pile
            ballsRemoved.append(contents_copy.pop(random.randint(0,len(contents_copy)-1)))
            # If there are no more balls in the hat
            if len(contents_copy) == 0:
                # break the loop
                 break
        
        # Return the balls removed to the caller
        return ballsRemoved
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # count of the number of experiments that have been successful
    successfulExperimentsCount = 0

    # Run through all the experiments
    for i in range(num_experiments):
        # Initially assume that the experiment is successful
        successfulExperiment = True
        # run through the experiment
        ballsRemoved = hat.draw(num_balls_drawn)
        
        # Set up a dictionary to count up the number of balls in the experiment
        ballsCount = {}
        # Loop through each color
        for color in expected_balls.keys():
            # Count up the balls actually removed from the hat
            ballsCount[color] = ballsRemoved.count(color)

            # Check to see if we removed enough balls 
            if ballsCount[color] < expected_balls[color]:
                # If not, we failed the experiment
                successfulExperiment = False
                # we don't need to run through any other color if we have failed.
                continue

        # If this experiment was successful
        if successfulExperiment: 
            # then add it to the total count.
            successfulExperimentsCount += 1
        
    # calculate the probability of the result. 
    probability = successfulExperimentsCount/num_experiments
    return probability