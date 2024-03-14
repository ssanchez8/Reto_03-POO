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

p1 = Point(-2, 5)
p2 = Point(3, 8)
line = Line(p1, p2)

print("La longitud de la línea es: ", line.compute_length())
print("La pendiente de la línea es: ", line.compute_slope())

line.compute_horizontal_cross()
line.compute_vertical_cross()

    


    
    
