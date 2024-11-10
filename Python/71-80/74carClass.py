class Car:
    def __init__(self, Brand: str, Model: str, Year: int, Color: str):
        self.Brand = Brand
        self.Model = Model
        self.Year = Year
        self.Color = Color

    def displayDetails(self) -> None:
        print(f"Brand: {self.Brand}")
        print(f"Model: {self.Model}")
        print(f"Year: {self.Year}")
        print(f"Color: {self.Color}")

def CarMenu():
    Cars = {}
    while True:
        print("\nMenu:")
        print("1. Create a new car")
        print("2. Display car details")
        print("3. Exit")
        Choice = input("Please select an option: ")

        if Choice == '1':
            Brand = input("Enter the car brand: ")
            Model = input("Enter the car model: ")
            Year = int(input("Enter the car year: "))
            Color = input("Enter the car color: ")
            CarName = f"{Brand} {Model}"
            Cars[CarName] = Car(Brand, Model, Year, Color)
            print("Car created successfully.")
        
        elif Choice == '2':
            CarName = input("Enter the car name (Brand Model) to display: ")
            if CarName in Cars:
                Cars[CarName].displayDetails()
            else:
                print("Car not found.")
        
        elif Choice == '3':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

CarMenu()
