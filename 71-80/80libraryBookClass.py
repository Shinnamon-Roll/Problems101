class LibraryBook:
    def __init__(self, Title: str, Author: str, YearPublished: int, ISBN: str):
        if not Title:
            raise ValueError("Title cannot be empty.")
        if not Author:
            raise ValueError("Author cannot be empty.")
        if YearPublished <= 0 or YearPublished > 2024:
            raise ValueError("Year published must be a positive integer not in the future.")
        if not ISBN.isdigit() or len(ISBN) not in [10, 13]:
            raise ValueError("ISBN must be 10 or 13 digits long and numeric.")
        
        self.Title = Title
        self.Author = Author
        self.YearPublished = YearPublished
        self.ISBN = ISBN
        self.Status = "available"

    def check_out(self):
        if self.Status == "available":
            self.Status = "checked out"
        else:
            print("The book is already checked out.")

    def return_book(self):
        if self.Status == "checked out":
            self.Status = "available"
        else:
            print("The book is already available.")

    def display_info(self):
        print(f"Title: {self.Title}")
        print(f"Author: {self.Author}")
        print(f"Year Published: {self.YearPublished}")
        print(f"ISBN: {self.ISBN}")
        print(f"Status: {self.Status}")

class Library:
    def __init__(self):
        self.Books = {}

    def add_book(self):
        try:
            Title = input("Enter the title of the book: ").strip()
            Author = input("Enter the author of the book: ").strip()
            YearPublished = int(input("Enter the year published: "))
            ISBN = input("Enter the ISBN: ").strip()

            book = LibraryBook(Title, Author, YearPublished, ISBN)
            self.Books[ISBN] = book
            print("Book added successfully.")

        except ValueError as e:
            print(f"Error: {e}")

    def check_out_book(self):
        ISBN = input("Enter the ISBN of the book to check out: ").strip()
        if ISBN in self.Books:
            self.Books[ISBN].check_out()
        else:
            print("Book not found.")

    def return_book(self):
        ISBN = input("Enter the ISBN of the book to return: ").strip()
        if ISBN in self.Books:
            self.Books[ISBN].return_book()
        else:
            print("Book not found.")

    def display_book_info(self):
        ISBN = input("Enter the ISBN of the book: ").strip()
        if ISBN in self.Books:
            self.Books[ISBN].display_info()
        else:
            print("Book not found.")

    def display_all_books(self):
        if not self.Books:
            print("No books in the library.")
            return
        for book in self.Books.values():
            book.display_info()
            print("-" * 40)

def main():
    library = Library()
    
    while True:
        print("\nLibrary Menu:")
        print("1. Add a new book")
        print("2. Check out a book")
        print("3. Return a book")
        print("4. Display information about a specific book")
        print("5. Display all books in the library")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                library.add_book()
            elif choice == 2:
                library.check_out_book()
            elif choice == 3:
                library.return_book()
            elif choice == 4:
                library.display_book_info()
            elif choice == 5:
                library.display_all_books()
            elif choice == 6:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
