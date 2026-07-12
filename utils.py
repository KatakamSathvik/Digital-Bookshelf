from book import Book

def display_menu()->None:
    print("\n---Personal Library Manager---")
    print("1. Add a Book")
    print("2. List all Book")
    print("3. Search for a Book")
    print("4. Remove a Book")
    print("5. Edit a book")
    print("6. Quit\n")

def search_display():
    print("1. Search book By title")
    print("2. Search books By author")
    print("3. Search books By year range")
    print("4. Search book In a year")

def choice(num:int)->int:
    choices = tuple(str(i) for i in range(1, num+1))
    while True:
        user_choice = input(f"Enter your choice(1-{num}): ")
        if user_choice in choices:
            return int(user_choice)
        else:
            print(f"invalid choice. please enter a digit(1-{num}).")

def display_books(books:list[Book])->None:
        for index, book in enumerate(books, start=1):
            print(f"{index}. {book}")


def valid_year(year:str)->bool:
    if year == '':
        return False
    try:
        year = int(year)
    except ValueError:
        return False
    if 1450<=int(year)<=2026:
        return True
    return False

def get_title()->str:
    while True:
        title = input("enter the TITLE: ").strip()
        if title != "":
            title = title.title()
            return title
        print("please enter a title.")

def get_author()->str:
    while True:
        author = input("enter the AUTHOR NAME: ").strip()
        if author != "":
            author = author.title()
            return author
        print("please enter the author name.")

def get_year(start_end:str='')->int:
    while True:
        year = input(f"enter the {start_end}YEAR: ").strip()
        if valid_year(year):
            return int(year)
        print("enter a valid year.")

def update_book()->tuple[str, str|None, str|None, int|None]:
    while True:
        old_title = input("enter TITLE of the book you want to update: ").strip()
        if old_title != '':
            break
        print("please enter the title.")
    new_title = input("enter NEW TITLE (or) leave it blank: ").strip()
    if new_title == '':
        new_title = None
    new_author = input("enter NEW AUTHOR (or) leave it blank: ").strip()
    if new_author == '':
        new_author = None
    while True:
        new_year = input("enter the NEW YEAR (or) leave it blank: ").strip()
        if new_year == '':
            new_year = None
            break
        if not valid_year(new_year):
            print("please enter a valid year to update the year.")
        
    return old_title, new_title, new_author, new_year      
