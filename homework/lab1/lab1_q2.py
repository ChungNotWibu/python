class rectangle:
    def __init__(self,Height,Width):
        self.Height = Height
        self.Width = Width

    def perimeter(self):
        return 2 * (self.Height + self.Width)

    def acreage(self):
        return self.Height * self.Width


class circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def acreage(self):
        return 3.14 * self.radius**2

def main():
    Shape = input("Enter the name of the shape to calculate (rectangle/circle): ").lower()

    if Shape == "rectangle" :
        Height = float(input("Enter height: "))
        Width = float(input("Enter width: "))
        Rectangle = rectangle(Height, Width)

        print("The perimeter of the rectangle is:", Rectangle.perimeter())
        print("The acreage of the rectangle is:", Rectangle.acreage())
    
    elif Shape == "circle":
        radius = float(input("Enter radius: "))
        Circle = circle(radius)

        print("The circumference of the circle is:", Circle.perimeter())
        print("The area of the circle is:", Circle.acreage())
    
    else:
        print("Shape is not supported.")

if __name__ == "__main__":
    main()