class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Line:
    def __init__(self, point1:Point, point2:Point):
        self.length = None
        self.slope = None
        self.start = point1
        self.end = point2
    
    def compute_length(self):
        if self.length is None:
            self.length = ((self.end.x - self.start.x)**2 + (self.end.y - self.start.y)**2)**0.5
        return self.length
    
    def compute_slope(self):
        if self.slope is None:
            dy = self.end.y - self.start.y
            dx = self.end.x - self.start.x
            self.slope = (dy/dx)
            if dx == 0:
                self.slope = "infinite"                            
        return self.slope
    
    def compute_horizontal_cross(self):
        if self.start.y * self.end.y < 0:
            print("La línea cruza al eje x")
        else:
            print("La línea no cruza al eje x")
    
    def compute_vertical_cross(self):
        if self.start.x * self.end.x < 0:
            print("La línea cruza al eje y")
        else:
            print("La línea no cruza al eje y")

class Rectangle:
    def __init__(self, method, *args):
       
        if method == 1:
            self.method_1(*args)
        elif method == 2:
            self.method2(*args)
        elif method == 3:
            self.method3(*args)
        elif method == 4:
            self.method4(*args)

    def method_1(self, bottom_left, width, height):
        self.bottom_left = bottom_left
        self.width = width
        self.height = height
        self.center = Point(bottom_left.x + width / 2, bottom_left.y + height / 2)

    def method2(self, center, width, height):
        self.center = center
        self.width = width
        self.height = height
        self.bottom_left = Point(center.x - width / 2, center.y - height / 2)

    def method3(self, bottom_left, upper_right):
        self.bottom_left = bottom_left
        self.upper_right = upper_right
        self.width = upper_right.x - bottom_left.x
        self.height = upper_right.y - bottom_left.y
        self.center = Point(bottom_left.x + self.width / 2, bottom_left.y + self.height / 2)
        
    def method4 (self, line1, line2, line3, line4):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.line4 = line4
        self.width = line1.compute_length()
        self.height = line2.compute_length()
        self.center = Point(self.line1.start.x + self.width / 2, self.line1.start.y + self.height / 2)

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2 * (self.width + self.height)

# 1st Method
method = 1 
bottom_left = Point(0, 0)  
width = 5
height = 3
rectangle1 = Rectangle(method, bottom_left, width, height)  

print("MÉTODO 1")
print("El área del rectángulo es: ", rectangle1.compute_area())
print("El perímetro del rectángulo es: ", rectangle1.compute_perimeter(), "\n")

# 2nd Method
method = 2
center = Point(2, 2)
width = 5
height = 3
rectangle2 = Rectangle(method, center, width, height)
print("MÉTODO 2")
print("El área del rectángulo es: ", rectangle2.compute_area())
print("El perímetro del rectángulo es: ", rectangle2.compute_perimeter(), "\n")

#3rd Method

print("MÉTODO 3")
method = 3
bottom_left = Point(0, 0)
upper_right = Point(5, 3)
rectangle3 = Rectangle(method, bottom_left, upper_right)

print("El área del rectángulo es: ", rectangle3.compute_area())
print("El perímetro del rectángulo es: ", rectangle3.compute_perimeter())

#4th Method

print("MÉTODO 4")
p1 = Point(0, 0)
p2 = Point(5, 0)
p3 = Point(5, 3)
p4 = Point(0, 3)
line1 = Line(p1, p2)
line2 = Line(p2, p3)
line3 = Line(p3, p4)
line4 = Line(p4, p1)
rectangle4 = Rectangle(4, line1, line2, line3, line4)

print("El área del rectángulo es: ", rectangle4.compute_area())
print("El perímetro del rectángulo es: ", rectangle4.compute_perimeter())