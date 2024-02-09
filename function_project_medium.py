# Define global variables
books = []

# Function to display menu
def display_menu():
    print("Welcome to the Library Management System")
    print("1. Add a book")
    print("2. Display available books")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Display borrowed books")
    print("6. Exit")

# Function to add a book
def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    books.append({'title': title, 'author': author})
    print("Book added successfully!")

# Function to display available books
def display_books():
    if books:
        print("Available Books:")
        for book in books:
            print(f"Title: {book['title']}, Author: {book['author']}")
    else:
        print("No books available in the library.")

# Function to borrow a book
def borrow_book():
    display_books()
    title = input("Enter the title of the book you want to borrow: ")
    for book in books:
        if book['title'] == title:
            books.remove(book)
            print(f"You have borrowed '{title}' successfully.")
            return
    print(f"'{title}' is not available in the library.")

# Function to return a book
def return_book():
    title = input("Enter the title of the book you want to return: ")
    author = input("Enter the author of the book: ")
    books.append({'title': title, 'author': author})
    print(f"You have returned '{title}' successfully.")

# Function to display borrowed books
def display_borrowed_books():
    borrowed_books = [book['title'] for book in books]
    if borrowed_books:
        print("Borrowed Books:")
        for book in borrowed_books:
            print(book)
    else:
        print("No books are currently borrowed.")

# Main function to run the program
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            display_books()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            display_borrowed_books()
        elif choice == '6':
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
