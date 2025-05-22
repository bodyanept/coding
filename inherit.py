from abc import ABC, abstractmethod

# TASK 1.1
class LibaryUser(ABC):
    name = ''
    user_id = 0
    borrowed_books = []
    def __init__(self,name,user_id):
        self.name = name
        self.idshnik = user_id
        self.borrowed_books = []
        
    
    
    @abstractmethod
    def borrow_book(self,book):
        pass
        
        
    @abstractmethod
    def return_book(self,book):
        pass
        
        



# TASK 1.2

class Student(LibaryUser):
    def borrow_book(self,book):
        self.borrowed_books.append(book)

        
    def return_book(self,book):
        print(f'Пользователь {self.name} вернул книгу {book}')
        
    def list_book(self,*books):
        if len(books) > 3:
            print('Лимит для студента: не больше трех книг')
        else:
            for book in books:
                self.borrow_book(book)
            print(f'Студент {self.name} взял следующие книги: ')
            for book in self.borrowed_books:
                print(book)
        
class Teacher(Student):
    def list_book(self,*books):
        if len(books) > 5:
            print('Лимит для препода: не больше пяти книг')
        else:
            for book in books:
                self.borrow_book(book)
            print(f'Препод {self.name} взял следующие книги: ')
            for book in self.borrowed_books:
                print(book)   
user1 = Student('John', 0)
user1.list_book('aaa','bbb','ccc')

teacher = Teacher('Maria Ivanovna', 1)
teacher.list_book('aaa','bbb','ccc','ddd','eee')
# TASK 1.3

class Book:
    def __init__(self,title, author, isbn, available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
    
    

books = []

