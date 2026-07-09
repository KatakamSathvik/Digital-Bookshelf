class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
    
    def to_dict(self):
        return {"title":self.title, "author":self.author, "year":self.year}
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['title'], data['author'], data['year'])
