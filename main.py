from crud.books import add_book
from crud.category import add_category, show_all_categories


def main():
    print("""
    1. Add category
    2. Delete category
    3. Show all category
    4. Show all books
    5. Add book
    6. Delete book
    7. Search book | name, author, note, category
    8. Exit
    """)
    option = input("Enter your option: ")
    if option == "1":
        add_category()
    elif option == "2":
        pass
    elif option == "3":
        show_all_categories()
    elif option == "4":
        pass
    elif option == "5":
        add_book()
    elif option == "6":
        pass
    elif option == "7":
        pass
    elif option == "8":
        print("Goodbye")
        return None
    else:
        print("Invalid option")
    return main()


if __name__ == '__main__':
    # execute_query(category)
    # execute_query(books)
    main()
