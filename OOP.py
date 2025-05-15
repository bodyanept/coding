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



class BankAccount:
    number = None
    balance = None
    
    def __init__(self,number,balance):
        self.__number = number
        self.__balance = balance
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print('Вы не можете положить меньше 0 рублей)')
            
    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('на вашем счете не достаточно средств')
    def get_balance(self):
        print (self.__balance)
    def get_number(self):
        print (self.__number)
        

        
account = BankAccount(123456,1000)
account.deposit(500)

account.get_balance()
account.get_number()
