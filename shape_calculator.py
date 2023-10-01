class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self, width):
    self.width = width  

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    picture = ""
    for _ in range(self.height):
      picture += "*" * self.width + "\n"
    return picture

  def get_amount_inside(self, shape):
    if shape.width > self.width or shape.height > self.height:
      return 0

    return self.get_area() // shape.get_area()


class Square(Rectangle):

  def __init__(self, side):
    # self.side = side
    super().__init__(side, side)

  def __str__(self):
    return f"Square(side={self.width})"

  def set_side(self, side):
    self.set_width(side)

  def set_width(self, width):
    super().set_width(width)
    super().set_height(width)

  def set_height(self, height):
    super().set_width(height)
    super().set_height(height)
