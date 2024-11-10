class Pet:
    def __init__(self, Species: str, Breed: str, Color: str, Name: str, Height: float, Weight: float):
        self.Species = Species
        self.Breed = Breed
        self.Color = Color
        self.Name = Name
        self.Height = Height
        self.Weight = Weight

    def displayInfo(self):
        print("Pet Information:")
        print(f"Species: {self.Species}")
        print(f"Breed: {self.Breed}")
        print(f"Color: {self.Color}")
        print(f"Name: {self.Name}")
        print(f"Height: {self.Height} cm")
        print(f"Weight: {self.Weight} kg")

def getValidInput(prompt: str, validationFunc) -> str:
    while True:
        value = input(prompt)
        if validationFunc(value):
            return value
        print("Invalid input. Please try again.")

def isNonEmptyString(value: str) -> bool:
    return bool(value.strip())

def isPositiveFloat(value: str) -> bool:
    try:
        return float(value) > 0
    except ValueError:
        return False

def PetMenu():
    petTypes = ["Dog", "Cat", "Bird"]
    print("Select a pet type to store information:")
    for index, petType in enumerate(petTypes, 1):
        print(f"{index}. {petType}")

    choice = getValidInput("Enter your choice (1-3): ", lambda x: x.isdigit() and 1 <= int(x) <= 3)
    species = petTypes[int(choice) - 1]

    breed = getValidInput("Enter the breed: ", isNonEmptyString)
    color = getValidInput("Enter the color: ", isNonEmptyString)
    name = getValidInput("Enter the name: ", isNonEmptyString)
    
    height = getValidInput("Enter the height (in cm): ", isPositiveFloat)
    weight = getValidInput("Enter the weight (in kg): ", isPositiveFloat)
    
    pet = Pet(species, breed, color, name, float(height), float(weight))
    pet.displayInfo()

PetMenu()
