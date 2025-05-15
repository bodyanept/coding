class book:
    name = None
    author = None
    year = None
    
    def add_book(self,name,author,year):
        self.name = name
        self.author = author
        self.year = year
    def get_info(self):
        print(f'Книга: {self.name}, Автор: {self.author}, Год издания: {self.year}')
        
        
book1 = book() 
book2 = book()
book3= book()

book1.add_book('Война и мир','Лев Толстой',1867 )
book2.add_book('Преступление и наказание','Федор Достоевский',1866 )
book3.add_book('Война и мир','Лев Толстой',1867 )


book1.get_info()
book2.get_info()
book3.get_info()
