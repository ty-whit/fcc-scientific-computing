class Rectangle:
    def __init__(self, width, height):
        # set the width of the rectangle
        self.set_width(width)
        # set the height of the rectangle
        self.set_height(height)
        return
    
    def __str__(self):
        # return string to print
        return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'
    
    def set_width(self, width):
        # Set width of the rectangle
        self.width = width
        return

    def set_height(self, height):
        # Set height of rectangle
        self.height = height
        return

    def get_area(self):
        # Area = width * height
        return self.width * self.height

    def get_perimeter(self):
        # Perimeter = 2*width + 2*height
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        # Use Pythagorean Theorem to compute diagonal
        return (self.width**2 + self.height**2)**(1/2)

    def get_picture(self):
        # Check to see if the rectangle size is too large
        if self.height > 50 or self.width > 50: 
            return 'Too big for picture.'
        # Build the first line of the rectangle
        printString  = '*'*self.width + '\n'
        # Duplicate the line for the height
        printString *= self.height
        # Return this string
        return printString

    def get_amount_inside(self, rect):
        # How many whole rectangles (of the kind passed in) fit inside of 
        # the rectangle given  
        return self.get_area() // rect.get_area()

class Square(Rectangle):
    def __init__(self, side):
        # Set the side of the square
        self.set_side(side)
        return 

    def __str__(self):
        # String to be printed for Square class. 
        return 'Square(side=' + str(self.width) + ')'

    def set_side(self, side):
        # Since both height and width are the same, we set both using side.
        self.set_width(side)
        self.set_height(side)
        return

