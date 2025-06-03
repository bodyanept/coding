class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display_info(self):
        print(f'''
            Имя:{self.name}
            Вид:{self.species}
            Возраст:{self.age}
        ''')
    
    
    
    
bobik = Animal('Bobik','dog',3)
bobik.display_info()


class Shelter:
    def __init__(self):
        animals = []
