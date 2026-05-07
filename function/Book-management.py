books = []   # FIXED: use list instead of dict

def add_book():
    book = {
        "id": input("Enter Book id: "),
        "title": input("Enter Title: "),
        "author": input("Enter author: "),
        "year": input("Enter year: ")
    }
    books.append(book)
    print("Book added successfully.")

def view_books():
    if not books:
        print("No Book available.")
        return
    for book in books:
        print(book)

def search_book():
    title = input("Enter title to search: ").lower()
    for book in books:
        if book["title"].lower() == title:
            print("Book Found:", book)
            return
    print("Book not found.")

def delete_book():
    book_id = input("Enter Book ID to delete: ")
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            print("Book deleted.")
            return
    print("Book not found.")

while True:
    print("\n--- Book Management ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book by Title")
    print("4. Delete Book by ID")
    print("5. Exit")
    
    choice = input("Enter choice: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        view_books()
    elif choice == '3':
        search_book()
    elif choice == '4':
        delete_book()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")