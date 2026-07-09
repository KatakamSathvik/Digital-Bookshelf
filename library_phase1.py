import json
import os

DATA_FILE = "library.json"

def valid_year(year):
    try:
        int(year)
        return True
    except:
        return False

def isEmpty(list):
    if len(list)==0:
        return True
    return False

def display_menu():
    print("\n---Personal Library Manager---")
    print("1. Add a Book")
    print("2. List all Book")
    print("3. Search for a Book")
    print("4. Remove a Book")
    print("5. Edit a book")
    print("6. books by author")
    print("7. Quit\n")

def save_library(library):
    library.sort(key=lambda book: (book['title'], book['year'], book['author']))
    with open(DATA_FILE, "w") as file:
        json.dump(library, file, indent=2)

def add_book(library):
    title = input("enter the book title: ").strip().title()
    author = input("enter the author: ").strip().title()
    while True:
        year = input("enter the publication year: ").strip()
        if valid_year(year):
            year = int(year)
            break
        print("please enter a valid number.")
    book = {"title": title, "author": author, "year": year}
    library.append(book)
    save_library(library)
    print(f"'{title}' added successfully!")

def list_books(library):
    if len(library)==0:
        print("your library is empty")
    else:
        for index, book in enumerate(library, start=1):
            print(f"{index}. {book['title']} by {book['author']} ({book['year']})")

def search_books(library):
    if isEmpty(library):
        print("your library is empty. nothing to search.")
        return
    query = input("enter a title or author to search: ").strip().lower()
    results = []
    for book in library:
        if query in book["title"].lower() or query in book["author"].lower():
            results.append(book)
    if isEmpty(results):
        print("no matching books found.")
    else:
        print(f"found {len(results)} books.")
        for index,book in enumerate(results, start=1):
            print(f"{index}. {book['title']} by {book['author']} {book['year']}")

def remove_book(library):
    if isEmpty(library):
        print("your library is empty. nothing to remove.")
        return
    title = input("enter the exact title of the book to remove: ").strip().lower()
    for index, book in enumerate(library):
        if book["title"].lower()==title:
            temp = book
            library.pop(index)
            save_library(library)
            print(f"'{temp["title"]}' removed successfully.")
            return
    print(f"no book titled '{title}' found.")

def edit_book(library):
    if isEmpty(library):
        print("your library is empty. nothing to edit.")
        return
    query = input("enter the title: ").strip().lower()
    flag = False
    for index,book in enumerate(library):
        if book['title'].lower()==query:
            flag = True
            break
    if not flag:
        print(f"{query} not found.")
        return
    title = input("Enter the updated title(leave it blank to keep it unchanged): ")
    if title !='':
        library[index]['title'] = title.title()
    author = input("Enter the updated author(leave it blank to keep it unchanged): ")
    if author != '':
        library[index]['author'] = author.title()
    while True:
        year = input("Enter the updated year(leave it blank to keep it unchanged): ")
        if year == '':
            break
        if valid_year(year):
            library[index]['year'] = int(year)
            break
        print("enter a valid number.")
    save_library(library)
    print(f"{query} updated successfully.")

def books_by_author(library):
    if isEmpty(library):
        print("library is empty.")
        return
    author = input("Enter the author name: ").strip().lower()
    results = []
    for book in library:
        if author in book['author'].lower():
            results.append(book)
    if isEmpty(results):
        print(f"no books found by {author}")
        return
    print(f"there are {len(results)} books by {results[0]['author']}")
    list_books(results)

def choice():
    while True:
        user_choice = input("Enter your choice(1-7): ")
        if user_choice in ('1', '2', '3', '4', '5','6', '7'):
            return int(user_choice)
        print("invalid choice. please enter a digit 1-7.")

def load_library():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return(json.load(file))
    return []

def main():
    print("Welcome to Your Library Manager!")
    library = load_library()
    print(f"loaded {len(library)} books.")
    while True:
        display_menu()
        user_choice = choice()
        match user_choice:
            case 1:
                add_book(library)
            case 2:
                list_books(library)
            case 3:
                search_books(library)
            case 4:
                remove_book(library)
            case 5:
                edit_book(library)
            case 6:
                books_by_author(library)
            case 7:
                print("Goodbye!")
                break
    
if __name__=="__main__":
    main()

