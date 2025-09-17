from mylibrary import Library

def show_menu():
    print("\n Library Menu:")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Show All Books")
    print("5. Exit")

def main():
    my_library = Library()

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            my_library.add_book(title, author)

        elif choice == "2":
            title = input("Enter title of book to remove: ")
            my_library.remove_book(title)

        elif choice == "3":
            title = input("Enter title to search: ")
            book = my_library.search_book(title)
            if book:
                print(f" Found: {book}")
            else:
                print(" Book not found.")

        elif choice == "4":
            my_library.show_books()

        elif choice == "5":
            print(" Exiting the library system. Goodbye!")
            break

        else:
            print(" Invalid choice. Please try again.")

if __name__ == "__main__":
    main()