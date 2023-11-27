import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_abscisse(self):
        return self.x

    def get_ordonne(self):
        return self.y

    def set_abscisse(self, abscisse):
        self.x = abscisse

    def set_ordonne(self, ordonne):
        self.y = ordonne

    def distance(self, p):
        x1 = self.get_abscisse()
        y1 = self.get_ordonne()
        x2 = p.get_abscisse()
        y2 = p.get_ordonne()
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def norme(self):
        return math.sqrt(self.get_abscisse() ** 2 + self.get_ordonne() ** 2)

if __name__ == "__main__":
    point1 = Point(1, 2)
    point2 = Point(4, 6)

    print("Point 1 - Abscisse:", point1.get_abscisse(), ", Ordonnée:", point1.get_ordonne())
    print("Point 2 - Abscisse:", point2.get_abscisse(), ", Ordonnée:", point2.get_ordonne())

    distance = point1.distance(point2)
    print("Distance entre les points 1 et 2:", distance)

    norme_point1 = point1.norme()
    print("Norme du point 1:", norme_point1)

    norme_point2 = point2.norme()
    print("Norme du point 2:", norme_point2)

# print("hi")
# print