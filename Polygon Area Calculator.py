class Rectangle:

  def __init__(self,width,height):
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
    perimeter = (2*self.width) + (2*self.height)
    return perimeter 
  
  def get_diagonal(self):
    diagonal = ((self.width ** 2) + (self.height ** 2)) ** .5
    return diagonal

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      picture = ''
      for i in range(self.height):
        picture += "*" * self.width
        picture += '\n'
      return picture

  def get_amount_inside(self,shape):
    if self.width < shape.width or self.height < shape.height:
      return 0
    else:
      height_div = self.height // shape.height
      width_div  = self.width // shape.width 
      amount_inside = height_div * width_div
      return amount_inside

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)

  def __str__(self):
    return f"Square(side={self.height})"

  def set_side(self,side):
    self.height = side 
    self.width = side

  def set_width(self, side):
    self.set_side(side)

  def set_height(self, side):
    self.set_side(side)


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))