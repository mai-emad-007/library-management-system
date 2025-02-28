from abc import ABC, abstractmethod

# Define the abstract Item class with common methods
class Item(ABC):
    def __init__(self, title, author, price):
        # Initialize an item with title, author, and price
        self.__title = title  # Encapsulated attribute
        self.__author = author  # Encapsulated attribute
        self.__price = price  # Encapsulated attribute

    @abstractmethod
    def get_details(self):
        # Abstract method to get details of an item
        pass

    @abstractmethod
    def get_genre(self):
        # Abstract method to get the genre of an item
        pass

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    # Getter method for price
    def get_price(self):
        return self.__price

    # Setter method for price
    def set_price(self, new_price):
        self.__price = new_price

    def update_price(self, new_price):
        # Update the price of an item using the setter method
        self.set_price(new_price)

# Define Book subclass inheriting from Item
class Book(Item):
    def __init__(self, title, author, price, genre, num_pages):
        # Initialize a book with attributes like title, author, price, genre, and number of pages
        super().__init__(title, author, price)
        self.genre = genre
        self.num_pages = num_pages

    def get_details(self):
        # Overridden method to get details of the book including its attributes
        return f'{self.get_title()} by {self.get_author()}. ${self.get_price():.2f}, genre: {self.genre}, pages: {self.num_pages}'

    def get_genre(self):
        return self.genre

# Define Magazine subclass inheriting from Item
class Magazine(Item):
    def __init__(self, title, author, price, issue_number, publication_date, editor):
        # Initialize a magazine with attributes like title, author, price, issue_number, publication_date, and editor
        super().__init__(title, author, price)
        self.issue_number = issue_number
        self.publication_date = publication_date
        self.editor = editor

    def get_details(self):
        # Overridden method to get details of the magazine including its attributes
        return f'{self.get_title()} by {self.get_author()}. ${self.get_price():.2f}, issue: {self.issue_number}, published: {self.publication_date}, Editor: {self.editor}'

    def get_genre(self):
        return "Magazine"

# Define DVD subclass inheriting from Item
class DVD(Item):
    def __init__(self, title, author, price, director, duration, genre):
        # Initialize a DVD with attributes like title, author, price, director, duration, and genre
        super().__init__(title, author, price)
        self.director = director
        self.duration = duration
        self.genre = genre

    def get_details(self):
        # Overridden method to get details of the DVD including its attributes
        return f'{self.get_title()} by {self.get_author()}. ${self.get_price():.2f}, Director: {self.director}, Duration: {self.duration} minutes, Genre: {self.genre}'

    def get_genre(self):
        return self.genre

# Define the Bookstore class to manage inventory, orders, and sales
class Bookstore:
    def __init__(self):
        self.inventory = []
        self.orders = []
        self.total_sales = 0.0

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print("Item not found in Inventory.")

    def display_inventory(self):
        print("Current Inventory:")
        self.display_items(self.inventory)

    def display_items(self, items):
        print("Items in Inventory:")
        print("-------------------------------")
        print("{:<25} {:<15} {:<15} {:<15}".format("Name", "Author", "Genre", "Price ($)"))
        print("-------------------------------")
        for item in items:
            print("{:<25} {:<15} {:<15} {:<15.2f}".format(item.get_title(), item.get_author(), item.get_genre(), item.get_price()))
        print("-------------------------------")

    def search_item_by_name(self, name):
        found_items = [item for item in self.inventory if name.lower() in item.get_title().lower()]
        if found_items:
            print(f"Found {len(found_items)} item(s) with name '{name}':")
            self.display_items(found_items)
        else:
            print(f"No item found with name '{name}'.")

    def search_item_by_author(self, author):
        found_items = [item for item in self.inventory if author.lower() in item.get_author().lower()]
        if found_items:
            print(f"Found {len(found_items)} item(s) by author '{author}':")
            self.display_items(found_items)
        else:
            print(f"No item found by author '{author}'.")

    def search_item_by_genre(self, genre):
        found_items = [item for item in self.inventory if isinstance(item, (Book, DVD)) and genre.lower() in item.get_genre().lower()]
        if found_items:
            print(f"Found {len(found_items)} item(s) in genre '{genre}':")
            self.display_items(found_items)
        else:
            print(f"No item found in genre '{genre}'.")

    def place_order(self, item_idx, quantity=1):
        if 0 <= item_idx < len(self.inventory):
            item = self.inventory[item_idx]
            ordered_item = {
                "name": item.get_title(),
                "author": item.get_author(),
                "price": item.get_price(),
                "quantity": quantity
            }
            self.orders.append(ordered_item)
            self.total_sales += item.get_price() * quantity
            print(f"Order placed successfully for '{item.get_title()}' x{quantity}.")
        else:
            print("Invalid item index. Please select a valid item.")

    def display_orders(self):
        if self.orders:
            print("Current Orders:")
            print("-------------------------------")
            print("{:<25} {:<15} {:<15} {:<15}".format("Name", "Author", "Price ($)", "Quantity"))
            print("-------------------------------")
            for order in self.orders:
                print("{:<25} {:<15} {:<15.2f} {:<15}".format(order["name"], order["author"], order["price"], order["quantity"]))
            print("-------------------------------")
        else:
            print("No orders placed yet.")

    def display_total_sales(self):
        print(f"Total Sales: ${self.total_sales:.2f}")

# Function to handle user interactions
def bookstore_app():
    bookstore = Bookstore()
    # Define initial items and add to inventory
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 12.99, "Classic", 180)
    magazine1 = Magazine("National Geographic", "Various", 5.99, "May 2024", "May 2024", "Editor-in-Chief")
    dvd1 = DVD("Inception", "Christopher Nolan", 9.99, "Christopher Nolan", 148, "Science Fiction")
    # Add items to the inventory
    bookstore.add_item(book1)
    bookstore.add_item(magazine1)
    bookstore.add_item(dvd1)

    # Main loop for user interaction
    while True:
        print("\nWelcome to the Bookstore Management System")
        print("1. Display Inventory")
        print("2. Search Item by Name")
        print("3. Search Item by Author")
        print("4. Search Item by Genre")
        print("5. Place Order")
        print("6. Display Orders")
        print("7. Display Total Sales")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            bookstore.display_inventory()
        elif choice == '2':
            name = input("Enter the name of the item you want to search: ")
            bookstore.search_item_by_name(name)
        elif choice == '3':
            author = input("Enter the author's name you want to search: ")
            bookstore.search_item_by_author(author)
        elif choice == '4':
            genre = input("Enter the genre you want to search: ")
            bookstore.search_item_by_genre(genre)
        elif choice == '5':
            # Exception handling
            try:
                item_idx = int(input("Enter the index of the item you want to order: "))
                quantity = int(input("Enter the quantity: "))
                bookstore.place_order(item_idx, quantity)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        elif choice == '6':
            bookstore.display_orders()
        elif choice == '7':
            bookstore.display_total_sales()
        elif choice == '8':
            print("Thank you for using the Bookstore Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 8.")

# Run the bookstore application if this script is executed as the main module
if __name__ == "__main__":
    bookstore_app()