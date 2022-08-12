class Rectangle:
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * (self.height + self.width)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if max(self.height, self.width) > 50:
            return "Too big for picture."
        line = "*" * self.width
        result = ""
        for x in range(self.height):
            result += line
            result += "\n"
        return result

    def get_amount_inside(self, rectangle):
        return int(self.height / rectangle.height) * int(self.width / rectangle.width)

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

class Square(Rectangle):
    def __init__(self, side):
        self.height = side
        self.width = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_height(self, height):
        self.set_side(height)

    def set_width(self, width):
        self.set_side(width)

    def __str__(self):
        return "Square(side={})".format(self.width)
