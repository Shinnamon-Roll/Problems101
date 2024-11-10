class Cashier:
    def __init__(self):
        self.Products = {}

    def AddProduct(self, Name: str, Price: float, Quantity: int):
        if Name in self.Products:
            self.Products[Name]['Quantity'] += Quantity
            self.Products[Name]['Price'] = Price
        else:
            self.Products[Name] = {'Price': Price, 'Quantity': Quantity}

    def RemoveProduct(self, Name: str):
        if Name in self.Products:
            del self.Products[Name]
        else:
            print(f"Product '{Name}' does not exist.")

    def CalculateTotal(self) -> float:
        total = sum(item['Price'] * item['Quantity'] for item in self.Products.values())
        return total

    def DisplayProducts(self):
        if not self.Products:
            print("No products available.")
            return
        print("Product List:")
        for Name, Details in self.Products.items():
            print(f"{Name} - Price: ${Details['Price']}, Quantity: {Details['Quantity']}")

def main():
    cashier = Cashier()
    
    while True:
        print("\nMenu:")
        print("1. Add a product")
        print("2. Remove a product")
        print("3. Calculate total cost")
        print("4. Display all products")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            Name = input("Enter product name: ").strip()
            while not Name:
                Name = input("Invalid name. Enter product name: ").strip()

            Price = input("Enter product price: ")
            while not Price.replace('.', '', 1).isdigit() or float(Price) <= 0:
                Price = input("Invalid price. Enter product price: ")
            Price = float(Price)

            Quantity = input("Enter product quantity: ")
            while not Quantity.isdigit() or int(Quantity) <= 0:
                Quantity = input("Invalid quantity. Enter product quantity: ")
            Quantity = int(Quantity)

            cashier.AddProduct(Name, Price, Quantity)

        elif choice == '2':
            Name = input("Enter product name to remove: ").strip()
            cashier.RemoveProduct(Name)

        elif choice == '3':
            TotalCost = cashier.CalculateTotal()
            print(f"Total Cost: ${TotalCost:.2f}")

        elif choice == '4':
            cashier.DisplayProducts()

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
