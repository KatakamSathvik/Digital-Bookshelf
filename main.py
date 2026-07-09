DATA_FILE = "library.json"

from library_oop import Library
from book import Book

library = Library()
library.load_library(DATA_FILE)

def valid_year(year:int)->bool:
    try:
        int(year)
        return True
    except:
        return False

def display_menu()->None:
    print("\n---Personal Library Manager---")
    print("1. Add a Book")
    print("2. List all Book")
    print("3. Search for a Book")
    print("4. Remove a Book")
    print("5. Edit a book")
    print("6. books by author")
    print("7. Quit\n")

def choice()->int:
    while True:
        user_choice = input("Enter your choice(1-7): ")
        if user_choice in ('1', '2', '3', '4', '5','6', '7'):
            return int(user_choice)
        print("invalid choice. please enter a digit 1-7.")

print("Welcome to Your Library Manager!")

def display_books(books:list[Book])->None:
        for index, book in enumerate(books, start=1):
            print(f"{index}. {book.title} by {book.author} ({book.year})")

while True:
    display_menu()
    user_choice = choice()
    match user_choice:
        case 1:
            title = input("enter the book title: ").strip().title()
            author = input("enter the author: ").strip().title()
            while True:
                year = input("enter the publication year: ").strip()
                if valid_year(year):
                    year = int(year)
                    break
                print("please enter a valid number.")
            book = {"title": title, "author": author, "year": year}
            library.add_book(Book.from_dict(book))
            library.save_library(DATA_FILE)
            print(f"{title} added successfully.")

        case 2:
            book_list = library.get_books()
            display_books(book_list)

        case 3:
            query = input("Enter the title or author: ").strip().lower()
            results = library.search_book(query)
            if results:
                print(f"found {len(results)} books.")
                display_books(results)
            else:
                print("no matching books found.")

        case 4:
            query = input("enter the exact title to remove: ").strip().lower()
            if library.remove_book(query):
                print(f"{query} removed successfully.")
                library.save_library(DATA_FILE)
            else:
                print(f"{query} not found")

        case 5:
            query = input("enter the title: ").strip().lower()
            new_title = input("Enter the updated title(leave it blank to keep it unchanged): ").strip()
            if new_title == '':
                new_title = None
            new_author = input("Enter the updated author(leave it blank to keep it unchanged): ").strip()
            if new_author=='':
                new_author = None
            while True:
                new_year = input("Enter the updated year(leave it blank to keep it unchanged): ").strip()
                if new_year == '':
                    new_year = None
                    break
                if valid_year(new_year):
                    new_year = int(new_year)
                    break
                print("enter a valid number.")
            if library.edit_book(query, new_title, new_author, new_year):
                print(f"{query} updated successfully.")
                library.save_library(DATA_FILE)
            else:
                print("no matching book found.")

        case 6:
            author = input("enter the author name: ").strip().lower()
            results = library.books_by_author(author)
            if results:
                print(f"found {len(results)} books by {results[0].author}.")
                display_books(results)
            else:
                print("no matching books found.")

        case 7:
            print("Goodbye!")
            break