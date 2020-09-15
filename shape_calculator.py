class Rectangle:
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)
        return
    
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
        pass

    def get_amount_inside(self, rect):
        pass

class Square(Rectangle):
    def set_side(self, side):
        pass

