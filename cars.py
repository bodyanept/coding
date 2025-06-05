class Vehicle:
    
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        
    
    def drive(self, distance):
        self.mileage += distance
        print(f'пробег увеличился на {distance}, теперь пробег равен {self.mileage} км')
        
    def display_info(self):
        print(f'''
            Марка:{self.brand}
            Модель:{self.model}
            Год выпуска:{self.year}
            Пробег:{self.mileage}
        ''')
        
banan = Vehicle('Mercedes', 'CLS', 2014, 13892)
banan.display_info()
