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
    pass