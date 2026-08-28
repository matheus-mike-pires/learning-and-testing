from typing import Self
class Shape:
  is3d = False
  is2d = True

  def __init__(self, color=None):
    self.color = input('what is the color?: ')
    


class Square(Shape):
  def __init__(self, color=None, side=None):
    super().__init__(color=None)
    self.side = float(input('what is the side?: '))
  def area(self):
    return (self.side * self.side)

class Triangle(Shape):
  def __init__(self, color=None, base=None, height=None):
    super().__init__(color=None)
    self.base = float(input('what is the base?: '))
    self.height = float(input('what is the height?: '))

  def area(self):
    return (self.base * self.height) * 0.5


class Circle(Shape):
  def __init__(self, color=None, radius=None):
    super().__init__(color=None)
    self.radius = float(input('what is the radius?: '))

  def area(self):
    return (self.radius ** 2) * 3.14 


  
  
def main():
  is_running = True
  while is_running:
    choice1 = input('to verify circles, press 1. To verify tringles, press 2. To verify squares, press 3: ')
    valid_choices1 = ['1', '2', '3'] 
    while choice1 not in valid_choices1:
      print()
      choice1 = input('please, select a valid option: ')
    if choice1 == '1':
      print()
      circle1 = Circle()
      print(f'the area of the {circle1.color} circle is {circle1.area()} cm^2')
    elif choice1 == '2':
      print()
      triangle1 = Triangle()
      print(f'the area of the {triangle1.color} triangle is {triangle1.area()} cm^2')
    elif choice1 == '3':
      print()
      square1 = Square()
      print(f'the area of the {square1.color} square is {square1.area()} cm^2')
    
    
    print()
    choice2 = input('Press 1 to try again. Press 2 to quit: ')
    valid_choices2 = ['1', '2'] 
    while choice1 not in valid_choices1:
      print()
      choice2 = input('please, select a valid option: ')
    if choice2 == '1':
      continue
    if choice2 == '2':
      is_running = False
      break



print('Use OOP to verify the color and area of circles, triangles and squares')
print()

if __name__ == '__main__':
  main()

print('thank you for exploring this program!')
