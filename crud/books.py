from core.db_settings import execute_query
from crud.category import show_all_categories


def add_book():
    if show_all_categories() is None:
        return None
    category_id = input("Enter category id: ")
    # check this id is existing or not

    name = input("Enter book name: ")
    author = input("Enter book author: ")
    note = input("Enter note: ")
    status = input("Enter book status(done,ongoing,new): ")
    query = "INSERT INTO books (category_id, name, author, note, status) VALUES (%s, %s, %s, %s, %s)"
    params = (category_id, name, author, note, status,)
    if execute_query(query=query, params=params):
        print("Books is added")
        return None
    else:
        print("Something getting wrong, please try again later")
        return True

def delete_book(books_list):
    book_id = int(input("Enter book id you want to delete: "))

    for book in books_list:
        if book['id'] == book_id:
            books_list.remove(book)
            print(f"🗑 '{book['title']}' deleted")
            return books_list

    print("Book not found")
    return books_list

def search_books(books_list):
    query = input("Enter book name or author or note to find a book: ").lower()

    results = []
    for book in books_list:
        full_info = f"{book['title']} {book['author']} {book['note']}".lower()

        if query in full_info:
            results.append(book)

    if results:
        print(f"\n🔍 {len(results)} number of books found: ")
        for b in results:
            print(f"ID: {b['id']} | Nomi: {b['title']} | Muallifi: {b['author']} | Note: {b['note']}")
    else:
        print("Book not found.")
