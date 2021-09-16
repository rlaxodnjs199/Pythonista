from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):
    def noofsides(self):
        print("3")


class Pentagon(Polygon):
    def noofsides(self):
        print("5")


class Hexagon(Polygon):
    def noofsides(self):
        print("6")


class Arbitrary:
    def noofsides(self):
        print("hehehehe")


if __name__ == "__main__":
    polygons = [Triangle(), Pentagon(), Hexagon(), Arbitrary()]
    for polygon in polygons:
        polygon.noofsides()
