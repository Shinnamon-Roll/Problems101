class Person:
    def __init__(self, Name: str, Age: int):
        self.Name = Name
        self.Age = Age

    def GetName(self) -> str:
        return self.Name

    def GetAge(self) -> int:
        return self.Age

    def SetName(self, Name: str) -> None:
        self.Name = Name

    def SetAge(self, Age: int) -> None:
        if Age >= 0:
            self.Age = Age
        else:
            raise ValueError("Age must be a non-negative integer.")

PersonInstance = Person("Alice", 30)
print(PersonInstance.GetName())
print(PersonInstance.GetAge())
PersonInstance.SetName("Bob")
PersonInstance.SetAge(35)
print(PersonInstance.GetName())
print(PersonInstance.GetAge())
