import math

class Circle:
    def __init__(self, Radius: float):
        self.Radius = Radius

    def Area(self) -> float:
        return math.pi * (self.Radius ** 2)

    def Circumference(self) -> float:
        return 2 * math.pi * self.Radius

def main():
    Radius = float(input("Enter the radius of the circle: "))
    CircleInstance = Circle(Radius)
    print(f"Area of the circle: {CircleInstance.Area()}")
    print(f"Circumference of the circle: {CircleInstance.Circumference()}")

if __name__ == "__main__":
    main()
