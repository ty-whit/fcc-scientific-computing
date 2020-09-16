class Rectangle:
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)
        return
    
    def __str__(self):
        return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'
    
    def set_width(self, width):
        self.width = width
        return

    def set_height(self, height):
        self.height = height
        return

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 *(self.width + self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**(1/2)

    def get_picture(self):
        if self.height > 50 or self.width > 50: 
            return 'Too big for picture.'
        printString  = '*'*self.width + '\n'
        printString *= self.height
        return printString

    def get_amount_inside(self, rect):
        return self.get_area() // rect.get_area()

class Square(Rectangle):
    def __init__(self, side):
        self.set_side(side)
        return 

    def __str__(self):
        return 'Square(side=' + str(self.width) + ')'


    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)
        return

