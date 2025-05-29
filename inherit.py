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
    limit = 3
    
    
    def borrow_book(self,book):
        if len(self.borrowed_books) < self.limit:
            if book.available:
                self.borrowed_books.append(book)
                print(f'{self.name} взял книгу {book.title}')
                book.available = False
            else:
                print(f'книгу {book.title} кто то уже забрал, приходите позже')
        else:
            print(f'{self.name} исчерпал свой лимит')

        
    def return_book(self,book):
        if book in self.borrowed_books:
            print(f'{self.name} вернул книгу {book.title}')
            self.borrowed_books.remove(book)
            book.available = True
        else:
            print(f'ты не брал книгу {book.title} ')
        
        
    def list_book(self):
        print(f'Студент {self.name} взял следующие книги: ')
        for book in self.borrowed_books:
            print(book.title)
        
class Teacher(Student):
    limit = 5
    def list_book(self):
        print(f'Препод {self.name} взял следующие книги: ')
        for book in self.borrowed_books:
            print(book.title)  
                


student = Student('John', 0)


teacher = Teacher('Maria Ivanovna', 1)

# TASK 1.3

class Book:
    def __init__(self,title, author, isbn, available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
    
    

class Libary:
    books = []
    
    
    
    def add_book(self, Book):
        if Book in self.books:
            print(f'книга {Book.title} уже есть в библиотеке')
        else:
            self.books.append(Book)
            print(f'книга {Book.title} добавлена в библиотеку')
            
    def remove_book(self,Book):
        if Book in self.books:
            self.books.remove(Book)
            print(f'книга {Book.title} больше нет в библиотеке')
        else:
            print(f'книги {Book.title} не бывало в этой библиотеке')


    def find_book_by_title(self,title):
        for book in self.books:
            if book.title == title:
                print(f'книга {title} есть в библиотеке')
            else:
                print(f'книги {title} нет в библиотеке')
                
    
    def list_available_books(self):
        print('В наличии имеются следующие книги:')
        for book in self.books:
            if book.available == True:
                print(f'{book.title}')

                
book1 = Book('booky title','booka author', 33500, True)            
book2 = Book('rocky','chak chak nori', 152, True)            
book3 = Book('romka i zhulen','kakoy-to author', 11, True)            
book4 = Book('arrrw','chuchuka', 89, True)            
book5 = Book('fffffffffffa','ina', 2, False)            
book6 = Book('ooooo','kuper', 7, True)            
book7 = Book('luntik b mahachkale','uci', 5, True)            
libary = Libary()

libary.add_book(book1)
libary.add_book(book2)
libary.add_book(book3)
libary.add_book(book4)
libary.add_book(book5)
libary.add_book(book6)
libary.add_book(book7)
print('          ')
# libary.add_book(book2)
# libary.remove_book(book2)
# libary.remove_book(book2)
# libary.find_book_by_title('booky title')
# libary.find_book_by_title('booky titlee')
# student.borrow_book(book1)
# student.borrow_book(book2)
# student.borrow_book(book3)
# student.borrow_book(book4)

# teacher.borrow_book(book1)
# teacher.borrow_book(book2)
# teacher.borrow_book(book3)
# teacher.borrow_book(book4)
# teacher.borrow_book(book7)
# teacher.borrow_book(book6)

student.return_book(book1)
libary.list_available_books()
