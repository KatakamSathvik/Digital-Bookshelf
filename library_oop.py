from book import Book
import json

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book:Book)->None:
        self.books.append(book)
    
    def search_book(self, query:str)->list[Book]:
        results = []
        for book in self.books:
            if query in book.title.lower() or query in book.author.lower():
                results.append(book)
        return results
    
    def remove_book(self, title:str)->bool:
        for index,book in enumerate(self.books):
            if book.title.lower()==title:
                self.books.pop(index)
                return True
        return False

    def edit_book(self, old_title:str, new_title:str=None, new_author:str=None, new_year:str=None)->bool:
        if len(self.books)==0:
            return False
        for book in self.books:
            if book.title.lower() == old_title.lower():
                if new_title != None:
                    book.title = new_title.title()
                if new_author != None:
                    book.author = new_author.title()
                if new_year != None:
                    book.year = new_year
                return True
        return False

    def books_by_author(self, author:str)->list[Book]:
        results = []
        for book in self.books:
            if author.lower() == book.author.lower():
                results.append(book)
        return results
        
    def get_books(self)->list[Book]:
        return self.books

    def save_library(self, file)->None:
        book_list = []
        for book in self.books:
            book_list.append(book.to_dict())
        book_list.sort(key=lambda book: (book['title'], book['year'], book['author']))
        with open(file, "w") as f:
            json.dump(book_list, f, indent=2)
        
    def load_library(self, file)->None:
        with open(file, "r") as f:
            book_list = json.load(f)
        for book in book_list:
            self.books.append(Book.from_dict(book))