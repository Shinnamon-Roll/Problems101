class Book:
    def __init__(self, Name: str, Status: str):
        self.Name = Name
        self.Status = Status

    def __str__(self) -> str:
        return f"Book Name: {self.Name}, Status: {self.Status}"

def BookMenu():
    Books = {}
    while True:
        print("\nMenu:")
        print("1. Create a new book")
        print("2. Display book information")
        print("3. Update book status")
        print("4. Exit")
        Choice = input("Please select an option: ")

        if Choice == '1':
            Name = input("Enter the book name: ")
            Status = input("Enter the book status (available/checked out): ")
            Books[Name] = Book(Name, Status)
            print("Book created successfully.")
        
        elif Choice == '2':
            Name = input("Enter the book name to display: ")
            if Name in Books:
                print(Books[Name])
            else:
                print("Book not found.")
        
        elif Choice == '3':
            Name = input("Enter the book name to update status: ")
            if Name in Books:
                NewStatus = input("Enter the new status (available/checked out): ")
                Books[Name].Status = NewStatus
                print("Status updated successfully.")
            else:
                print("Book not found.")
        
        elif Choice == '4':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

BookMenu()
