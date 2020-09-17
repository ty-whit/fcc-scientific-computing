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
    
    def draw(self):
        pass

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass