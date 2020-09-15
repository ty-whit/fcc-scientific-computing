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
        pass

    def get_perimeter(self):
        pass

    def get_diagonal(self):
        pass

    def get_picture(self):
        pass

    def get_amount_inside(self, rect):
        pass

class Square(Rectangle):
    def set_side(self, side):
        pass

