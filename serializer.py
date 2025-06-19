import json

class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def get_info(self):
        print(f'{self.name}, {self.author}, {self.year}')
        
    def to_dict(self):
        return {
            "name": self.name,
            "author": self.author,
            "year": self.year
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["author"], data["year"])   

class libary:
    books = []
    def add_book(self, book):
        self.books.append(book)
        self.save()
    
    def del_book(self, name):
        for book in self.books:
            if name in book.name:
                self.books.remove(book)
        self.save()
    
    def display_info(self):
        for book in self.books:
            print(book.name, book.author, book.year)
    
    def save(self):
        data = []
        for book in self.books:
            data.append(book.to_dict())
        with open("filename.json", "w") as f:
            json.dump(data, f)
        
    def load(self):
        try:
            with open("filename.json", "r") as f:
                data = json.load(f)
            self.books = []
            for item in data:
                book = Book.from_dict(item)
                self.books.append(book)
        except FileNotFoundError as e:
            print('Файл не найден')
    
libary = libary()
libary.load()
b1 = Book('kniga zhalob i predlozheniy','bodyan',1980)
b2 = Book('kniga one','antipin',1318)
b3 = Book('kniga four','lelik',2000)
libary.add_book(b1)
libary.add_book(b2)
libary.add_book(b3)
while True:
    act = int(input(f'''
    выберите действие с книгой:
    1 - добавить
    2 - удалить
    3 - вывести список книг
    '''))
    
    if act == 1:
        name = str(input('Какую книгу хотите добавить?'))
        author = str(input('Кто автор?'))
        year = int(input('Какого она года?'))
        libary.add_book(Book(name,author,year))
    elif act == 2:
        name = input('Какую книгу хотите удалить?')
        libary.del_book(name)
    elif act == 3:
        libary.display_info()
        
        
        
