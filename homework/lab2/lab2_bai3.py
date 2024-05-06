class Square:
    def __init__(self, side_length):
        self.side_length = side_length
    def cal_area(self):
        return self.side_length ** 2

class Cube(Square):
    def cal_area(self):
        return 6 * super().cal_area()
    def cal_volume(self):
        return self.side_length ** 3

square = Square(2)
print('Square area:', square.cal_area())

cube = Cube(2)
print('Cube area:', cube.cal_area())
print('Cube volume:', cube.cal_volume())