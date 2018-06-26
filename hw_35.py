class Point:
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord


class Circle:
    def __init__(self, x_centre_coord, y_centre_coord, radius):
        self.x_centre_coord = x_centre_coord
        self.y_centre_coord = y_centre_coord
        self.radius = radius

    def is_point_in_circle(self, point):
        if (point.x_coord - self.x_centre_coord) ** 2 + (point.y_coord - self.y_centre_coord) ** 2 <= self.radius ** 2:
            return True
        else:
            return False


p1 = Point(2, 3)
c1 = Circle(10, 20, 30)
print(c1.is_point_in_circle(p1))

p2 = Point(100, 200)
c2 = Circle(5, 10, 5)
print(c2.is_point_in_circle(p2))