class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def get_info(self):
        print(f'{self.name}, {self.author}, {self.year}')
        

class libary:
    def add_book(self,book):
        pass
    
    def del_book(self,book):
        pass
    
    def display_info(self):
        pass
    
while True:
    input(f'''
    выберите действие с книгой:
    1 - добавить
    2 - удалить
    3 - вывести список книг
    ''')

    if act == 1:
        libary.add_book()
    elif act == 2:
        libary.del_book()
    elif act == 3:
        libary.display_info()
        
        
