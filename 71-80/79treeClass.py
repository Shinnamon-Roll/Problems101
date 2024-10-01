class Tree:
    def __init__(self, Species: str, Height: float, Age: int, Location: str):
        if not Species:
            raise ValueError("Species name cannot be empty.")
        if Height <= 0:
            raise ValueError("Height must be a positive number.")
        if Age <= 0:
            raise ValueError("Age must be a positive integer.")
        if not Location:
            raise ValueError("Location cannot be empty.")
        
        self.Species = Species
        self.Height = Height
        self.Age = Age
        self.Location = Location

    def Grow(self, GrowthAmount: float):
        if GrowthAmount <= 0:
            raise ValueError("Growth amount must be positive.")
        self.Height += GrowthAmount

    def ChangeLocation(self, NewLocation: str):
        if not NewLocation:
            raise ValueError("New location cannot be empty.")
        self.Location = NewLocation

    def DisplayInfo(self):
        print(f"Species: {self.Species}")
        print(f"Height: {self.Height} meters")
        print(f"Age: {self.Age} years")
        print(f"Location: {self.Location}")

def main():
    try:
        Species = input("Enter the species of the tree: ").strip()
        Height = float(input("Enter the height of the tree in meters: "))
        Age = int(input("Enter the age of the tree in years: "))
        Location = input("Enter the location of the tree: ").strip()

        tree = Tree(Species, Height, Age, Location)

        growth_amount = float(input("Enter how much the tree has grown (in meters): "))
        tree.Grow(growth_amount)

        new_location = input("Enter the new location of the tree: ").strip()
        tree.ChangeLocation(new_location)

        print("\nTree Information:")
        tree.DisplayInfo()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
