class Point:
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord


class Circle:
    def __init__(self, x_centre_coord, y_centre_coord, radius):
        self.x_centre_coord = x_centre_coord
        self.y_centre_coord = y_centre_coord
        self.radius = radius

    def check(self, point):
        if (point.x_coord - self.x_centre_coord) ** 2 + (point.y_coord - self.y_centre_coord) ** 2 <= self.radius ** 2:
            print('Point in circle')
        else:
            print('Point out circle')


p1 = Point(2, 3)
c1 = Circle(10, 20, 30)
c1.check(p1)

p2 = Point(100, 200)
c2 = Circle(5, 10, 5)
c2.check(p2)